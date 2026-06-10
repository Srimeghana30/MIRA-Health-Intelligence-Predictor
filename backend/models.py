from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import Text
from sqlalchemy import DateTime
from datetime import datetime

from database import Base

class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    dob = Column(Date)

    email = Column(String, unique=True)

    glucose = Column(Float)

    haemoglobin = Column(Float)

    cholesterol = Column(Float)
    
    risk_level = Column(String)

    health_score = Column(Integer)

    remarks = Column(Text)
    
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    