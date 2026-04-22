import joblib
import pandas as pd

def predict(input_data):
    
    # input_data must be preprocessed same as training data
    
    model = joblib.load("models/model.pkl")

    df = pd.DataFrame([input_data])
    prediction = model.predict(df)

    return prediction[0]