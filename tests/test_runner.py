
from evaluation.runner import load_dataset, evaluate_dataset


def test_load_dataset():
    dataset = load_dataset()

    assert isinstance(dataset, list)
    assert len(dataset) > 0
    assert "question" in dataset[0]
    assert "expected_answer" in dataset[0]


def test_evaluate_dataset_returns_summary():
    dataset = load_dataset()
    report = evaluate_dataset(dataset)

    assert report["total_questions"] == len(dataset)
    assert report["exact_matches"] == len(dataset)
    assert report["exact_match_rate"] == 1.0
    assert 0.0 <= report["average_similarity"] <= 1.0


def test_evaluate_dataset_with_different_answer():
    dataset = [{
        "id": "TEST001",
        "category": "testing",
        "question": "What is Python?",
        "expected_answer": "Python is a programming language."
    }]

    report = evaluate_dataset(
        dataset,
        actual_answers={"TEST001": "Python is a snake."}
    )

    assert report["total_questions"] == 1
    assert report["exact_matches"] == 0
    assert report["exact_match_rate"] == 0.0


def test_evaluate_empty_dataset():
    report = evaluate_dataset([])

    assert report["total_questions"] == 0
    assert report["exact_matches"] == 0
    assert report["exact_match_rate"] == 0.0
    assert report["average_similarity"] == 0.0
