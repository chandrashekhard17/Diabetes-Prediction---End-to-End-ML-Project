# Diabetes Prediction End-to-End ML Project using Logistic Regression

## Project Overview
This project involves building an end-to-end machine learning model for predicting the likelihood of diabetes in patients based on certain medical measurements. The model is created using **Logistic Regression**, one of the most effective techniques for binary classification problems.

### Key Features
- **Data Preprocessing**: Handling missing values, feature scaling.
- **Exploratory Data Analysis (EDA)**: Visualizing data distributions and correlations.
- **Model Building**: Using Logistic Regression to classify patients as diabetic or non-diabetic.
- **Web Application**: A Flask web app that allows users to input new data and get predictions.
  
---

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Building](#model-building)
- [Web Application](#web-application)
- [Results](#results)
- [Screenshots](#screenshots)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)
- [Acknowledgments](#acknowledgments)

---

## Dataset
The dataset used for this project is the **Pima Indians Diabetes Database**. It contains medical diagnostic measurements from 768 female patients, with the goal of predicting whether a patient is diabetic.

### Features:
- `Pregnancies`: Number of pregnancies
- `Glucose`: Plasma glucose concentration
- `BloodPressure`: Diastolic blood pressure
- `SkinThickness`: Triceps skinfold thickness
- `Insulin`: 2-Hour serum insulin
- `BMI`: Body mass index
- `DiabetesPedigreeFunction`: A function that scores the likelihood of diabetes based on family history
- `Age`: Age in years
- `Outcome`: 1 if diabetic, 0 if not

---

## Requirements
To run this project, you will need to install the following dependencies:

```bash
pip install -r requirements.txt
```

### Main Libraries
- **Flask**: For web application development
- **Pandas**: Data manipulation
- **NumPy**: Numerical operations
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib & Seaborn**: Data visualization

---

## Project Structure
Here is the folder structure of the project:

```
├── dataset
│   └── diabetes.csv
├── templates
│   ├── home.html
│   ├── index.html
│   ├── SinglePrediction.html
├── .ebextensions
│   └── python.config
├── application.py
├── requirements.txt
├── README.md
```

---

## Exploratory Data Analysis

Here are some key findings from the Exploratory Data Analysis:

- **Glucose levels** are a strong predictor of diabetes.
- Patients with **high BMI** tend to have a higher chance of diabetes.

### Example Visualization:
![Glucose Distribution](https://github.com/chandrashekhard17/Diabetes-Prediction---End-to-End-ML-Projects/blob/main/Screenshots/output.png)

You can see that most diabetic patients have higher glucose levels compared to non-diabetic patients.

---

## Model Building
### Logistic Regression
We used Logistic Regression as the primary model because it's well-suited for binary classification tasks.

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
```

---

## Web Application

The web application was developed using **Flask**, which allows users to input data and get predictions on whether the patient is likely to have diabetes.

### Example Input Form:
![Input Form Screenshot](https://github.com/chandrashekhard17/Diabetes-Prediction---End-to-End-ML-Projects/blob/main/Screenshots/Screenshot%20(188).png)

### Example Data Filling
![Data filling](https://github.com/chandrashekhard17/Diabetes-Prediction---End-to-End-ML-Projects/blob/main/Screenshots/Screenshot%20(189).png)

### Example Prediction Output:
![Prediction Output Screenshot](https://github.com/chandrashekhard17/Diabetes-Prediction---End-to-End-ML-Projects/blob/main/Screenshots/Screenshot%20(190).png)

---

## Results
The model achieved an accuracy of **78%** on the test set, with the following performance metrics:

- **Precision**: 0.76
- **Recall**: 0.80
- **F1-Score**: 0.78

You can further optimize the model by hyperparameter tuning or using more advanced techniques like ensemble learning.

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/chandrashekhard17/Diabetes-Prediction---End-to-End-ML-Projects.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python application.py
   ```
4. Open your browser and go to:
   ```bash
   http://127.0.0.1:5000/
   ```

You should now see the web application where you can enter patient data to predict the likelihood of diabetes.

---

## Conclusion
This project demonstrates how to build an end-to-end machine learning solution, from data preprocessing and model training to deploying a web app. Logistic Regression provides a solid baseline model for diabetes prediction, and this solution could be extended with more advanced models or additional data features.

---

## Acknowledgments
- The dataset was sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/diabetes).
- Special thanks to [Scikit-learn](https://scikit-learn.org/) for providing easy-to-use machine learning tools.
```

You can copy and paste this into your `README.md` file on GitHub, and it will appear in the "blackboard" style due to the code block formatting. Replace the image paths with the actual image links once you've uploaded your screenshots to the repository.
