def predict_health(
    glucose,
    haemoglobin,
    cholesterol
):

    score = 0

    reasons = []

    if glucose > 180:
        score += 40
        reasons.append("elevated glucose")

    elif glucose > 140:
        score += 20
        reasons.append("borderline glucose")

    if cholesterol > 240:
        score += 30
        reasons.append("high cholesterol")

    elif cholesterol > 200:
        score += 15
        reasons.append("borderline cholesterol")

    if haemoglobin < 10:
        score += 30
        reasons.append("low haemoglobin")

    elif haemoglobin < 12:
        score += 15
        reasons.append("mild anaemia indicators")

    if score >= 70:

        risk = "High Risk"

        remarks = (
            "Patient exhibits "
            + ", ".join(reasons)
            + ". Immediate clinical evaluation is recommended."
        )

    elif score >= 40:

        risk = "Moderate Risk"

        remarks = (
            "Patient demonstrates "
            + ", ".join(reasons)
            + ". Lifestyle modifications and regular monitoring are advised."
        )

    else:

        risk = "Low Risk"

        remarks = (
            "Patient blood markers are within acceptable ranges."
        )

    return {

        "score": score,

        "risk": risk,

        "remarks": remarks

    }