from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load model
import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '..', 'models', 'model.pkl')

model = pickle.load(open(model_path, 'rb'))

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
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)