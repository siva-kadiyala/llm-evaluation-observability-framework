# LLM Evaluation & Observability Framework

A Python-based framework for evaluating Large Language Model (LLM) responses, measuring text similarity, and maintaining evaluation history through REST APIs.

The project provides a foundation for testing LLM outputs, validating response quality, and building automated evaluation workflows for Generative AI applications.

## Project Overview

LLM applications need reliable ways to compare generated responses against expected answers. This project implements an evaluation API that calculates exact-match results, measures text similarity, and records evaluation results for review.

The framework is being developed incrementally, with automated tests and continuous integration through GitHub Actions.

## Key Features

- **LLM Response Evaluation:** Compare expected answers with actual model responses.
- **Exact Match Evaluation:** Check whether two text responses match after basic text normalization.
- **Text Similarity Scoring:** Calculate a similarity score between expected and actual responses.
- **Evaluation History:** Store evaluation inputs, results, and UTC timestamps in memory.
- **REST API:** Expose evaluation functionality through FastAPI endpoints.
- **Input Validation:** Validate incoming requests using Pydantic models.
- **Automated Testing:** Run Python tests using pytest.
- **Continuous Integration:** Execute the configured test suite through GitHub Actions.

## Technology Stack

- **Programming Language:** Python
- **API Framework:** FastAPI
- **Data Validation:** Pydantic
- **Evaluation Logic:** Python string normalization and similarity scoring
- **Testing:** pytest
- **HTTP Testing:** HTTPX
- **Data Processing:** Pandas
- **CI/CD:** GitHub Actions
- **Version Control:** Git and GitHub

## Project Structure

```text
llm-evaluation-observability-framework/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── evaluation/
│   └── metrics.py
│
├── tests/
│   ├── test_api.py
│   └── test_metrics.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## API Endpoints

The application exposes the following REST API endpoints.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check application health |
| POST | `/evaluate` | Evaluate two text responses |
| GET | `/evaluations` | Retrieve stored evaluation results |
| DELETE | `/evaluations` | Clear evaluation history |

### Health Check

**Request**

```http
GET /health
```

**Example response**

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

**Example request body**

```json
{
  "expected_answer": "Paris is the capital of France.",
  "actual_answer": "Paris is the capital of France."
}
```

**Example response**

```json
{
  "exact_match": true,
  "similarity_score": 1.0
}
```

The similarity score ranges from `0.0` to `1.0`. The exact score depends on the implemented text similarity calculation.

### Retrieve Evaluation History

**Request**

```http
GET /evaluations
```

Returns the evaluation records stored during the current application process, including the expected answer, actual answer, evaluation results, and timestamp.

### Clear Evaluation History

**Request**

```http
DELETE /evaluations
```

Clears the in-memory evaluation history.

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

### 3. Start the Application

```bash
python -m uvicorn app.main:app --reload
```

The API will start locally at:

`http://127.0.0.1:8000`

### 4. Open Interactive API Documentation

Open the following URL in your browser:

`http://127.0.0.1:8000/docs`

Use the Swagger UI to explore the endpoints, submit evaluation requests, and review their responses.

### 5. Run Automated Tests

```bash
python -m pytest -v
```

The test suite covers the evaluation metrics and API functionality implemented in the repository.

## Continuous Integration

GitHub Actions is configured to run the Python test workflow when changes are pushed to the configured branch or a pull request is opened.

The workflow checks the configured automated tests and helps identify issues before additional changes are introduced.

## Current Limitations

- Evaluation history is stored in memory and is lost when the application restarts.
- Text similarity scoring is a basic text-based metric, not a semantic embedding-based evaluation.
- Token usage, model latency, and production monitoring are not yet implemented.
- Integration with external LLM providers is not yet implemented.
- Persistent storage and historical reporting are planned enhancements.

## Planned Enhancements

- Add semantic similarity evaluation using embedding models.
- Integrate multiple LLM providers.
- Track latency, token usage, and evaluation errors.
- Support repeatable evaluation datasets and prompt comparisons.
- Generate evaluation reports in JSON and CSV formats.
- Add persistent storage for evaluation history.
- Introduce Docker-based deployment.
- Expand automated tests and evaluation metrics.

## Project Goals

The goal is to develop a practical framework for testing LLM application outputs, tracking evaluation results, and building a foundation for Generative AI quality assurance and observability.

## Author

**Siva Kadiyala**

GitHub: https://github.com/siva-kadiyala

---

*This project is under active development. Features and documentation will be updated as the framework evolves.*
