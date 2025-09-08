# Network Packet Sniffer with Anomaly Detection

## Features
- Real-time network sniffing with Scapy
- Anomaly detection (simple logic, expandable to ML)
- Alert system via print/log or email
- SQLite logging and CLI/graphical traffic summary

## Usage
Install requirements:
    pip install -r requirements.txt

Run the sniffer:
    sudo python sniffer.py

See traffic summary and plot:
    python report.py

## Extending
- Add GUI with Tkinter/PyQt
- Improve anomaly logic in anomaly.py
- Set email server in alert.py
