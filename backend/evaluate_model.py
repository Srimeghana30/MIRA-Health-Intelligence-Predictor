import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load dataset
data = pd.read_csv(
    "data/healthcare_dataset.csv"
)

X = data[
    ["glucose", "haemoglobin", "cholesterol"]
]

y_true = data["risk"]

# Load model
model = joblib.load(
    "risk_model.pkl"
)

encoder = joblib.load(
    "label_encoder.pkl"
)

# Predict
predictions = model.predict(X)

y_pred = encoder.inverse_transform(
    predictions
)

print("\nAccuracy:")

print(
    accuracy_score(
        y_true,
        y_pred
    )
)

print("\nClassification Report:")

print(
    classification_report(
        y_true,
        y_pred
    )
)

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_true,
        y_pred
    )
)