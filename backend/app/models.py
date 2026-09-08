from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Meter(Base):
    __tablename__ = "meters"
    id = Column(Integer, primary_key=True, index=True)
    serial = Column(String, unique=True, index=True)
    address = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    status = Column(String)
    installed_at = Column(DateTime)

    readings = relationship("Reading", back_populates="meter")

class Reading(Base):
    __tablename__ = "readings"
    id = Column(Integer, primary_key=True, index=True)
    meter_id = Column(Integer, ForeignKey("meters.id"))
    timestamp = Column(DateTime)
    volume = Column(Float)
    cumulative_volume = Column(Float)

    meter = relationship("Meter", back_populates="readings")
