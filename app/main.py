
from datetime import datetime, timezone
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

from evaluation.metrics import exact_match, similarity_score


app = FastAPI(
    title="LLM Evaluation API",
    description="API for evaluating LLM responses and tracking evaluation results.",
    version="0.2.0",
)


class EvaluationRequest(BaseModel):
    expected_answer: str = Field(min_length=1)
    actual_answer: str = Field(min_length=1)


class EvaluationResponse(BaseModel):
    exact_match: bool
    similarity_score: float


class EvaluationRecord(EvaluationResponse):
    expected_answer: str
    actual_answer: str
    timestamp: str


evaluation_history: List[EvaluationRecord] = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/evaluate", response_model=EvaluationResponse)
def evaluate_response(request: EvaluationRequest):
    result = EvaluationResponse(
        exact_match=exact_match(
            request.expected_answer,
            request.actual_answer,
        ),
        similarity_score=similarity_score(
            request.expected_answer,
            request.actual_answer,
        ),
    )

    evaluation_history.append(
        EvaluationRecord(
            expected_answer=request.expected_answer,
            actual_answer=request.actual_answer,
            exact_match=result.exact_match,
            similarity_score=result.similarity_score,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
    )

    return result


@app.get("/evaluations", response_model=List[EvaluationRecord])
def get_evaluations():
    return evaluation_history


@app.delete("/evaluations")
def clear_evaluations():
    evaluation_history.clear()
    return {"message": "Evaluation history cleared"}
