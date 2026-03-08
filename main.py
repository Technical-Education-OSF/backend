from fastapi import FastAPI
from api.vehicle_routes import router

app = FastAPI(title="Vehicle Logger API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Vehicle Logger API running"}