# LLM Evaluation & Observability Framework

A Python-based framework for evaluating Large Language Model (LLM) responses, measuring text similarity, tracking evaluation history, and generating evaluation reports through REST APIs and dataset-based evaluation workflows.

The project provides a foundation for testing LLM outputs, comparing evaluation results, and building automated quality checks for Generative AI applications.

## Project Overview

LLM applications need reliable ways to evaluate response quality and identify changes in model behavior. This project provides evaluation metrics, a dataset-based evaluation runner, REST API endpoints, evaluation history, and JSON/CSV report exports.

The framework uses Python, FastAPI, Pydantic, pytest, and GitHub Actions.

## Key Features

- **LLM Response Evaluation:** Compare expected answers with actual responses.
- **Exact Match Evaluation:** Check whether normalized text responses match.
- **Text Similarity Scoring:** Calculate a text similarity score between expected and actual answers.
- **Dataset-Based Evaluation:** Run evaluations against a JSON dataset containing questions and expected answers.
- **Evaluation History:** Save evaluation results and timestamps for later review.
- **Run Comparison:** Compare evaluation results across runs.
- **REST API:** Expose evaluation functionality through FastAPI endpoints.
- **Input Validation:** Validate API requests using Pydantic models.
- **Report Generation:** Export evaluation summaries and individual results to JSON and CSV.
- **Automated Testing:** Test evaluation logic, API endpoints, reporting, and history functionality using pytest.
- **Continuous Integration:** Run automated tests through GitHub Actions.

## Technology Stack

- **Programming Language:** Python
- **API Framework:** FastAPI
- **Data Validation:** Pydantic
- **Evaluation Metrics:** Exact Match and Text Similarity
- **Dataset Format:** JSON
- **Reporting:** JSON and CSV
- **Testing:** pytest
- **HTTP Testing:** HTTPX
- **Data Processing:** Pandas
- **CI/CD:** GitHub Actions
- **Version Control:** Git and GitHub

## Project Structure

```text
llm-evaluation-observability-framework/
├── .github/
│   └── workflows/
│       └── tests.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── evaluation/
│   ├── dataset.json
│   ├── history.py
│   ├── metrics.py
│   ├── report.py
│   └── runner.py
├── tests/
│   ├── test_api.py
│   ├── test_history.py
│   ├── test_metrics.py
│   └── test_runner.py
├── .gitignore
├── README.md
└── requirements.txt
```

The `app` directory contains the REST API, `evaluation` contains the evaluation logic and reporting modules, and `tests` contains the automated test suite.

## API Endpoints

The application provides REST API endpoints for evaluating responses and managing evaluation history.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check application health |
| POST | `/evaluate` | Evaluate expected and actual responses |
| GET | `/evaluations` | Retrieve stored evaluation history |
| DELETE | `/evaluations` | Clear evaluation history |

### Health Check

**Request**

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### Evaluate an LLM Response

**Request**

```http
POST /evaluate
Content-Type: application/json
```

Example request:

```json
{
  "expected_answer": "Paris is the capital of France.",
  "actual_answer": "Paris is the capital of France."
}
```

Example response:

```json
{
  "exact_match": true,
  "similarity_score": 1.0
}
```

The response fields shown above are illustrative. Actual response fields depend on the API implementation.

### Retrieve Evaluation History

**Request**

```http
GET /evaluations
```

Returns evaluation records stored by the API, subject to the application's current storage implementation.

### Clear Evaluation History

**Request**

```http
DELETE /evaluations
```

Clears evaluation history if supported by the running API implementation.

## Dataset Evaluation

The framework includes a JSON dataset containing questions, categories, and expected answers.

The evaluation runner processes the dataset and calculates metrics for each question, including exact-match results and text similarity scores. Actual answers can also be supplied to evaluate responses from an LLM application.

The runner produces an evaluation summary containing:

- Total number of questions
- Number of exact matches
- Exact-match rate
- Average similarity score
- Individual question results

## Sample Evaluation Output

The following is an illustrative example, not a verified result from an actual execution.

```json
{
  "total_questions": 10,
  "exact_matches": 8,
  "exact_match_rate": 0.8,
  "average_similarity": 0.87
}
```

Evaluation reports can be exported in JSON and CSV formats. Saved evaluation history can be used to review results and compare runs.

## Getting Started

### Prerequisites

- Python 3.10 or later
- Git
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/siva-kadiyala/llm-evaluation-observability-framework.git
cd llm-evaluation-observability-framework
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the API

```bash
python -m uvicorn app.main:app --reload
```

The API should be available locally at:

`http://127.0.0.1:8000`

### 4. Open API Documentation

Open the following URL in your browser:

`http://127.0.0.1:8000/docs`

Use the interactive Swagger UI to explore and test the available API endpoints.

### 5. Run Automated Tests

```bash
python -m pytest -v
```

The tests validate the implemented evaluation metrics, API endpoints, dataset runner, reporting, and history functionality.

### 6. Run the Dataset Evaluation

From the repository root, run:

```bash
python -m evaluation.runner
```

The runner loads the dataset, calculates evaluation metrics, saves evaluation history, exports reports, and prints the evaluation summary, according to the implemented configuration.

## Continuous Integration

GitHub Actions runs the configured Python test workflow when repository changes trigger the workflow.

The workflow helps detect test failures and maintain the project as new evaluation features are added.

## Current Limitations

- Evaluation history may be stored in memory or another configured format; persistence depends on the implementation.
- Text similarity scoring is a basic text-based metric, not necessarily semantic similarity.
- External LLM provider integrations are not yet documented as implemented.
- Token usage, model latency, and production-grade observability require additional implementation.
- The sample evaluation values above are illustrative and should not be treated as benchmark results.

## Planned Enhancements

- Add semantic similarity evaluation using embedding models.
- Integrate external LLM providers for live response evaluation.
- Track response latency, token usage, and evaluation errors.
- Add persistent storage for evaluation history.
- Support prompt-version comparisons and repeatable benchmark datasets.
- Introduce Docker-based deployment.
- Expand evaluation metrics and automated tests.

## Project Goals

The goal is to develop a practical framework for evaluating LLM application outputs, tracking evaluation results, comparing runs, and supporting quality assurance for Generative AI applications.

## Author

**Siva Kadiyala**

GitHub: https://github.com/siva-kadiyala

---

*This project is under active development. Features and documentation will be updated as the framework evolves.*
