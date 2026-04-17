import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Load dataset
df = pd.read_csv("data/phishing.csv")

# Features & label
X = df.drop("phishing", axis=1)
y = df["phishing"]

# Model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model
os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")