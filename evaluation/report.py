
import csv
import json
from pathlib import Path
from typing import List, Dict, Any

REPORT_DIR = Path("reports")


def export_json(
    records: List[Dict[str, Any]],
    filename: str = "evaluation_report.json",
) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REPORT_DIR / filename

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)

    return output_path


def export_csv(
    records: List[Dict[str, Any]],
    filename: str = "evaluation_report.csv",
) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REPORT_DIR / filename

    if not records:
        fieldnames = [
            "expected_answer",
            "actual_answer",
            "exact_match",
            "similarity_score",
            "timestamp",
        ]
    else:
        fieldnames = list(
            dict.fromkeys(
                key for record in records for key in record.keys()
            )
        )

    with output_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    return output_path
