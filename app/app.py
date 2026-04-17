from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load model
model = pickle.load(open("../models/model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Since your model needs multiple features,
    # we will just use dummy input for now
    features = [50,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    
    prediction = model.predict([features])[0]

    result = "Phishing Website ❌" if prediction == 1 else "Safe Website ✅"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)