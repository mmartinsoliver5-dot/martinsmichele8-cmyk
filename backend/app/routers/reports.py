from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/reports", tags=["reports"])

@router.post("/generate")
def generate_report():
    return {"status": "scheduled"}
