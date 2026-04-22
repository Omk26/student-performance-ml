from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from src.data_preprocessing import load_and_preprocess

def train():
    X_train, X_test, y_train, y_test = load_and_preprocess()

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    print("MSE:", mse)

    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train()