from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/api/v1/meters", tags=["meters"])

@router.get("/", response_model=List[schemas.MeterRead])
def list_meters(db: Session = Depends(get_db)):
    meters = db.query(models.Meter).all()
    return meters

@router.post("/", response_model=schemas.MeterRead)
def create_meter(m: schemas.MeterCreate, db: Session = Depends(get_db)):
    meter = models.Meter(serial=m.serial, address=m.address, lat=m.lat, lon=m.lon)
    db.add(meter)
    db.commit()
    db.refresh(meter)
    return meter
