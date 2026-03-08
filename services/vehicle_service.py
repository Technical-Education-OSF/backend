from models.vehicle_model import VehicleLog
from database.db import SessionLocal
from datetime import datetime, timezone


def save_vehicle(data):
    db = SessionLocal()
    vehicle = VehicleLog(
        plate_number=data.plate_number,
        vehicle_type=data.vehicle_type,
        location=data.location,
        timestamp=data.timestamp
    )
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    db.close()
    return vehicle


def get_all_vehicles():
    db = SessionLocal()
    try:
        return db.query(VehicleLog).all()
    finally:
        db.close()


def get_vehicles_today():
    db = SessionLocal()
    try:
        today = datetime.now(timezone.utc).date()
        return db.query(VehicleLog).filter(
            VehicleLog.timestamp >= datetime(today.year, today.month, today.day)
        ).all()
    finally:
        db.close()
