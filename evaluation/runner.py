
import json
from pathlib import Path

from evaluation.metrics import exact_match, similarity_score
from evaluation.report import export_json, export_csv


DATASET_PATH = Path(__file__).with_name("dataset.json")


def load_dataset():
    """Load questions from the evaluation dataset."""
    with DATASET_PATH.open("r", encoding="utf-8") as file:
        dataset = json.load(file)

    if not isinstance(dataset, list):
        raise ValueError("Dataset must contain a JSON list.")

    return dataset


def evaluate_dataset(dataset, actual_answers=None):
    """Evaluate responses against expected answers."""
    results = []

    for item in dataset:
        question_id = item["id"]
        expected = item["expected_answer"]

        if actual_answers and question_id in actual_answers:
            actual = actual_answers[question_id]
        else:
            actual = expected

        results.append({
            "id": question_id,
            "category": item["category"],
            "question": item["question"],
            "expected_answer": expected,
            "actual_answer": actual,
            "exact_match": exact_match(expected, actual),
            "similarity_score": similarity_score(
                expected, actual
            ),
        })

    total = len(results)
    exact_matches = sum(
        1 for result in results if result["exact_match"]
    )

    average_similarity = (
        sum(result["similarity_score"] for result in results) / total
        if total else 0.0
    )

    return {
        "total_questions": total,
        "exact_matches": exact_matches,
        "exact_match_rate": exact_matches / total if total else 0.0,
        "average_similarity": average_similarity,
        "results": results,
    }


def main():
    dataset = load_dataset()
    report = evaluate_dataset(dataset)

    # Export individual evaluation results.
    export_json(report["results"])
    export_csv(report["results"])

    # Display summary and report locations.
    print(json.dumps({
        "total_questions": report["total_questions"],
        "exact_matches": report["exact_matches"],
        "exact_match_rate": report["exact_match_rate"],
        "average_similarity": report["average_similarity"],
        "json_report": "reports/evaluation_report.json",
        "csv_report": "reports/evaluation_report.csv",
    }, indent=2))


if __name__ == "__main__":
    main()
