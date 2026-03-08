# 🚗 Vehicle Logger API

A lightweight REST API for logging and analyzing vehicle traffic data. Built with **FastAPI** and **PostgreSQL**, it records vehicle sightings (plate number, type, location, and timestamp) and exposes analytics endpoints for traffic reporting.

---

## ✨ Features

- **Vehicle Logging** – Record vehicle plate numbers, types, locations, and timestamps.
- **Daily & Today's Vehicles** – Retrieve all logged vehicles or filter by today's date.
- **Traffic Analytics** – Get total vehicle count, daily summaries, hourly breakdowns, and statistics by vehicle type.
- **Interactive API Docs** – Automatic Swagger UI and ReDoc documentation via FastAPI.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12+ |
| Framework | FastAPI |
| ASGI Server | Uvicorn |
| ORM | SQLAlchemy 2.x |
| Database | PostgreSQL |
| DB Driver | psycopg2-binary |
| Package Manager | [uv](https://github.com/astral-sh/uv) |

---

## 📁 Project Structure

```
backend/
├── main.py                  # Application entry point
├── pyproject.toml           # Project metadata & dependencies
├── uv.lock                  # Locked dependency versions
├── .python-version          # Python version pin (3.12)
│
├── api/
│   └── vehicle_routes.py    # All API route definitions
│
├── models/
│   └── vehicle_model.py     # SQLAlchemy ORM model (VehicleLog)
│
├── schemas/
│   └── vehicle_schema.py    # Pydantic request/response schemas
│
├── services/
│   └── vehicle_service.py   # CRUD business logic
│
├── analytics/
│   └── report_service.py    # Traffic analytics & reporting
│
└── database/
    ├── base.py              # SQLAlchemy declarative base
    └── db.py                # Database engine & session factory
```

---

## ⚙️ Prerequisites

- **Python 3.12+**
- **PostgreSQL** (running locally or via a connection string)
- **uv** package manager — [install here](https://docs.astral.sh/uv/getting-started/installation/)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Technical-Education-OSF/backend.git
cd backend
```

### 2. Install dependencies

```bash
uv sync
```

> Alternatively, install with pip:
> ```bash
> pip install fastapi uvicorn sqlalchemy psycopg2-binary
> ```

### 3. Configure the database

Open `database/db.py` and update the `DATABASE_URL` with your PostgreSQL credentials:

```python
DATABASE_URL = "postgresql://<user>:<password>@<host>/<database>"
```

For example:

```python
DATABASE_URL = "postgresql://postgres:secret@localhost/vehicle_logger"
```

> **Tip:** For production use, store the connection string in an environment variable and load it with `os.getenv("DATABASE_URL")`.

### 4. Create the database tables

The application uses SQLAlchemy models. Run a one-time setup to create the tables:

```python
# From a Python shell or a migration script
from database.base import Base
from database.db import engine
Base.metadata.create_all(bind=engine)
```

### 5. Start the server

```bash
uvicorn main:app --reload
```

The API will be available at **http://localhost:8000**.

---

## 📖 API Reference

Once running, visit the interactive docs:

- **Swagger UI** → [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc** → [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints

#### Health Check

```
GET /
```

**Response:**
```json
{ "message": "Vehicle Logger API running" }
```

---

#### Log a Vehicle

```
POST /vehicle/log
```

**Request Body:**
```json
{
  "plate_number": "ABC-1234",
  "vehicle_type": "bus",
  "location": "Main Street",
  "timestamp": "2024-06-01T08:30:00"
}
```

**Response:**
```json
{ "status": "vehicle logged" }
```

---

#### Get All Vehicles

```
GET /vehicles
```

**Response:**
```json
{
  "vehicles": [
    {
      "id": 1,
      "plate_number": "ABC-1234",
      "vehicle_type": "bus",
      "location": "Main Street",
      "timestamp": "2024-06-01T08:30:00"
    }
  ]
}
```

---

#### Get Vehicles Logged Today

```
GET /vehicles/today
```

**Response:**
```json
{
  "vehicles_today": [ /* same shape as /vehicles */ ]
}
```

---

#### Traffic Overview

```
GET /analytics/traffic
```

**Response:**
```json
{ "total_vehicles": 42 }
```

---

#### Daily Analytics

```
GET /analytics/daily
```

Returns total vehicle counts grouped by vehicle type.

---

#### Hourly Analytics

```
GET /analytics/hourly
```

Returns vehicle counts broken down by hour of the day.

---

#### Vehicle-Type Analytics

```
GET /analytics/vehicle-types
```

Returns counts for each distinct vehicle type recorded.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request against `main`.

Please keep commits small and focused, and ensure your code is consistent with the existing project style.

---

## 📄 License

This project is open-source. A license file has not yet been added — please check with the maintainers before using or redistributing the code.
