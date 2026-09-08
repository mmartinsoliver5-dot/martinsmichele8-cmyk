from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/v1/photos", tags=["photos"])

@router.post("/upload")
async def upload_photo(meter_serial: str = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Placeholder: save file to storage (S3/MinIO) and record metadata in DB
    return {"meter_serial": meter_serial, "filename": file.filename}
