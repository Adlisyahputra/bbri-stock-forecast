from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(__file__))
from features import build_features, FEATURE_COLS

app = FastAPI(title="BBRI Stock Price Forecast API", version="1.0")

model_path = os.path.join(os.path.dirname(__file__), "..", "models", "bbri_price_model.joblib")
model = joblib.load(model_path)

class PriceInput(BaseModel):
    recent_closes: list[float]

class PredictionOutput(BaseModel):
    predicted_next_close: float

@app.get("/")
def root():
    return {"message": "BBRI Stock Forecast API aktif. Kirim POST ke /predict"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PriceInput):
    features = build_features(input_data.recent_closes)
    X = pd.DataFrame([features])[FEATURE_COLS]
    prediction = model.predict(X)[0]

    return PredictionOutput(predicted_next_close=round(float(prediction), 2))