import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 1. Path to your data
data_path = 'C:/Users/Misbah/Desktop/network_traffic.csv'
model_path = 'C:/Users/Misbah/Desktop/traffic_model.pkl'

if os.path.exists(data_path):
    # 2. Load the CSV data
    data = pd.read_csv(data_path)
    X = data[['request_rate', 'packet_size']] # Features (The numbers the AI looks at)
    y = data['is_attack']                     # Labels (0 for Safe, 1 for Attack)

    # 3. Initialize and Train the "Brain"
    print("Training the AI model... please wait.")
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    # 4. Save the "Brain" as a file
    joblib.dump(model, model_path)

    print("--- SUCCESS ---")
    print(f"AI Model 'traffic_model.pkl' has been created on your Desktop.")
    print("Your AI is now trained and ready to defend the ESP32!")
else:
    print("Error: network_traffic.csv not found on Desktop. Run simulate_traffic.py first.")