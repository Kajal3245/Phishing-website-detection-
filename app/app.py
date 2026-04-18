from flask import Flask, render_template, request
import pickle
import os

# ✅ correct import (since utils is inside app)
from utils.feature_extraction import extract_features

app = Flask(__name__)

# ✅ Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '..', 'models', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

# 🏠 Home route
@app.route('/')
def home():
    return render_template("index.html")

# 🔍 Predict route (FIXED: no error on direct access)
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            url = request.form['url']

            # extract features
            features = extract_features(url)

            # predict
            prediction = model.predict([features])[0]

            result = "Phishing Website ❌" if prediction == 1 else "Safe Website ✅"

            return render_template("index.html", prediction_text=result)

        except Exception as e:
            return render_template("index.html", prediction_text=f"Error: {str(e)}")

    # ✅ if someone opens /predict directly → no crash
    return render_template("index.html")


# 🚀 Run app (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)