from fastapi import APIRouter
from schemas.vehicle_schema import VehicleLog
from services.vehicle_service import save_vehicle, get_all_vehicles, get_vehicles_today
from analytics.report_service import get_daily_analytics, get_hourly_analytics, get_vehicle_type_analytics

router = APIRouter()


@router.post("/vehicle/log")
def log_vehicle(vehicle: VehicleLog):
    save_vehicle(vehicle)
    return {"status": "vehicle logged"}


@router.get("/vehicles")
def get_vehicles():
    vehicles = get_all_vehicles()
    return {"vehicles": [v.__dict__ for v in vehicles]}


@router.get("/vehicles/today")
def vehicles_today():
    vehicles = get_vehicles_today()
    return {"vehicles_today": [v.__dict__ for v in vehicles]}


@router.get("/analytics/traffic")
def traffic_overview():
    vehicles = get_all_vehicles()
    return {"total_vehicles": len(vehicles)}


@router.get("/analytics/daily")
def daily_analytics():
    return get_daily_analytics()


@router.get("/analytics/hourly")
def hourly_analytics():
    return get_hourly_analytics()


@router.get("/analytics/vehicle-types")
def vehicle_type_analytics():
    return get_vehicle_type_analytics()
