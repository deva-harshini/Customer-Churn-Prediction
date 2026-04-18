import streamlit as st
import pandas as pd
import joblib
import os

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="📊",
    layout="wide"
)

# ===============================
# LOAD MODEL
# ===============================
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/churn_pipeline.pkl")
model = joblib.load(MODEL_PATH)

# ===============================
# STYLING
# ===============================
st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: 700;
}
.subtitle {
    font-size: 18px;
    color: #9aa0a6;
}
.result-box {
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# HEADER
# ===============================
st.markdown('<div class="main-title">📊 Customer Churn Risk Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict churn probability and understand customer risk</div>', unsafe_allow_html=True)

st.markdown("---")

# ===============================
# INPUT FORM
# ===============================
st.subheader("📄 Customer Profile")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])

with col2:
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

with col3:
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer", "Credit card"
    ])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

st.markdown("---")

# ===============================
# PREDICTION BUTTON
# ===============================
if st.button("🚀 Predict Churn", use_container_width=True):

    try:
        # ===============================
        # INPUT DATA (MATCH TRAINING FEATURES)
        # ===============================
        input_data = pd.DataFrame([{
            "gender": gender,
            "SeniorCitizen": senior,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": "Yes",
            "MultipleLines": multiple_lines,
            "InternetService": internet_service,
            "OnlineSecurity": "No",
            "OnlineBackup": "No",
            "DeviceProtection": "No",
            "TechSupport": "No",
            "StreamingTV": "No",
            "StreamingMovies": "No",
            "Contract": contract,
            "PaperlessBilling": "Yes",
            "PaymentMethod": payment,
            "MonthlyCharges": monthly,
            "TotalCharges": total
        }])

        # ===============================
        # PREDICT
        # ===============================
        prob = model.predict_proba(input_data)[0][1]
        pred = int(prob > 0.5)

        # ===============================
        # DISPLAY RESULT
        # ===============================
        st.markdown("### 📊 Prediction Result")

        colA, colB = st.columns(2)

        with colA:
            st.metric("Churn Probability", f"{prob:.2%}")

        with colB:
            if pred == 1:
                st.error("⚠️ High Risk of Churn")
            else:
                st.success("✅ Low Risk of Churn")

        # ===============================
        # BUSINESS INSIGHT
        # ===============================
        st.markdown("### 💡 Insight")

        if prob > 0.7:
            st.warning("Customer is highly likely to churn. Consider offering discounts or proactive support.")
        elif prob > 0.4:
            st.info("Customer shows moderate churn risk. Monitor engagement.")
        else:
            st.success("Customer is stable. Maintain current service quality.")

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")