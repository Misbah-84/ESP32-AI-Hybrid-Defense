import pandas as pd
import numpy as np

# This creates 1000 rows of 'Normal' traffic and 200 rows of 'Attack' traffic
normal = pd.DataFrame({
    'request_rate': np.random.uniform(0.1, 2.0, 1000),
    'packet_size': np.random.randint(100, 800, 1000),
    'is_attack': 0
})

attack = pd.DataFrame({
    'request_rate': np.random.uniform(20.0, 100.0, 200),
    'packet_size': np.random.randint(1500, 5000, 200),
    'is_attack': 1
})

# Combine and save as the CSV file your AI needs
df = pd.concat([normal, attack])
df.to_csv('C:/Users/Misbah/Desktop/network_traffic.csv', index=False)

print("--- SUCCESS ---")
print("File 'network_traffic.csv' has been created on your Desktop.")