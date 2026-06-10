from sqlalchemy.orm import Session

from models import Patient
from predictor import predict_health


def create_patient(
    db: Session,
    patient
):
    """
    Create a new patient record.
    """

    prediction = predict_health(
        patient.glucose,
        patient.haemoglobin,
        patient.cholesterol
    )

    db_patient = Patient(
        full_name=patient.full_name,
        dob=patient.dob,
        email=patient.email,
        glucose=patient.glucose,
        haemoglobin=patient.haemoglobin,
        cholesterol=patient.cholesterol,
        health_score=prediction["score"],
        risk_level=prediction["risk"],
        remarks=prediction["remarks"]
    )

    db.add(db_patient)

    db.commit()

    db.refresh(db_patient)

    return db_patient


def get_patients(
    db: Session
):
    """
    Retrieve all patients.
    """

    return db.query(Patient).all()


def get_patient(
    db: Session,
    patient_id: int
):
    """
    Retrieve a patient by ID.
    """

    return (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )


def update_patient(
    db: Session,
    patient_id: int,
    patient_data
):
    """
    Update an existing patient.
    """

    patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if patient is None:
        return None

    patient.full_name = patient_data.full_name

    patient.dob = patient_data.dob

    patient.email = patient_data.email

    patient.glucose = patient_data.glucose

    patient.haemoglobin = patient_data.haemoglobin

    patient.cholesterol = patient_data.cholesterol

    prediction = predict_health(
        patient.glucose,
        patient.haemoglobin,
        patient.cholesterol
    )

    patient.health_score = prediction["score"]

    patient.risk_level = prediction["risk"]

    patient.remarks = prediction["remarks"]

    db.commit()

    db.refresh(patient)

    return patient


def delete_patient(
    db: Session,
    patient_id: int
):
    """
    Delete a patient record.
    """

    patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if patient is None:
        return False

    db.delete(patient)

    db.commit()

    return True