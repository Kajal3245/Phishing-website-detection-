from flask import Flask, render_template, request
import pickle
import os

# ✅ correct import
from utils.feature_extraction import extract_features

app = Flask(__name__)

# ✅ load model
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
    try:
        url = request.form['url']

        features = extract_features(url)
        prediction = model.predict([features])[0]

        result = "Phishing Website ❌" if prediction == 1 else "Safe Website ✅"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)