import streamlit as st
import joblib

model = joblib.load("Prb_congestion_model.pkl")

st.title("Prb congestion")
st.write("Enter CCE congestion, Traffic and number of users")

# 3 inputs
charge_CCE = st.number_input("CCE congestion", min_value=0.0, step=1.0)
Traffic    = st.number_input("Traffic",        min_value=0.0, step=1.0)
NBR_UE     = st.number_input("Number of users (NBR_UE)", min_value=0.0, step=1.0)

if st.button("Predict"):
    try:
        X = [[charge_CCE, Traffic, NBR_UE]]
        prediction = model.predict(X)
        st.write(f"Predicted cell state: {float(prediction[0]):.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
      
