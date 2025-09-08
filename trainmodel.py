import numpy as np
import joblib
from scapy.all import sniff
from sklearn.ensemble import IsolationForest

# --- Configuration ---
SAMPLE_SIZE = 2000  # Number of packets to capture for training
MODEL_FILENAME = 'anomaly_model.pkl'

# --- Data Collection ---
print(f"[*] Starting network capture for training. Capturing {SAMPLE_SIZE} packets...")
captured_packets = []

def packet_callback(packet):
    """Extracts features from each packet for training."""
    # We stop sniffing once we have enough packets
    if len(captured_packets) >= SAMPLE_SIZE:
        return True

    info = {
       # Use 0 as a default if a layer or attribute is missing
       "proto": packet.proto if hasattr(packet, 'proto') else 0,
       "sport": packet.sport if hasattr(packet, 'sport') else 0,
       "dport": packet.dport if hasattr(packet, 'dport') else 0,
       "length": len(packet)
    }
    # Append the feature values as a list
    captured_packets.append(list(info.values()))


# Sniff packets until the stop condition is met
sniff(prn=packet_callback, stop_filter=lambda p: len(captured_packets) >= SAMPLE_SIZE, store=0)

print(f"[+] Captured {len(captured_packets)} packets for training data.")

# --- Model Training ---
if captured_packets:
    # Convert the list of features into a NumPy array for the model
    X_train = np.array(captured_packets, dtype=float)
    
    print("[*] Training the Isolation Forest model... (This may take a moment)")
    # Initialize the model. 'auto' contamination is a good general-purpose setting.
    model = IsolationForest(contamination='auto', random_state=42)
    
    # Train the model on the captured packet data
    model.fit(X_train)
    
    # --- Save the Model ---
    joblib.dump(model, MODEL_FILENAME)
    print(f"[+] Model trained and saved successfully as '{MODEL_FILENAME}'!")
else:
    print("[!] No packets were captured. Model training aborted. Try running as an administrator.")

