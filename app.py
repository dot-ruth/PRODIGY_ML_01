from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

# Load the trained model
model = joblib.load('house_price_model.pkl')

app = Flask(__name__)

# Enable CORS
CORS(app)

@app.route('/')
def index():
    return "House Price Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    GrLivArea = data['GrLivArea']
    BedroomAbvGr = data['BedroomAbvGr']
    FullBath = data['FullBath']
    
    # Prepare the features for prediction
    features = np.array([[GrLivArea, BedroomAbvGr, FullBath]])
    
    # Make the prediction
    predicted_price = model.predict(features)[0]
    
    return jsonify({"price": predicted_price})

if __name__ == '__main__':
    app.run(debug=True)
