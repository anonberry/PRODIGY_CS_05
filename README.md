# PRODIGY_CS_05

# 🌐 Network Packet Analyzer

## 📌 Project Overview
The Network Packet Analyzer is a Python-based educational tool designed to capture and inspect network packets on an authorized network interface.

The application uses Scapy to display useful packet information, including source and destination IP addresses, protocol labels, port numbers (when available), packet size, and a short printable payload preview (when exposed).

This project provides an introduction to network traffic analysis and packet inspection.

## 🎯 Objectives
- Understand how network packets are captured and inspected.
- Identify source and destination IP addresses.
- Recognize common network protocols.
- Inspect TCP/UDP port information.
- Learn the basics of packet payloads and their limitations.
- Practice responsible and ethical network analysis.

## ✨ Features
- **Packet Capture:** Captures a user-selected number of packets.
- **Interface Selection:** Allows the user to select a network interface.
- **IP Address Analysis:** Displays source and destination IP addresses when available.
- **Protocol Identification:** Labels common traffic such as DNS, TCP, UDP, and ICMP.
- **Port Information:** Displays TCP/UDP source and destination ports when available.
- **Packet Size:** Shows the captured packet length.
- **Payload Preview:** Displays a short, printable preview of exposed payload data.
- **Controlled Capture:** Limits captures to 1–100 packets and supports stopping with `Ctrl + C`.

## 🛠️ Technologies Used
- Python 3
- Scapy

## 📁 Project Structure
```text
PRODIGY_CS_05/
│
├── network_packet_analyzer.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## 🚀 Getting Started

### Prerequisites
- Python 3 installed.
- A supported packet-capture setup.
- Capture permissions for the selected interface.
- On Windows, Npcap may be required for Scapy packet capture.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anonberry/PRODIGY_CS_05.git
   ```

2. Navigate into the project directory:
   ```bash
   cd PRODIGY_CS_05
   ```

3. (Recommended) Create and activate a virtual environment.

   **Windows:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **Linux/macOS:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If you do not have a `requirements.txt` yet, install Scapy directly:
   ```bash
   pip install scapy
   ```

### Running the Program
```bash
python network_packet_analyzer.py
```

Depending on your operating system and capture configuration, you may need to run the terminal with appropriate privileges. Use elevated permissions only when necessary and authorized.

## 💻 Usage
1. Start the program.
2. Review the available network interfaces.
3. Enter the interface name, or press Enter to use Scapy's default.
4. Choose a packet count between 1 and 100.
5. Observe the packet details displayed in the terminal.
6. Press `Ctrl + C` to stop early.

## ⚙️ How It Works
1. Scapy captures packets from the selected interface.
2. The program checks packet layers to determine a basic protocol label.
3. It extracts IP addresses from IPv4 or IPv6 packets when present.
4. For TCP and UDP packets, it displays source and destination ports.
5. It reports packet length and, when available, a short printable preview of raw payload bytes.
6. The program displays results in the terminal and does not intentionally save captured packets to disk.

## 🔎 Example Output
```text
[1] 14:32:10 | TCP
    Source:      192.168.1.10:52431
    Destination: 93.184.216.34:443
    Packet size: 74 bytes
    Payload:     (no exposed payload)
```

*Example output is illustrative. Actual packet details depend on the traffic and capture environment.*

## 🔒 Security & Ethical Considerations
- Use the analyzer only on devices and networks you own or have explicit permission to monitor.
- Do not capture or inspect other people's private communications without authorization.
- Payload previews may contain sensitive information. Keep captures limited and avoid sharing private packet data or screenshots.
- Encrypted traffic, including HTTPS/TLS, generally does not expose readable application content.
- A network interface may not see all traffic on the network. Visibility depends on the interface, network configuration, operating system, and capture permissions.
- This is an educational analyzer, not a complete protocol dissector or intrusion detection system.

## 📚 Learning Outcomes
- Gained introductory experience with packet capture using Scapy.
- Practiced extracting network and transport-layer metadata.
- Improved understanding of IP addresses, protocols, and ports.
- Learned about payload visibility, encryption, and capture limitations.
- Reinforced responsible cybersecurity practices.

## 👨‍💻 Author
**anonberry**

GitHub: [@anonberry](https://github.com/anonberry)

## 📄 License
This project is licensed under the MIT License.
