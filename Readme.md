# NetFloodX - Network Stress Testing Tool


## ⚠️ DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL AND TESTING PURPOSES ONLY**

Using this tool against targets without explicit permission is illegal and may result in legal consequences. The author is not responsible for any misuse of this software.

By using this tool, you agree to use it responsibly and ethically, only on networks and systems you own or have explicit permission to test.

## Description

NetFloodX is a comprehensive network stress testing tool designed to help network administrators and security professionals evaluate the resilience of their network infrastructure. The tool includes multiple attack simulations including SYN floods and UDP floods to test network stability under stress conditions.

## Features

- **SYN Flood Testing**: Tests TCP connection handling by sending numerous TCP SYN packets
- **UDP Flood Testing**: Tests UDP packet processing capabilities
- **Combined Test Mode**: Simultaneously performs SYN and UDP flood tests
- **Multi-threading**: Uses multiple threads to maximize testing capabilities
- **User-friendly Interface**: Simple command-line menu for easy operation
- **Cross-platform Support**: Works on major operating systems with Python 3

## Requirements

- Python 3.6+
- Administrative/root privileges (required for raw socket creation)
- External scripts: Syn.py and Udp.py (included in the package)

## Installation

```bash
# Clone the repository
git clone https://github.com/cybersquad6351/NetFloodX.git

# Change to the directory
cd NetFloodX

# Make sure the scripts are executable
chmod +x NetFloodX.py Syn.py Udp.py
```

## Usage

The tool requires root privileges to create raw sockets:

```bash
sudo python3 NetFloodX.py
```

After launching the tool:
1. Enter the target IP address and port
2. Select the type of stress test from the menu
3. The tool will execute the selected test
4. Press Ctrl+C to stop the test

### Main Menu Options

1. **SYN Flood Test**: Launches TCP SYN flood testing
2. **UDP Flood Test**: Launches UDP flood testing
3. **Combined Test**: Launches both SYN and UDP flood tests simultaneously
4. **Change Target**: Modify the target IP and port
5. **Exit**: Quit the application

### SYN Flood Script Usage (Standalone)

```bash
sudo python3 Syn.py -t TARGET_IP -p TARGET_PORT
```

### UDP Flood Script Usage (Standalone)

```bash
sudo python3 Udp.py -t TARGET_IP -p TARGET_PORT
```

## How It Works

NetFloodX operates by generating network traffic to test infrastructure resilience:

1. **SYN Flood Testing**: Creates TCP SYN packets with randomized source ports to test how servers handle multiple connection attempts.
2. **UDP Flood Testing**: Sends UDP packets to specified ports to test bandwidth and processing capabilities.
3. **Multi-threading**: Uses 4 threads per test type to provide comprehensive stress testing.

## Legitimate Use Cases

- Testing network infrastructure resilience
- Validating firewall and IDS/IPS configurations
- Stress testing server applications
- Network capacity planning
- Security research on DDoS mitigation techniques

## Developer Information

- **Developer**: Cyber_Squad6351
- **Email**: mishraaditya.skm14@gmail.com
- **Website**: [cybersquad6351.netlify.app](https://cybersquad6351.netlify.app)
- **Instagram**: [@cyber__squad6351](https://www.instagram.com/cyber__squad6351/)
- **YouTube**: [Cyber_Squad6351](https://www.youtube.com/c/Cyber_Squad6351)

## Version History

- **v1.2 (Open Source Edition)**: Current stable release

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This tool was created for educational purposes to understand network security concepts
- Thanks to all the community members who provided feedback and suggestions

---

⚠️ **Remember**: Always obtain proper authorization before conducting any network stress tests.

---

© 2025 Cyber Squad | Created for Network Security Education
