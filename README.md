Live Network Security Monitor with Anomaly Detection
A real-time network traffic sniffer built with Python. It uses a machine learning model to detect anomalies and displays the results on a live web dashboard.

Features
Real-time Packet Capture: Sniffs network packets and analyzes them on the fly using Scapy.

ML-Powered Anomaly Detection: Uses a Scikit-learn (Isolation Forest) model to learn normal traffic patterns and flag suspicious outliers.

High-Performance: Employs a multi-threaded, producer-consumer model to handle heavy traffic without dropping packets.

Live Interactive Dashboard: Visualizes network activity in real-time with a web-based interface built using Streamlit.

Persistent Logging: All captured packet data is stored in a local SQLite database for later analysis.

Usage
1. Installation
First, clone the repository and install the necessary dependencies.

# Clone the repository to your local machine
git clone [https://github.com/your-username/network-sniffer.git](https://github.com/your-username/network-sniffer.git)

# Navigate into the project directory
cd network-sniffer

# Install all required libraries
pip install -r requirements.txt

2. How to Run
Running the sniffer requires administrator privileges to access the network interface.

Step 1: Train the Model (Run this once)

This command captures a sample of your network traffic to build a baseline for anomaly detection.

# On Windows (in an Administrator terminal)
python train_model.py

# On macOS / Linux
sudo python train_model.py

Step 2: Start the Sniffer

This command starts the packet capture and analysis. It will run continuously in the background.

# On Windows (in an Administrator terminal)
python sniffer.py

# On macOS / Linux
sudo python sniffer.py

Step 3: Launch the Dashboard

Open a new, second terminal and run this command to start the web interface.

streamlit run dashboard.py

Your web browser should automatically open to the live dashboard.

Project Structure
├── anomaly.py          # Handles ML-based anomaly detection.
├── dashboard.py        # The Streamlit web dashboard.
├── db.py               # Manages the SQLite database.
├── sniffer.py          # The core packet sniffing script.
├── train_model.py      # Script to train the ML model.
├── alert.py            # Placeholder for alert functions.
├── requirements.txt    # List of project dependencies.
└── README.md           # This file.
