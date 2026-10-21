
import csv
import json

from evaluation.report import export_json, export_csv


def sample_records():
    return [
        {
            "expected_answer": "Paris",
            "actual_answer": "Paris",
            "exact_match": True,
            "similarity_score": 1.0,
        },
        {
            "expected_answer": "London",
            "actual_answer": "Paris",
            "exact_match": False,
            "similarity_score": 0.2,
        },
    ]


def test_export_json(tmp_path, monkeypatch):
    monkeypatch.setattr("evaluation.report.REPORT_DIR", tmp_path)

    records = sample_records()
    output_path = export_json(records)

    assert output_path.exists()

    with output_path.open("r", encoding="utf-8") as file:
        exported = json.load(file)

    assert exported == records


def test_export_csv(tmp_path, monkeypatch):
    monkeypatch.setattr("evaluation.report.REPORT_DIR", tmp_path)

    records = sample_records()
    output_path = export_csv(records)

    assert output_path.exists()

    with output_path.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        exported = list(csv.DictReader(file))

    assert len(exported) == 2
    assert exported[0]["expected_answer"] == "Paris"
    assert exported[0]["exact_match"] == "True"
    assert exported[1]["actual_answer"] == "Paris"


def test_export_empty_records(tmp_path, monkeypatch):
    monkeypatch.setattr("evaluation.report.REPORT_DIR", tmp_path)

    json_path = export_json([])
    csv_path = export_csv([])

    assert json.loads(
        json_path.read_text(encoding="utf-8")
    ) == []
    assert csv_path.exists()
