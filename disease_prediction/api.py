from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

with open("model/diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

app = FastAPI(
    title="Diabetes Prediction API",
    version="1.0"
)

class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.post("/predict")
def predict_diabetes(data: PatientData):
    input_data = np.array([[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])

    prediction = model.predict(input_data)[0]

    result = "Diabetic" if prediction == 1 else "Non-Diabetic"

    return {
        "prediction": result
    }
