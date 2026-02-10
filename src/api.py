from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

from src.feature_engineering import extract_features
from src.config import MODEL_PATH, SCALER_PATH


app = FastAPI(title="Password Strength API")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


class PasswordRequest(BaseModel):
    password: str


@app.post("/predict")
def predict_strength(data: PasswordRequest):
    features = extract_features(data.password).to_frame().T
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]

    return {
        "password": data.password,
        "strength": int(prediction),
        "probabilities": {
            "weak": round(probabilities[0], 3),
            "medium": round(probabilities[1], 3),
            "strong": round(probabilities[2], 3),
        },
    }
