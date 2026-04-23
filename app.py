import streamlit as st
import joblib
import pandas as pd
import os
from src.data_preprocessing import load_and_preprocess

st.set_page_config(page_title="🎓 Student Performance ML", layout="wide")

# ── Header ─────────────────────────────────────────────────────────────────
st.title("🎓 Student Performance Predictor")
st.caption("Explainable ML · Auto-evaluated via GitHub Actions")

# ── Tabs ───────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["📈 Predictor", "🏆 Leaderboard"])

# ── Tab 1: Predictor ───────────────────────────────────────────────────────
with tab1:
    model_path = "models/model.pkl"
    if not os.path.exists(model_path):
        st.warning("⚠️ No trained model found. Run the training pipeline first.")
    else:
        model = joblib.load(model_path)
        X_train, _, _, _ = load_and_preprocess()

        st.write("Select a student sample:")
        row_index = st.slider("Choose student index", 0, len(X_train) - 1, 0)
        input_data = pd.DataFrame([X_train.iloc[row_index]])

        st.write("Selected Student Data:")
        st.dataframe(input_data, use_container_width=True)

        if st.button("Predict", type="primary"):
            prediction = model.predict(input_data)
            st.success(f"🎯 Predicted Final Grade (G3): **{prediction[0]:.2f}**")

        if os.path.exists("models/feature_importance.png"):
            st.subheader("📊 Feature Importance")
            st.image("models/feature_importance.png")

# ── Tab 2: Leaderboard ─────────────────────────────────────────────────────
with tab2:
    st.subheader("🏆 Model Leaderboard")
    st.caption("Auto-updated every time a Pull Request is merged via GitHub Actions.")

    leaderboard_path = "leaderboard.csv"

    if not os.path.exists(leaderboard_path):
        st.info("No submissions yet. Fork the repo, add your model, and open a PR!")
    else:
        df = pd.read_csv(leaderboard_path)

        # Rank column
        df.insert(0, "Rank", range(1, len(df) + 1))

        # Highlight top row
        def highlight_top(row):
            return ["background-color: #ffd70033"] * len(row) if row["Rank"] == 1 else [""] * len(row)

        # Display
        st.dataframe(
            df.style.apply(highlight_top, axis=1).format({"mse": "{:.4f}", "r2": "{:.4f}"}),
            use_container_width=True,
            hide_index=True,
        )

        # Summary metrics
        best = df.iloc[0]
        col1, col2, col3 = st.columns(3)
        col1.metric("🥇 Best Model", best["model"])
        col2.metric("👤 Best Contributor", best["contributor"])
        col3.metric("📈 Best R² Score", f"{best['r2']:.4f}")

        # Bar chart of R2 scores
        st.subheader("R² Score Comparison")
        chart_data = df.set_index("model")[["r2"]].sort_values("r2", ascending=False)
        st.bar_chart(chart_data)

    # How to contribute section
    with st.expander("🚀 How to contribute your model"):
        st.markdown("""
        1. **Fork** this repository on GitHub
        2. Add your model to `src/` — expose it via `get_models()` or `MODELS` dict:
           ```python
           # src/my_model.py
           from xgboost import XGBRegressor

           def get_models():
               return {"XGBoost": XGBRegressor()}
           ```
        3. Open a **Pull Request** against `main`
        4. GitHub Actions will automatically:
           - Run `evaluate_pr.py`
           - Score your model (MSE + R²)
           - Update `leaderboard.csv`
           - Comment results on your PR
        5. Refresh this page to see your result! 🎉
        """)
