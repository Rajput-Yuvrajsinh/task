import pickle
import matplotlib.pyplot as plt

with open("model/diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

feature_names = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]

importances = model.feature_importances_

plt.figure(figsize=(8, 5))
plt.barh(feature_names, importances)
plt.xlabel("Importance Score")
plt.title("Feature Importance - Diabetes Prediction")
plt.show()
