
import json

from evaluation import history


def test_save_evaluation(tmp_path, monkeypatch):
    history_file = tmp_path / "history.json"
    monkeypatch.setattr(history, "HISTORY_PATH", history_file)

    report = {
        "total_questions": 2,
        "exact_matches": 1,
        "exact_match_rate": 0.5,
        "average_similarity": 0.75,
        "results": [],
    }

    saved = history.save_evaluation(report)

    assert saved["total_questions"] == 2
    assert "timestamp" in saved
    assert history_file.exists()

    records = json.loads(
        history_file.read_text(encoding="utf-8")
    )
    assert len(records) == 1
    assert records[0]["exact_match_rate"] == 0.5


def test_load_history(tmp_path, monkeypatch):
    history_file = tmp_path / "history.json"
    history_file.write_text(
        json.dumps([{"exact_match_rate": 0.8}]),
        encoding="utf-8",
    )
    monkeypatch.setattr(history, "HISTORY_PATH", history_file)

    assert history.load_history() == [
        {"exact_match_rate": 0.8}
    ]


def test_compare_latest_runs(tmp_path, monkeypatch):
    history_file = tmp_path / "history.json"
    monkeypatch.setattr(history, "HISTORY_PATH", history_file)

    history_file.write_text(
        json.dumps([
            {
                "timestamp": "2026-10-20T10:00:00+00:00",
                "exact_match_rate": 0.5,
                "average_similarity": 0.6,
            },
            {
                "timestamp": "2026-10-21T10:00:00+00:00",
                "exact_match_rate": 0.8,
                "average_similarity": 0.9,
            },
        ]),
        encoding="utf-8",
    )

    comparison = history.compare_latest_runs()

    assert abs(
        comparison["exact_match_rate_change"] - 0.3
    ) < 1e-9

    assert abs(
        comparison["average_similarity_change"] - 0.3
    ) < 1e-9


def test_compare_with_insufficient_history(
    tmp_path, monkeypatch
):
    history_file = tmp_path / "history.json"
    monkeypatch.setattr(history, "HISTORY_PATH", history_file)
    history_file.write_text("[]", encoding="utf-8")

    comparison = history.compare_latest_runs()

    assert "message" in comparison
