import streamlit as st
import joblib
import pandas as pd
from src.data_preprocessing import load_and_preprocess

st.title("🎓 Student Performance Predictor")

# Load model
model = joblib.load("models/model.pkl")

# Load training structure
X_train, _, _, _ = load_and_preprocess()

st.write("Select a student sample:")

row_index = st.slider("Choose student index", 0, len(X_train)-1, 0)

input_data = pd.DataFrame([X_train.iloc[row_index]])

st.write("Selected Student Data:")
st.dataframe(input_data)

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")
    st.subheader("📊 Feature Importance")
    st.image("models/feature_importance.png")