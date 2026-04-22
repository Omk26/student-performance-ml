from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from data_preprocessing import load_and_preprocess

def evaluate_models():
    X_train, X_test, y_train, y_test = load_and_preprocess()

    models = {
        "Random Forest": RandomForestRegressor(),
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor()
    }

    results = []

    print("📊 Model Leaderboard:\n")

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        mse = mean_squared_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        results.append((name, mse, r2))

    # Sort by MSE (lower is better)
    results.sort(key=lambda x: x[1])

    for rank, (name, mse, r2) in enumerate(results, 1):
        print(f"{rank}. {name}")
        print(f"   MSE: {mse:.4f}")
        print(f"   R2: {r2:.4f}\n")
        
    import pandas as pd
    import os

    os.makedirs("models", exist_ok=True)

    df = pd.DataFrame(results, columns=["Model", "MSE", "R2"])
    df.to_csv("models/leaderboard.csv", index=False)

    print("✅ Leaderboard saved in models/leaderboard.csv")

if __name__ == "__main__":
    evaluate_models()