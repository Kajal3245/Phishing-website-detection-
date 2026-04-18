from flask import Flask, render_template, request
import pickle
import os
from utils.feature_extraction import extract_features

app = Flask(__name__)

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '..', 'models', 'model.pkl')

model = pickle.load(open(model_path, 'rb'))

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']   # user input

    # Convert URL → features
    features = extract_features(url)

    # Prediction
    prediction = model.predict([features])[0]

    # Result
    result = "Phishing Website ❌" if prediction == 1 else "Safe Website ✅"

    return render_template("index.html", prediction_text=result)

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)