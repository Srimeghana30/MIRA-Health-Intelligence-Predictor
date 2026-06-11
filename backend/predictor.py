import joblib

model = joblib.load(
    "risk_model.pkl"
)

encoder = joblib.load(
    "label_encoder.pkl"
)


def predict_health(
    glucose,
    haemoglobin,
    cholesterol
):

    prediction = model.predict(
        [[
            glucose,
            haemoglobin,
            cholesterol
        ]]
    )[0]

    risk = encoder.inverse_transform(
        [prediction]
    )[0]

    remarks = {
        "Low Risk":
            "Overall biomarkers are within acceptable ranges.",
        "Moderate Risk":
            "Clinical monitoring and lifestyle modifications are advised.",
        "High Risk":
            "Immediate clinical evaluation is recommended."
    }

    score_map = {
        "Low Risk": 25,
        "Moderate Risk": 60,
        "High Risk": 90
    }

    return {
        "risk": risk,
        "score": score_map[risk],
        "remarks": remarks[risk]
    }