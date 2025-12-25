import streamlit as st
import requests

# -------------------------------
# App Configuration
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Risk Intelligence",
    page_icon="📉",
    layout="centered"
)

st.title("📉 Customer Churn Risk Intelligence")
st.write("Predict the likelihood of a customer churning using ML")

API_URL = "http://127.0.0.1:8000/predict"

# -------------------------------
# Input Form
# -------------------------------
with st.form("churn_form"):
    st.subheader("Customer Details")

    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, value=12)

    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )

    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0, value=1000.0)

    submitted = st.form_submit_button("Predict Churn Risk")

# -------------------------------
# Prediction Logic
# -------------------------------
if submitted:
    payload = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            # ✅ FIXED KEYS (THIS WAS THE BUG)
            churn_prediction = result["churn_prediction"]
            churn_probability = result["churn_probability"]

            st.subheader("Prediction Result")

            if churn_prediction == 1:
                st.error(f"⚠️ High Churn Risk\n\nProbability: **{churn_probability:.2%}**")
            else:
                st.success(f"✅ Low Churn Risk\n\nProbability: **{churn_probability:.2%}**")

        else:
            st.error(f"API Error: {response.status_code}")
            st.json(response.json())

    except Exception as e:
        st.error("❌ Could not connect to FastAPI backend")
        st.exception(e)
