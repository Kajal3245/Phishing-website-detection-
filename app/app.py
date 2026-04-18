from flask import Flask, render_template, request
import pickle
import os

# ✅ correct import (utils is inside app folder)
from utils.feature_extraction import extract_features

app = Flask(__name__)

# ✅ Load model safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '..', 'models', 'model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# 🏠 Home route
@app.route('/')
def home():
    return render_template("index.html")

# 🔍 Predict route (FINAL VERSION)
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        url = request.form.get('url')

        # ⚠️ Handle empty input
        if not url:
            return render_template("index.html", prediction_text="Please enter a URL ⚠️")

        url_lower = url.lower()

        # 🚨 STRONG rule-based phishing detection
        suspicious_keywords = ["@", "login", "verify", "update", "secure", "account", "bank"]

        if any(word in url_lower for word in suspicious_keywords):
            return render_template("index.html", prediction_text="Phishing Website ❌")

        try:
            # ML prediction
            features = extract_features(url)
            prediction = model.predict([features])[0]

            result = "Phishing Website ❌" if prediction == 1 else "Safe Website ✅"

            return render_template("index.html", prediction_text=result)

        except Exception as e:
            return render_template("index.html", prediction_text=f"Error: {str(e)}")

    # If user opens /predict directly
    return render_template("index.html")


# 🚀 Run app (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)