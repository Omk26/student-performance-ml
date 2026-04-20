# 🎓 Explainable Student Performance Prediction using Machine Learning

## 📌 Project Description

This project aims to predict student academic performance using multiple machine learning models and identify the key factors influencing the results. The system compares different models, selects the best-performing one, and provides interpretability using feature importance.

---

## 🎯 Objectives

* Predict whether a student will pass or fail based on various features
* Compare multiple machine learning models
* Select the most accurate model
* Identify important factors affecting student performance

---

## 📊 Dataset

The project uses the **Student Performance Dataset**, which includes academic, social, and behavioral attributes of students.

### 🔹 Key Features:

* Study time
* Attendance-related factors (absences)
* Previous grades (G1, G2)
* Family background
* Lifestyle factors (alcohol consumption, free time, etc.)

### 🎯 Target Variable:

* Final Grade (G3) converted into:

  * **Pass (1)**
  * **Fail (0)**

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

---

## 🤖 Machine Learning Models Used

* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)

---

## 📈 Model Comparison

All models were trained and evaluated using accuracy.

| Model               | Description             |
| ------------------- | ----------------------- |
| Decision Tree       | Simple tree-based model |
| Random Forest       | Best performing model   |
| KNN                 | Distance-based model    |

---

## 🏆 Best Model

* **Random Forest** achieved the highest accuracy and was selected as the final model.

---

## 📊 Model Evaluation

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## 🔍 Explainability

To understand the model decisions, **Random Forest feature importance** was used.

This helps identify:

* Which features most influence student performance
* Key factors such as study time, previous grades, and absences

---

## 🚀 How to Run the Project

1. Clone the repository
2. Install required libraries:

   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
3. Open the Jupyter Notebook
4. Run all cells

---

## 🏁 Conclusion

This project successfully demonstrates how machine learning can be used to predict student performance and analyze the factors affecting it. The combination of model comparison and feature importance provides both accuracy and interpretability.

---

## 📌 Future Improvements

* Add more advanced models (XGBoost, Neural Networks)
* Deploy as a web application
* Use real-time student data

---

## 👨‍💻 Author

Chaitanya Meher
Swaraj Mathwad
Durvesh Rane

---
