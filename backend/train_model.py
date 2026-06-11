import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("data/healthcare_dataset.csv")

# Features
X = data[
    ["glucose", "haemoglobin", "cholesterol"]
]

# Labels
y = data["risk"]

# Encode labels
encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

# Train model
model = LogisticRegression(
    max_iter=1000
)

model.fit(X, y_encoded)

# Save model and encoder
joblib.dump(model, "risk_model.pkl")

joblib.dump(encoder, "label_encoder.pkl")

print("Model trained successfully!")