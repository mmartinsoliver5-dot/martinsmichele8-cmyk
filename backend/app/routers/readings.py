from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/api/v1/readings", tags=["readings"])

@router.post("/ingest", response_model=schemas.ReadingRead)
def ingest_reading(r: schemas.ReadingCreate, db: Session = Depends(get_db)):
    reading = models.Reading(meter_id=r.meter_id, timestamp=r.timestamp, volume=r.volume, cumulative_volume=r.cumulative_volume)
    db.add(reading)
    db.commit()
    db.refresh(reading)
    return reading

@router.get("/", response_model=list[schemas.ReadingRead])
def list_readings(meter_id: int, db: Session = Depends(get_db)):
    q = db.query(models.Reading)
    if meter_id:
        q = q.filter(models.Reading.meter_id == meter_id)
    return q.order_by(models.Reading.timestamp.desc()).limit(100).all()
