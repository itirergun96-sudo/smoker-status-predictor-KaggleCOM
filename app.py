# src/app.py

import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------
# Load model (src-safe)
# -----------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "smoker_model.pkl")
model = joblib.load(MODEL_PATH)

st.title("🚬 Smoker Status Predictor")
st.write("Biyometrik ölçümleri gir → sigara kullanım tahmini al")

# -----------------------
# Input form
# -----------------------

age = st.number_input("Age", 10, 100, 30)
height = st.number_input("Height (cm)", 120, 220, 170)
weight = st.number_input("Weight (kg)", 30, 200, 70)
waist = st.number_input("Waist (cm)", 40.0, 150.0, 80.0)

eye_l = st.number_input("Eyesight Left", 0.0, 3.0, 1.0)
eye_r = st.number_input("Eyesight Right", 0.0, 3.0, 1.0)

hear_l = st.number_input("Hearing Left", 1, 2, 1)
hear_r = st.number_input("Hearing Right", 1, 2, 1)

systolic = st.number_input("Systolic", 80, 200, 120)
relaxation = st.number_input("Diastolic", 40, 150, 80)

fasting = st.number_input("Fasting Blood Sugar", 50, 300, 100)
cholesterol = st.number_input("Cholesterol", 100, 400, 200)
triglyceride = st.number_input("Triglyceride", 30, 500, 150)
hdl = st.number_input("HDL", 10, 150, 50)
ldl = st.number_input("LDL", 30, 300, 100)

hemoglobin = st.number_input("Hemoglobin", 5.0, 25.0, 15.0)
urine = st.number_input("Urine Protein", 1, 6, 1)
creatinine = st.number_input("Serum Creatinine", 0.1, 5.0, 1.0)

ast = st.number_input("AST", 5, 200, 25)
alt = st.number_input("ALT", 5, 200, 25)
gtp = st.number_input("GTP", 5, 500, 30)

dental = st.number_input("Dental Caries", 0, 1, 0)

# -----------------------
# Prediction
# -----------------------

if st.button("Predict Smoking Status"):

    data = pd.DataFrame([{
        "age": age,
        "height(cm)": height,
        "weight(kg)": weight,
        "waist(cm)": waist,
        "eyesight(left)": eye_l,
        "eyesight(right)": eye_r,
        "hearing(left)": hear_l,
        "hearing(right)": hear_r,
        "systolic": systolic,
        "relaxation": relaxation,
        "fasting blood sugar": fasting,
        "cholesterol": cholesterol,
        "triglyceride": triglyceride,
        "HDL": hdl,
        "LDL": ldl,
        "hemoglobin": hemoglobin,
        "Urine protein": urine,
        "serum creatinine": creatinine,
        "AST": ast,
        "ALT": alt,
        "Gtp": gtp,
        "dental caries": dental
    }])

    pred = model.predict(data)[0]

    if pred == 1:
        st.error("Prediction: Smoker")
    else:
        st.success("Prediction: Non-Smoker")
