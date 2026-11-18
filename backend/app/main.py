from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .service import triage_flock

app = FastAPI(title="PoultryGuard AI", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class TriageRequest(BaseModel):
    species: str = "chicken"
    age_weeks: int = Field(ge=0, le=200)
    flock_size: int = Field(ge=1, le=100000)
    symptoms: list[str] = Field(min_length=1)
    deaths_last_24h: int = Field(default=0, ge=0)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "poultryguard-api"}


@app.post("/api/v1/triage")
def triage(request: TriageRequest) -> dict:
    return {"id": str(uuid4()), "created_at": datetime.now(timezone.utc).isoformat(), **triage_flock(request.model_dump())}
