from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import field_validator

from datetime import date


class PatientCreate(BaseModel):

    full_name: str
    dob: date
    email: EmailStr

    glucose: float
    haemoglobin: float
    cholesterol: float

    @field_validator("dob")
    def validate_dob(cls, value):

        if value > date.today():
            raise ValueError(
                "Date of Birth cannot be future date"
            )

        return value

    @field_validator(
        "glucose",
        "haemoglobin",
        "cholesterol"
    )
    def validate_numbers(
        cls,
        value
    ):

        if value <= 0:
            raise ValueError(
                "Value must be greater than zero"
            )

        return value


class PatientResponse(PatientCreate):

    id: int
    health_score: int
    risk_level: str
    remarks: str

    class Config:
        from_attributes = True