import joblib
import os

MODEL_PATH = "models/churn_pipeline.pkl"
def load_model():
    return joblib.load(MODEL_PATH)
