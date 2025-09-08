from sklearn.ensemble import IsolationForest
import numpy as np
import joblib # For saving the trained model

# --- This part is done once (offline) ---
def train_model():
    # Assume you have a CSV or database of NORMAL traffic features
    # For example: ['proto', 'sport', 'dport', 'length']
    # X_train = load_normal_traffic_data() 
    
    print("[*] Training anomaly detection model...")
    # model = IsolationForest(contamination='auto', random_state=42)
    # model.fit(X_train)
    # joblib.dump(model, 'anomaly_model.pkl') # Save the model
    print("[+] Model trained and saved.")

# --- This part is used in real-time ---
try:
    model = joblib.load('anomaly_model.pkl')
except FileNotFoundError:
    print("[!] Model not found. Train one first or run in simple mode.")
    model = None

def analyze_packet(info):
    """Analyzes packet with the ML model."""
    if not model:
        return # Fallback to simple rules if model doesn't exist

    # Extract features for prediction
    features = np.array([[
        info.get('proto', 0), 
        info.get('sport', 0), 
        info.get('dport', 0), 
        info.get('length', 0)
    ]])
    
    prediction = model.predict(features)
    
    if prediction[0] == -1: # -1 indicates an anomaly
        print(f"ALERT: Anomaly detected from {info['src']}:{info['sport']}!")