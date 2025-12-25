import joblib
import os

MODEL_PATH = os.path.join("models", "churn_rf_pipeline.pkl")

def load_model():
    return joblib.load(MODEL_PATH)
