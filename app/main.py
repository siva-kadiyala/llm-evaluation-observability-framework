from fastapi import FastAPI
from pydantic import BaseModel, Field

from evaluation.metrics import exact_match, similarity_score

app = FastAPI(
    title="LLM Evaluation API",
    description="API for checking LLM response similarity.",
    version="0.1.0",
)


class EvaluationRequest(BaseModel):
    expected_answer: str = Field(min_length=1)
    actual_answer: str = Field(min_length=1)


class EvaluationResponse(BaseModel):
    exact_match: bool
    similarity_score: float


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/evaluate", response_model=EvaluationResponse)
def evaluate_response(request: EvaluationRequest):
    return EvaluationResponse(
        exact_match=exact_match(
            request.expected_answer,
            request.actual_answer,
        ),
        similarity_score=similarity_score(
            request.expected_answer,
            request.actual_answer,
        ),
    )
