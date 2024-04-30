from flask import Flask, render_template, request, jsonify
from sklearn.datasets import load_iris
import joblib
import os

app = Flask(__name__)

# Define paths
model_dir = os.path.join(app.root_path, 'models')
model_path = os.path.join(model_dir, 'iris_classifier.joblib')

# Load the trained model
model = joblib.load(model_path)

# Mapping dictionary for flower types
class_mapping = {
    0: 'Setosa',
    1: 'Versicolor',
    2: 'Virginica'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    data = request.get_json()

    # Parse input data
    sepalLength = float(data['sepalLength'])
    sepalWidth = float(data['sepalWidth'])
    petalLength = float(data['petalLength'])
    petalWidth = float(data['petalWidth'])

    # Make prediction using the loaded model
    prediction = model.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])

    # Convert numerical prediction to flower type
    predicted_class = int(prediction[0])
    predicted_flower = class_mapping[predicted_class]

    # Return prediction result as JSON response
    return jsonify({'prediction': predicted_flower})

if __name__ == '__main__':
    app.run(debug=True)
