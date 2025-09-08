# Live Network Security Monitor with Anomaly Detection
A real-time network traffic sniffer built with Python. It uses a machine learning model to detect anomalies and displays the results on a live, interactive web dashboard.

# Abstract
This project is a real-time network security monitor developed in Python. The system is engineered to capture network packets efficiently, analyze them for anomalies using a machine learning model, and present the findings on an interactive web dashboard. The architecture employs a multi-threaded producer-consumer model to handle high traffic volumes without packet loss. Network data is captured using the Scapy library, while an Isolation Forest algorithm from Scikit-learn is used to distinguish between normal and anomalous traffic patterns. All captured data is persistently stored in a local SQLite database. The user interface is a live, web-based dashboard created with Streamlit, which visualizes key network metrics, including the latest captured packets, top source IP addresses, and protocol distribution, providing an intuitive and accessible overview of network health and security.

# Features
Real-Time Packet Capture: Sniffs and analyzes network packets on the fly using Scapy.

ML-Powered Anomaly Detection: Utilizes a Scikit-learn (Isolation Forest) model to identify suspicious outliers in network traffic.

High-Performance Architecture: Employs a multi-threaded design to prevent packet loss under heavy load.

Live Interactive Dashboard: Visualizes network activity in real-time with a web-based interface built using Streamlit.

Persistent Logging: All captured packet data is stored in a local SQLite database for later analysis.

# Tools Used
Python

Scapy

Scikit-learn

Streamlit

SQLite

Pandas & NumPy

# How to Run
Running the sniffer requires administrator privileges to access the network interface.

1. Install Dependencies:

pip install -r requirements.txt

2. Train the Model (Run this once):
This command captures a sample of your network traffic to build a baseline for anomaly detection.

# On Windows (in an Administrator terminal)
python train_model.py

# On macOS / Linux
sudo python train_model.py

3. Start the Sniffer:
This command starts the packet capture and analysis. Leave this terminal running in the background.

# On Windows (in an Administrator terminal)
python sniffer.py

# On macOS / Linux
sudo python sniffer.py

4. Launch the Dashboard:
Open a new, second terminal and run this command to start the web interface.

streamlit run dashboard.py

Your web browser should automatically open to the live dashboard.
