from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers import patients


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="MIRA Health Intelligence Predictor",
    version="0.1.0"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include Patient Routes
app.include_router(
    patients.router,
    prefix="/patients",
    tags=["Patients"]
)


# Root Endpoint
@app.get("/")
def root():
    return {
        "status": "running"
    }