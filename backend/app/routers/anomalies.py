from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/anomalies", tags=["anomalies"])

@router.get("/")
def list_anomalies():
    return []
