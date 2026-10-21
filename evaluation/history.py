
import json
from datetime import datetime, timezone
from pathlib import Path


HISTORY_PATH = Path(__file__).with_name("history.json")


def save_evaluation(report):
    """Save an evaluation report with a timestamp."""
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_questions": report.get("total_questions", 0),
        "exact_matches": report.get("exact_matches", 0),
        "exact_match_rate": report.get("exact_match_rate", 0.0),
        "average_similarity": report.get("average_similarity", 0.0),
        "results": report.get("results", []),
    }

    history = load_history()
    history.append(record)

    HISTORY_PATH.write_text(
        json.dumps(history, indent=2),
        encoding="utf-8",
    )

    return record


def load_history():
    """Load previously saved evaluation reports."""
    if not HISTORY_PATH.exists():
        return []

    with HISTORY_PATH.open("r", encoding="utf-8") as file:
        history = json.load(file)

    if not isinstance(history, list):
        raise ValueError("Evaluation history must be a JSON list.")

    return history


def compare_latest_runs():
    """Compare the two most recent evaluation runs."""
    history = load_history()

    if len(history) < 2:
        return {
            "message": "At least two evaluation runs are required."
        }

    previous = history[-2]
    latest = history[-1]

    return {
        "previous_timestamp": previous["timestamp"],
        "latest_timestamp": latest["timestamp"],
        "exact_match_rate_change": (
            latest["exact_match_rate"]
            - previous["exact_match_rate"]
        ),
        "average_similarity_change": (
            latest["average_similarity"]
            - previous["average_similarity"]
        ),
    }
