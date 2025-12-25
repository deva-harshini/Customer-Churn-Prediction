# 📌 Customer Churn Risk Intelligence System

> **An end-to-end, production-ready Machine Learning system that predicts customer churn and explains the “why” behind every prediction using Explainable AI (SHAP).**

---

## 🚀 Why This Project Matters

Customer churn is one of the biggest challenges for subscription-based businesses.  
This project goes beyond a simple ML model and delivers a **complete decision-support system** that:

- Predicts **churn probability**
- Explains **key drivers of churn**
- Enables **actionable retention strategies**
- Is **deployable, reproducible, and explainable**

This is **not just a notebook project** — it is a **full ML system**.

---

## 🧠 What This System Does

✔ Predicts whether a customer is likely to churn  
✔ Provides churn **probability scores**  
✔ Explains predictions using **SHAP (Explainable AI)**  
✔ Exposes predictions via **FastAPI**  
✔ Allows interaction via **Streamlit UI**  
✔ Follows industry-grade ML lifecycle and deployment practices  

---

## 🏗️ System Architecture

User

│
▼

Streamlit Web UI

│
▼

FastAPI Backend

│
▼

ML Pipeline
(Preprocessing + Model)

│
▼

Prediction + Explanation


---

## 📂 Project Structure

```text
customer-churn-risk-intelligence/
│
├── app/                    # FastAPI backend
│   ├── main.py
│   ├── model_loader.py
│   └── schemas.py
│
├── ui/                     # Streamlit frontend
│   └── app.py
│
├── notebooks/              # ML lifecycle notebooks
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling_evaluation.ipynb
│   └── 04_model_explainability.ipynb
│
├── src/                    # Reusable utilities
│   ├── data_audit.py
│   └── eda_utils.py
│
├── reports/                # Insights & analysis
│   └── eda_insights.md
│
├── models/                 # Production model
│   └── churn_pipeline.pkl
│
├── data/                   # Local-only (ignored by git)
│   ├── raw/
│   ├── processed/
│   └── evaluation/
│
├── requirements.txt
├── README.md
└── .gitignore

```
---

## 🔬 Machine Learning Lifecycle

This project follows a **real-world ML workflow**:

1️⃣ **Exploratory Data Analysis (EDA)**  
   - Customer behavior patterns
   - Tenure, contract, service usage analysis

2️⃣ **Data Cleaning & Feature Engineering**  
   - Missing values
   - Categorical encoding
   - Feature scaling

3️⃣ **Model Training**  
   - Pipeline-based preprocessing + modeling
   - Prevents data leakage
   - Reusable in production

4️⃣ **Model Evaluation**  
   - ROC-AUC
   - Precision / Recall
   - Threshold optimization

5️⃣ **Explainability (SHAP)**  
   - Global churn drivers
   - Individual customer explanations

6️⃣ **Deployment & UI**  
   - FastAPI backend
   - Streamlit frontend

---

## ⚙️ Setup Instructions (For New Users)

### 🔹 1. Clone the Repository
Open **Command Prompt (Windows)** or **Terminal (macOS/Linux)** and run:

```bash
git clone https://github.com/<your-username>/customer-churn-risk-intelligence
cd customer-churn-risk-intelligence
```

### 🔹 2. Create & Activate Virtual Environment

Using a virtual environment ensures all dependencies are isolated.

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, you should see:

```bash
(venv)
```

### 🔹 3. Install Dependencies

Install all required libraries using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application
### 🔸 Step 1: Start FastAPI Backend
Run
```bash
uvicorn app.main:app --reload
```
Backend runs at: http://127.0.0.1:8000  

Test it via browser: http://127.0.0.1:8000/docs  

### 🔸 Step 2: Start Streamlit UI (New Terminal)
Run
```bash
streamlit run ui/app.py
```
The UI opens automatically in your browser.

---

## 🧪 Testing the API (Without UI)
You can test the API using Swagger UI:

1. Open: http://127.0.0.1:8000/docs
2. Click POST /predict
3. Use the example input below:
```json
   {
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 85.5,
  "TotalCharges": 1026.0
}
```
**Example Response**

```json
{
  "churn_probability": 0.75,
  "churn_prediction": 1
}
```
--- 

## 📊 Model Explainability (SHAP)

The model is fully explainable:

- Global feature importance
- Customer-level explanations
- Transparent decision-making
- Key churn drivers identified:
- Contract type
- Tenure
- Monthly charges
- Support services
- This enables targeted retention strategies.

---

## 🧪 Reproducibility & Best Practices

- Isolated virtual environment
- Deterministic dependencies (requirements.txt)
- Pipeline-based ML
- No data leakage
- Explainable predictions
- Clean Git history

---

## 🧠 Skills Demonstrated

- Python & Data Science
- Machine Learning Pipelines
- Model Evaluation & Metrics
- Explainable AI (SHAP)
- FastAPI (Backend)
- Streamlit (Frontend)
- Git & Version Control

---

## 👩‍💻 Author

**Mandali Deva Harshini**  

**Email:** mandalidevaharshini@gmail.com  
