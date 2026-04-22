import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(path="data/student-mat.csv"):
    df = pd.read_csv(path)

    # Example encoding (adjust based on your notebook)
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    
    X = df.drop("G3", axis=1)   # target column (adjust if needed)
    y = df["G3"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test