from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MeterBase(BaseModel):
    serial: str
    address: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None

class MeterCreate(MeterBase):
    pass

class MeterRead(MeterBase):
    id: int
    status: Optional[str] = None
    installed_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ReadingBase(BaseModel):
    meter_id: int
    timestamp: datetime
    volume: float
    cumulative_volume: float

class ReadingCreate(ReadingBase):
    pass

class ReadingRead(ReadingBase):
    id: int

    class Config:
        orm_mode = True
