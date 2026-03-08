from pydantic import BaseModel
from datetime import datetime


class VehicleLog(BaseModel):
    plate_number: str
    vehicle_type: str
    location: str
    timestamp: datetime
