# 📌 Customer Churn Risk Intelligence System

An end-to-end, production-ready Data Science and Machine Learning system that predicts customer churn risk and explains the “why” behind every prediction using Explainable AI (SHAP).

This project goes beyond a basic churn prediction notebook and demonstrates how real-world churn analytics systems are designed, evaluated, and deployed for decision support.


# 🚀 Why This Project Matters

Customer churn is one of the most critical business challenges for subscription-based companies.  
This system helps businesses:

- Predict customers likely to churn
- Understand factors driving churn behavior
- Support data-driven retention strategies
- Generate explainable and auditable predictions
- Deliver analytics through APIs and dashboards

This is not just a machine learning model — it is a complete churn intelligence system.


# 🧠 What This System Does

✔ Predicts customer churn probability  
✔ Performs data cleaning and feature engineering  
✔ Evaluates classification model performance  
✔ Explains predictions using SHAP (Explainable AI)  
✔ Exposes predictions via FastAPI APIs  
✔ Visualizes churn insights using Streamlit dashboards  
✔ Follows production-ready ML pipeline practices  


# 🏗️ System Architecture

```text
Customer Data
      │
      ▼
Data Preprocessing Pipeline
      │
      ├── Data Cleaning
      ├── Feature Engineering
      ├── Feature Scaling
      └── Validation
      │
      ▼
Machine Learning Pipeline
      │
      ├── Model Training
      ├── Model Evaluation
      ├── Churn Prediction
      └── SHAP Explainability
      │
      ▼
FastAPI Backend
      │
      ▼
Streamlit Dashboard
```
# 📂 Project Structure

```text
customer-churn-risk-intelligence/
│
├── app/                        # FastAPI backend
│   ├── main.py
│   ├── model_loader.py
│   └── schemas.py
│
├── ui/                         # Streamlit frontend
│   └── app.py
│
├── notebooks/                  # Development notebooks
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_explainability.ipynb
│
├── models/                     # Saved ML pipeline
│   └── churn_pipeline.pkl
│
├── src/                        # Utility modules
│   ├── data_validation.py
│   └── preprocessing_utils.py
│
├── reports/                    # Analysis summaries
│   └── churn_insights.md
│
├── data/                       # Local-only data
│   ├── raw/
│   ├── processed/
│   └── evaluation/
│
├── requirements.txt
├── README.md
└── .gitignore
```
# 📊 Data Science Workflow

## 1️⃣ Exploratory Data Analysis (EDA)

- Customer behavior analysis
- Contract and tenure trends
- Service usage exploration
- Churn distribution analysis


## 2️⃣ Data Cleaning & Feature Engineering

- Missing value handling
- Categorical encoding
- Feature scaling
- Data validation checks
- Pipeline-based preprocessing


## 3️⃣ Model Development

Implemented and compared multiple classification models:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

Best model selected based on evaluation metrics and generalization performance.


## 4️⃣ Model Evaluation

Evaluated models using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Performed threshold optimization to improve churn detection performance.


## 5️⃣ Explainable AI (SHAP)

Integrated SHAP to generate:

- Global feature importance
- Customer-level churn explanations
- Transparent prediction reasoning

Key churn drivers identified:

- Contract type
- Tenure
- Monthly charges
- Support services


## 6️⃣ Deployment & Visualization

- FastAPI backend for prediction APIs
- Streamlit dashboard for interactive analytics
- Real-time prediction and explanation support


# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/customer-churn-risk-intelligence.git
cd customer-churn-risk-intelligence
```
## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```


## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```


# 🚀 Running the Project

## 🔹 Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```


## 🔹 Start Streamlit Dashboard

Open a new terminal:

```bash
streamlit run ui/app.py
```

# 📊 Dashboard Features

- Churn probability visualization
- Feature importance insights
- SHAP explanation charts
- Customer risk segmentation
- Interactive prediction interface

# 🧠 Skills Demonstrated

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Machine Learning Pipelines
- Model Evaluation & Optimization
- Explainable AI (SHAP)
- FastAPI Development
- Streamlit Dashboarding
- Data Validation & Reproducibility
- Git & Version Control

---

# 🔒 Best Practices Implemented

✔ Pipeline-based preprocessing  
✔ Prevention of data leakage  
✔ Explainable predictions  
✔ Reproducible workflows  
✔ Modular project structure  
✔ Production-ready deployment architecture  

---

# 📌 Future Improvements

- Real-time streaming predictions
- Automated retraining pipelines
- Cloud deployment
- Drift detection and monitoring
- Advanced ensemble modeling

---

# 👩‍💻 Author

**Mandali Deva Harshini**
