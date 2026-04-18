import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Intelligence",
    layout="wide",
    page_icon="📊"
)

# -------------------------------
# LOAD MODEL
# -------------------------------
@st.cache_resource
def load_model():
    return joblib.load("models/churn_pipeline.pkl")

model = load_model()

# -------------------------------
# HEADER
# -------------------------------
st.title("📊 Customer Churn Risk Intelligence")
st.markdown("### Predict churn probability and understand customer risk")

st.divider()

# -------------------------------
# LAYOUT
# -------------------------------
col1, col2 = st.columns([2, 1])

# -------------------------------
# INPUT SECTION
# -------------------------------
with col1:
    st.subheader("🧾 Customer Profile")

    c1, c2, c3 = st.columns(3)

    with c1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Partner", ["Yes", "No"])

    with c2:
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (months)", 0, 72, 12)
        monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

    with c3:
        total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("🚀 Predict Churn", use_container_width=True):

    try:
        input_data = pd.DataFrame([{
            "gender": gender,
            "SeniorCitizen": senior,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "MonthlyCharges": monthly,
            "TotalCharges": total,
            "Contract": contract,
            "PaymentMethod": payment
        }])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        # -------------------------------
        # OUTPUT PANEL
        # -------------------------------
        with col2:
            st.subheader("📊 Prediction Result")

            st.metric(
                label="Churn Probability",
                value=f"{probability:.2%}"
            )

            # Risk Level
            if probability > 0.7:
                st.error("🔴 High Risk")
            elif probability > 0.4:
                st.warning("🟠 Medium Risk")
            else:
                st.success("🟢 Low Risk")

            # Progress bar
            st.progress(float(probability))

            st.markdown("### 📈 Insights")

            insights = []

            if tenure < 12:
                insights.append("Low tenure → higher churn risk")
            if contract == "Month-to-month":
                insights.append("Month-to-month contract increases churn")
            if monthly > 80:
                insights.append("High monthly charges detected")
            if partner == "No":
                insights.append("Customers without partners churn more")

            if insights:
                for i in insights:
                    st.write(f"• {i}")
            else:
                st.write("Stable customer profile")

    except Exception as e:
        st.error(f"Error during prediction: {e}")

# -------------------------------
# FOOTER
# -------------------------------
st.divider()
