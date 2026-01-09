from fastapi import FastAPI
from app.api.routes import router
from app.config.settings import settings

app = FastAPI(
    title="AI Error Log Summarizer",
    description="Analyze distributed system logs and summarize error patterns using LLMs",
    version="1.0.0",
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
