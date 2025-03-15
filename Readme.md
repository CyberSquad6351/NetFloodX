# FloodX - Network Stress Testing Tool



## ⚠️ DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL AND TESTING PURPOSES ONLY**

Using this tool against targets without explicit permission is illegal and may result in legal consequences. The author is not responsible for any misuse of this software.

By using this tool, you agree to use it responsibly and ethically, only on networks and systems you own or have explicit permission to test.

## Description

FloodX is a comprehensive network stress testing tool designed to help network administrators and security professionals evaluate the resilience of their network infrastructure. The tool includes multiple attack simulations including SYN floods and UDP floods to test network stability under stress conditions.

## Features

- **SYN Flood Attack**: Tests TCP connection handling by sending numerous TCP SYN packets
- **UDP Flood Attack**: Tests UDP packet processing capabilities
- **Combined Attack Mode**: Simultaneously performs SYN and UDP flood attacks
- **Customizable Parameters**: Adjust packet size, intervals, and more
- **Performance Metrics**: Real-time reports on packets sent and transmission rates

## Requirements

- Python 3.6+
- Linux operating system (recommended)
- Root/Administrator privileges

## Installation

```bash
# Clone the repository
git clone https://github.com/cybersquad6351/NetFloodX.git

# Change to the directory
cd FloodX

# Make the main script executable
chmod +x FloodX.py
```

## Usage

The tool requires root privileges to create raw sockets:

```bash
sudo python3 FloodX.py
```

### SYN Flood Script Usage

```bash
sudo python3 Syn.py -t TARGET_IP -p TARGET_PORT [-s SOURCE_IP] [-i REPORT_INTERVAL]
```

Options:
- `-t, --target`: Target IP address
- `-p, --port`: Target port (default: 80)
- `-s, --source`: Source IP address (default: auto-detect)
- `-i, --interval`: Reporting interval in packets (default: 1000)

### UDP Flood Script Usage

```bash
python3 Udp.py -t TARGET_IP [-p TARGET_PORT] [-s PACKET_SIZE] [-n PACKET_COUNT] [-i INTERVAL]
```

Options:
- `-t, --target`: Target IP address (required)
- `-p, --port`: Target port (default: 80)
- `-s, --size`: Packet size in bytes (default: 1024)
- `-n, --packets`: Number of packets to send (0 for infinite)
- `-i, --interval`: Delay between packets in seconds (default: 0.01)

## How It Works

FloodX operates by generating network traffic:

1. **SYN Floods**: Creates TCP SYN packets with randomized source ports to establish connections that consume resources on the target server.
2. **UDP Floods**: Sends UDP packets to random or specified ports to consume bandwidth and processing resources.
3. **Multi-threading**: Uses multiple threads to maximize the traffic generation capability.

## Legitimate Use Cases

- Testing network infrastructure resilience
- Validating firewall and IDS/IPS configurations
- Stress testing server applications
- Research on DDoS mitigation techniques

## Developer Information

- **Developer**: Cyber_Squad6351
- **Email**: mishraaditya.skm14@gmail.com
- **Website**: [cybersquad6351.netlify.app](https://cybersquad6351.netlify.app)
- **Instagram**: [@cyber__squad6351](https://www.instagram.com/cyber__squad6351/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This tool was created for educational purposes to understand network security concepts
- Thanks to all the community members who provided feedback and suggestions

---

⚠️ **Remember**: Always obtain proper authorization before conducting any network stress tests.

---

© 2025 Cyber Squad | Created for Network Security Education