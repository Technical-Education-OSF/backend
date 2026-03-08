from models.vehicle_model import VehicleLog
from database.db import SessionLocal
from sqlalchemy import func
from datetime import datetime, timezone


def get_daily_analytics():
    db = SessionLocal()
    try:
        total = db.query(VehicleLog).count()
        by_type = (
            db.query(VehicleLog.vehicle_type, func.count(VehicleLog.id))
            .group_by(VehicleLog.vehicle_type)
            .all()
        )
        return {
            "total_vehicles": total,
            "by_type": {vtype: count for vtype, count in by_type}
        }
    finally:
        db.close()


def get_hourly_analytics():
    db = SessionLocal()
    try:
        by_hour = (
            db.query(func.extract("hour", VehicleLog.timestamp), func.count(VehicleLog.id))
            .group_by(func.extract("hour", VehicleLog.timestamp))
            .order_by(func.extract("hour", VehicleLog.timestamp))
            .all()
        )
        return {"by_hour": {int(hour): count for hour, count in by_hour}}
    finally:
        db.close()


def get_vehicle_type_analytics():
    db = SessionLocal()
    try:
        by_type = (
            db.query(VehicleLog.vehicle_type, func.count(VehicleLog.id))
            .group_by(VehicleLog.vehicle_type)
            .all()
        )
        return {"vehicle_types": {vtype: count for vtype, count in by_type}}
    finally:
        db.close()
