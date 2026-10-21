from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_evaluate_endpoint_with_matching_answers():
    response = client.post(
        "/evaluate",
        json={
            "expected_answer": "Python is useful",
            "actual_answer": "python is useful",
        },
    )

    assert response.status_code == 200
    assert response.json()["exact_match"] is True
    assert response.json()["similarity_score"] == 1.0


def test_evaluate_endpoint_with_different_answers():
    response = client.post(
        "/evaluate",
        json={
            "expected_answer": "New York",
            "actual_answer": "New Jersey",
        },
    )

    assert response.status_code == 200
    assert response.json()["exact_match"] is False


def test_evaluate_endpoint_rejects_empty_answers():
    response = client.post(
        "/evaluate",
        json={
            "expected_answer": "",
            "actual_answer": "Some answer",
        },
    )

    assert response.status_code == 422
