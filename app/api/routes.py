from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.analyzer.analyzer import analyze_logs

router = APIRouter()


@router.post("/analyze-logs")
async def analyze_logs_endpoint(file: UploadFile = File(...)):
    if not file.filename.endswith((".log", ".txt")):
        raise HTTPException(status_code=400, detail="Only .log or .txt files are supported")

    raw_bytes = await file.read()
    raw_text = raw_bytes.decode("utf-8", errors="ignore")

    result = analyze_logs(raw_text)

    return JSONResponse(content=result)
