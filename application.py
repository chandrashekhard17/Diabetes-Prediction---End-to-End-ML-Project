from flask import Flask, request, app, render_template
import pickle
import numpy as np
import pandas as pd

application = Flask(__name__)
app = application

# Load the scaler and model
scaler = pickle.load(open('models/standardscaler.pkl', 'rb'))
model = pickle.load(open('models/modelforprediction.pkl', 'rb'))

@app.route('/')
def index():
    # Correct the template rendering with quotes
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""
    
    if request.method == 'POST':
        try:
            # Retrieve form data
            Pregnencies = int(request.form.get('Pregnencies'))
            Glucose = float(request.form.get('Glucose'))
            BloodPressure = float(request.form.get('BloodPressure'))
            SkinThickness = float(request.form.get('SkinThickness'))
            Insulin = float(request.form.get('Insulin'))
            BMI = float(request.form.get('BMI'))
            DiabetisPedigreeFunction = float(request.form.get('DiabetisPedigreeFunction'))
            Age = float(request.form.get('Age'))

            # Prepare data and apply scaling
            new_data = scaler.transform([[Pregnencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetisPedigreeFunction, Age]])
            
            # Predict using the model
            predict = model.predict(new_data)
            
            # Interpret prediction
            if predict[0] == 1:
                result = 'Diabetic'
            else:
                result = 'Non Diabetic'
        
        except Exception as e:
            result = f"Error occurred: {e}"
        
        # Render result to template
        return render_template('SinglePrediction.html', result=result)

    # Render the home template if method is GET
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
