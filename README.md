# MIRA Health Intelligence Predictor

An AI-powered healthcare risk prediction platform designed to assist healthcare professionals in identifying patient risk levels using clinical biomarkers and machine learning techniques.

---

## Project Overview

MIRA (Medical Intelligence Robotic Automation) is a full-stack healthcare application that combines modern backend technologies with machine learning to provide real-time health risk assessments.

The platform enables healthcare professionals to:

- Manage patient records efficiently.
- Predict patient risk levels using AI/ML techniques.
- Monitor healthcare trends through interactive dashboards.
- Export patient data for reporting and analysis.

---

## Features

### Patient Management
- Add new patients.
- View all patient records.
- Search patient information.
- Update existing patient details.
- Delete patient records.

### Healthcare Analytics Dashboard
- Total patient count.
- High-risk patient count.
- Moderate-risk patient count.
- Low-risk patient count.
- Average health score monitoring.

### Machine Learning Integration
- Logistic Regression model built using Scikit-learn.
- Real-time prediction during patient creation and updates.
- Automatic classification into:
  - Low Risk
  - Moderate Risk
  - High Risk

### Additional Functionalities
- CSV export of patient records.
- Swagger API documentation.
- Responsive frontend interface.

---

## Technology Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

### Frontend
- React
- Vite
- Bootstrap
- Axios
- React CSV

### Machine Learning
- Scikit-learn
- Pandas
- Joblib

---

## Machine Learning Workflow

Healthcare Data

↓

Feature Selection

- Glucose
- Haemoglobin
- Cholesterol

↓

Logistic Regression Training

↓

Model Serialization (Joblib)

↓

FastAPI Integration

↓

Real-Time Risk Prediction

↓

Dashboard Visualization

---

## Model Performance

The Logistic Regression model was evaluated using a proof-of-concept healthcare dataset.

### Evaluation Metrics

| Metric | Score |
|---------|--------|
| Accuracy | 100% |
| Precision | 100% |
| Recall | 100% |
| F1-Score | 100% |

### Confusion Matrix

| Actual / Predicted | High Risk | Low Risk | Moderate Risk |
|--------------------|------------|-----------|---------------|
| High Risk          | 11         | 0         | 0             |
| Low Risk           | 0          | 6         | 0             |
| Moderate Risk      | 0          | 0         | 8             |

> Note: The evaluation was conducted on a small proof-of-concept dataset to demonstrate end-to-end AI/ML integration. Future improvements include validation using larger real-world healthcare datasets.

---

## Project Structure

```text
MIRA Health Prediction/
│
├── backend/
│   ├── data/
│   │   └── healthcare_dataset.csv
│   ├── routers/
│   ├── models/
│   │   ├── risk_model.pkl
│   │   └── label_encoder.pkl
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── evaluate_model.py
│   ├── main.py
│   ├── predictor.py
│   ├── schemas.py
│   └── train_model.py
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation Guide

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```
http://localhost:5173
```

---

## Future Enhancements

- Integration with larger healthcare datasets.
- Cross-validation and advanced model evaluation techniques.
- Implementation of additional machine learning algorithms.
- Role-based authentication and authorization.
- Deployment using Docker and cloud platforms.

---

## Author

Meghana Supriya

AI/ML-Integrated Healthcare Risk Prediction Platform developed as part of a healthcare software engineering assessment.