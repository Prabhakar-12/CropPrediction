import numpy as np
from flask import Flask, request, render_template
import pickle
import os

# Initialize Flask app
flask_app = Flask(__name__)

# Load the model
model_path = os.path.join("..", "model", "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

print(f"✅ Model loaded: {type(model)}")  # Optional debug info

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form inputs and convert to floats
        float_features = [float(x) for x in request.form.values()]
        
        # Convert input to 2D numpy array
        features = np.array([float_features])
        
        # Predict using model
        prediction = model.predict(features)

        # Return result to frontend
        return render_template("index.html", Prediction_text=f"The predicted crop is {prediction[0]}")
    
    except Exception as e:
        return render_template("index.html", Prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    flask_app.run(debug=True)
