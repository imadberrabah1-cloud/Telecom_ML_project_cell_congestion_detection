import streamlit as st
import joblib
# load the model and 
model = joblib.load("Prb_congestion_model.pkl")
#stramlit
st.title("Prb congestion")
st.write("enter the value of CCE congestion ,Trafic and number of users")
# user input 
data= st.number_input("CCE congestion ,Trafic and number of users",min_value=0.0,step=1.0)

if st.button("Predict"):
  try:
      data = [[charge_CCE,Trafic,NBR_UE]]
      prediction = model.predict(data)
      st.write(f"predicted cell state :{prediction[0]:.2f)"} 
  except Exception as e:
       st.error(f"Error:{e}")

      
