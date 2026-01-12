import streamlit as st
import joblib
import pandas as pd

# Load the trained model
try:
    model = joblib.load("model/student_model.pkl")
except FileNotFoundError:
    st.error("Model file not found. Please run train.py first.")
    st.stop()

st.set_page_config(page_title="Student Performance AI", page_icon="🎓")

st.title("🎓 Student Performance AI")
st.write("Predict final performance score based on study habits.")

# Input form
with st.form("prediction_form"):
    attendance = st.number_input("Attendance Rate (%)", min_value=0, max_value=100, value=85)
    study_hours = st.number_input("Weekly Study Hours", min_value=0.0, step=0.1, value=5.0)
    previous_score = st.number_input("Previous Semester Score", min_value=0, max_value=100, value=75)
    
    submitted = st.form_submit_button("Predict Score")

if submitted:
    # Make prediction
    prediction = model.predict([[attendance, study_hours, previous_score]])
    final_score = round(prediction[0], 2)
    
    st.success(f"Predicted Final Score: **{final_score}**")
    
    if final_score >= 80:
        st.balloons()
