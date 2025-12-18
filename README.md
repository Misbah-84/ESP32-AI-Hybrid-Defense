# 🛡️ ESP32 Hybrid AI Defense System
### *Real-Time Network Security via Machine Learning & Hardware Resilience*

This repository contains the **Adaptive Intelligence Layer** for an ESP32-based secure Access Point. The system employs a hybrid defense strategy, combining low-level C++ firmware protections with a high-level Python AI engine.

## 🧠 AI Layer & Methodology
We developed a system that moves beyond simple static rules. The defense relies on a **Random Forest Classifier** trained to recognize the "fingerprints" of network anomalies.

* **Model:** Random Forest (Ensemble Learning)
* **Key Features:** * *Request Rate*: Monitoring frequency of incoming HTTP requests.
    * *Packet Size*: Analyzing data volume to detect malformed payloads.
* **Response Logic:** Automated IP blacklisting triggered upon anomaly detection.

## 📁 Repository Structure
* `simulate_traffic.py`: Generates a synthetic dataset of "Normal" vs "Attack" traffic.
* `network_traffic.csv`: The structured dataset (1200+ samples) containing network features.
* `train_ai.py`: Training script that optimizes the Random Forest model.
* `traffic_model.pkl`: The **Serialized AI Brain**; the trained model ready for deployment.
* `ai_monitor.py`: The real-time inference engine that monitors live traffic.

## 🚀 Deployment Workflow
1.  **Data Generation:** Execute `simulate_traffic.py` to establish a baseline.
2.  **Model Training:** Run `train_ai.py` to generate the intelligence file (`.pkl`).
3.  **Live Monitoring:** Deploy `ai_monitor.py` to intercept ESP32 traffic logs.

---
### 👨‍💻 Developed By:
**Misbah Ullah** 
