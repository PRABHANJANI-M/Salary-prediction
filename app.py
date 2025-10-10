# app.py
# ------------------------------------------
# Streamlit App for Salary Prediction using Pickled Model

import streamlit as st
import numpy as np
import pickle
import pandas as pd

# 1️⃣ Load trained model
model = pickle.load(open("salary_model.pkl", "rb"))

# 2️⃣ Streamlit app configuration
st.set_page_config(page_title="Salary Prediction App", page_icon="💼", layout="centered")

# 3️⃣ Custom CSS for red-black background and styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #FF0000, #000000);
            color: white;
            text-align: center;
        }
        input, button {
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #FF0000;
            color: white;
            border: none;
            padding: 0.5em 1em;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #990000;
        }
        h1, h2, h3, h4, h5, h6 {
            color: white;
        }
        .css-1d391kg {  /* For Streamlit number_input text */
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# 4️⃣ Title and description
st.title("💼 Salary Prediction App")
st.write("Predict your salary based on your years of experience!")

# 5️⃣ Input
experience = st.number_input("Enter your Years of Experience:", min_value=0.0, step=0.1)

# 6️⃣ Predict button
if st.button("Predict Salary"):
    try:
        prediction = model.predict(np.array([[experience]]))
        st.success(f"💰 Estimated Salary: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# 7️⃣ Optional: Show dataset preview
st.markdown("---")
st.subheader("📊 Dataset Preview")
try:
    data = pd.read_csv("Salary_dataset.csv")
    st.dataframe(data.head())
except FileNotFoundError:
    st.warning("Salary_dataset.csv not found. Place it in the same directory.")

# 8️⃣ Footer
st.markdown("---")
st.write("© 2025 Salary Prediction App")
