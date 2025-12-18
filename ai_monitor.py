import joblib
import pandas as pd

# 1. Load your trained AI Brain
model = joblib.load('C:/Users/Misbah/Desktop/traffic_model.pkl')

print("AI Monitor is ACTIVE. Waiting for ESP32 data...")

def analyze_traffic(rate, size):
    # This simulates receiving one line of data from the ESP32
    new_data = pd.DataFrame([[rate, size]], columns=['request_rate', 'packet_size'])
    prediction = model.predict(new_data)
    
    if prediction[0] == 1:
        print(f"⚠️ ATTACK DETECTED! (Rate: {rate}, Size: {size}) -> ACTION: BLOCKING IP")
    else:
        print(f"✅ Traffic Normal. (Rate: {rate}, Size: {size})")

# TEST: Let's pretend the ESP32 just sent us some data
print("\n--- Running Security Test ---")
analyze_traffic(1.5, 400)   # Normal traffic test
analyze_traffic(55.0, 3000) # Attack traffic test