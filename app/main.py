from fastapi import FastAPI
from app.health import get_health_status

app = FastAPI(title="DevOps FastAPI Service")

@app.get("/")
def root():
    return {"message": "DevOps FastAPI service is running"}

@app.get("/health")
def health():
    return get_health_status()