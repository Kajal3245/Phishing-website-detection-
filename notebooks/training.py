import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv(r"C:\Users\sanja\OneDrive\C PROGRAM\Desktop\phishing-detection\data\phishing.csv", encoding='utf-8-sig')

# Separate features and label
X = df.drop("phishing", axis=1)
y = df["phishing"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
import os
os.makedirs("../models", exist_ok=True)

pickle.dump(model, open("../models/model.pkl", "wb"))

print("Model trained successfully!")