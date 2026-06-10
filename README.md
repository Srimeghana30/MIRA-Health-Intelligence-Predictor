# MIRA Health Intelligence Predictor

## Overview

MIRA (Medical Intelligence Robotic Automation) is an AI-powered healthcare intelligence platform designed to assist healthcare professionals in assessing patient health risks based on clinical indicators. The application enables patient record management while generating automated risk predictions and health insights.

## Features

### Patient Management

* Add new patient records
* View all patient records
* Update existing patient information
* Delete patient records
* Search patients by name

### Health Intelligence

* Automated health score calculation
* Risk categorization:

  * Low Risk
  * Moderate Risk
  * High Risk
* Clinical remarks generation

### Analytics Dashboard

* Total patient count
* Risk distribution statistics
* Average health score monitoring
* Interactive dashboard cards

### Reporting

* Export patient records to CSV format

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

### Frontend

* React.js
* Vite
* Bootstrap
* Axios
* React CSV

## Project Structure

MIRA-Health-Intelligence-Predictor/
├── backend/
├── frontend/
├── README.md
├── requirements.txt
└── .gitignore

## Installation

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

## Future Enhancements

* Authentication and authorization
* PDF report generation
* Advanced predictive models
* Email notifications
* Deployment using Docker and Cloud platforms

## Author

Meghana Supriya
