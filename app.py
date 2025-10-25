import streamlit as st
import pandas as pd
import joblib

# =============================
# Load Model
# =============================
with open("credit_default_model.pkl", "rb") as f:
    model_data = joblib.load(f)

model = model_data["model"]
features = model_data["features"]

# =============================
# Streamlit Page Setup
# =============================
st.set_page_config(page_title="Credit Default Predictor", layout="centered")
st.title("💳 Credit Card Default Predictor")
st.markdown("Predict if a customer is likely to **default** on their next payment.")

# =============================
# Customer Input Section
# =============================
st.header("👤 Customer Details")

col1, col2 = st.columns(2)

with col1:
    LIMIT_BAL = st.number_input("Credit Limit (₹)", min_value=10000, max_value=1000000, value=200000, step=10000)
    AGE = st.number_input("Age", min_value=18, max_value=100, value=30)
    EDUCATION = st.selectbox("Education Level", [1, 2, 3, 4], help="1=Graduate School, 2=University, 3=High School, 4=Others")
    MARRIAGE = st.selectbox("Marital Status", [1, 2, 3], help="1=Married, 2=Single, 3=Others")

with col2:
    PAY_0 = st.selectbox("Last Payment Status (PAY_0)", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], help="-1=Paid duly, 0=Use of revolving credit, 1+=Delay months")
    BILL_AMT1 = st.number_input("Bill Amount (Last Month ₹)", min_value=0, max_value=1000000, value=50000, step=1000)
    PAY_AMT1 = st.number_input("Payment Amount (Last Month ₹)", min_value=0, max_value=1000000, value=20000, step=1000)
    SEX = st.selectbox("Gender", [1, 2], help="1=Male, 2=Female")

# Prepare input data for prediction
input_data = pd.DataFrame([{
    "LIMIT_BAL": LIMIT_BAL,
    "SEX": SEX,
    "EDUCATION": EDUCATION,
    "MARRIAGE": MARRIAGE,
    "AGE": AGE,
    "PAY_0": PAY_0,
    "BILL_AMT1": BILL_AMT1,
    "PAY_AMT1": PAY_AMT1
}])

# Add missing columns if needed
for col in features:
    if col not in input_data.columns:
        input_data[col] = 0

# =============================
# Prediction Section
# =============================
if st.button("🔍 Predict Default"):
    prob = model.predict_proba(input_data[features])[0, 1]
    prediction = model.predict(input_data[features])[0]

    st.subheader("📈 Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ Likely to Default on Next Payment\n**Probability:** {prob*100:.2f}%")
    else:
        st.success(f"✅ No Default Expected\n**Probability:** {(1 - prob)*100:.2f}%")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ by **Nitish Pathak**")
