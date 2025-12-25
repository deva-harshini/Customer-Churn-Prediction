from fastapi import FastAPI
import pandas as pd

from app.schemas import CustomerData
from app.model_loader import load_model

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts customer churn probability",
    version="1.0"
)

model = load_model()

@app.get("/")
def health_check():
    return {"status": "API running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    input_df = pd.DataFrame([data.dict()])
    
    churn_prob = model.predict_proba(input_df)[0][1]
    churn_label = int(churn_prob >= 0.4)  # business threshold
    
    return {
        "churn_probability": round(churn_prob, 3),
        "churn_prediction": churn_label
    }
