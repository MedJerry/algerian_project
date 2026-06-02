import streamlit as st
import pickle
import numpy as np

# Load model and scaler
ridge_model = pickle.load(open('model/ridgecv.pkl', 'rb'))
standard_scaler = pickle.load(open('model/scaler.pkl', 'rb'))

# Page configuration
st.set_page_config(
    page_title="FWI Prediction",
    page_icon="🔥",
    layout="wide"
)

# Title
st.title("🔥 Forest Fire Weather Index Prediction")
st.write("Enter the required weather parameters below.")

# Input fields
col1, col2 = st.columns(2)

with col1:
    Temperature = st.number_input("Temperature", value=0.0)
    RH = st.number_input("Relative Humidity (RH)", value=0.0)
    Ws = st.number_input("Wind Speed (Ws)", value=0.0)
    Rain = st.number_input("Rain", value=0.0)
    FFMC = st.number_input("FFMC", value=0.0)

with col2:
    DMC = st.number_input("DMC", value=0.0)
    ISI = st.number_input("ISI", value=0.0)
    Classes = st.number_input("Classes", value=0.0)
    Region = st.number_input("Region", value=0.0)

# Prediction button
if st.button("Predict FWI"):
    try:
        features = np.array([[
            Temperature, RH, Ws, Rain,
            FFMC, DMC, ISI, Classes, Region
        ]])

        scaled_data = standard_scaler.transform(features)
        prediction = ridge_model.predict(scaled_data)

        st.success(f"Predicted FWI: {prediction[0]:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")
