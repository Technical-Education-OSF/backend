from sqlalchemy import Column, Integer, String, DateTime
from database.base import Base


class VehicleLog(Base):
    __tablename__ = "vehicle_logs"

    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String)
    vehicle_type = Column(String)
    location = Column(String)
    timestamp = Column(DateTime)
