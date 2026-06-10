from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import func

import crud
import schemas

from models import Patient
from dependencies import get_db


router = APIRouter()


@router.post(
    "/",
    response_model=schemas.PatientResponse
)
def create_patient(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new patient.
    """

    existing = (
        db.query(Patient)
        .filter(
            Patient.email == patient.email
        )
        .first()
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Patient with this email already exists."
        )

    return crud.create_patient(
        db,
        patient
    )


@router.get(
    "/",
    response_model=list[schemas.PatientResponse]
)
def get_patients(
    db: Session = Depends(get_db)
):
    """
    Retrieve all patients.
    """

    return crud.get_patients(db)


# IMPORTANT:
# Place analytics BEFORE /{patient_id}
@router.get("/analytics")
def analytics(
    db: Session = Depends(get_db)
):
    """
    Get dashboard analytics.
    """

    total = db.query(Patient).count()

    high = (
        db.query(Patient)
        .filter(
            Patient.risk_level == "High Risk"
        )
        .count()
    )

    moderate = (
        db.query(Patient)
        .filter(
            Patient.risk_level == "Moderate Risk"
        )
        .count()
    )

    low = (
        db.query(Patient)
        .filter(
            Patient.risk_level == "Low Risk"
        )
        .count()
    )

    avg_glucose = (
        db.query(
            func.avg(Patient.glucose)
        )
        .scalar()
    )

    avg_cholesterol = (
        db.query(
            func.avg(Patient.cholesterol)
        )
        .scalar()
    )

    avg_score = (
        db.query(
            func.avg(Patient.health_score)
        )
        .scalar()
    )

    return {
        "total_patients": total,

        "high_risk": high,

        "moderate_risk": moderate,

        "low_risk": low,

        "average_glucose": (
            round(avg_glucose, 2)
            if avg_glucose
            else 0
        ),

        "average_cholesterol": (
            round(avg_cholesterol, 2)
            if avg_cholesterol
            else 0
        ),

        "average_health_score": (
            round(avg_score, 2)
            if avg_score
            else 0
        )
    }


@router.get(
    "/{patient_id}",
    response_model=schemas.PatientResponse
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a patient by ID.
    """

    patient = crud.get_patient(
        db,
        patient_id
    )

    if patient is None:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@router.put(
    "/{patient_id}",
    response_model=schemas.PatientResponse
)
def update_patient(
    patient_id: int,
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db)
):
    """
    Update a patient.
    """

    updated = crud.update_patient(
        db,
        patient_id,
        patient
    )

    if updated is None:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return updated


@router.delete(
    "/{patient_id}"
)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a patient.
    """

    deleted = crud.delete_patient(
        db,
        patient_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {
        "message": "Patient deleted successfully"
    }