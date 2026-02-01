from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("Prb_congestion_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define request body schema (input JSON)
class PredictionRequest(BaseModel):
    charge_cce: float
    trafic: float
    Nbr_UE: float

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the PRB congestion prediction API"}

# Prediction endpoint
@app.post("/prediction")
def predict(request: PredictionRequest):
    # Extract features from request
    charge_cce = request.charge_cce
    trafic = request.trafic
    Nbr_UE = request.Nbr_UE

    # Create DataFrame exactly like training data
    data = pd.DataFrame([{
    "charge_CCE": request.charge_cce,
    "Trafic": request.trafic,
    "NBR_UE": request.Nbr_UE
  }])


    # Make prediction
    prediction = model.predict(data)

    # Return result
    return {
        "predicted_prb": float(prediction[0])
    }
