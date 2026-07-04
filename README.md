# Network Scanner

A lightweight ARP-based network discovery tool written in Python. It identifies live hosts on a local network segment by sending ARP requests and collecting the responses, which include each device's IP and MAC address.

**Authorized use only.** Only run this against networks you own or have explicit written authorization to scan. Unauthorized network reconnaissance can violate computer-misuse laws depending on jurisdiction, even when no data is altered or exfiltrated.

## How it works

The scanner sends an ARP request asking "who has this IP address?" to a target IP or IP range (e.g. `192.168.1.0/24`). Any live device at that address responds with its MAC address, which the scanner captures and reports. This is the same technique used by tools like `arp-scan` and the host-discovery phase of `nmap -sn`, and it's typically the first step in both a network asset inventory and the reconnaissance phase of an authorized penetration test.

![ARP request example](https://github.com/user-attachments/assets/f2d0d950-336e-4f37-b7ed-fb685587e523)

## Requirements

- Python 3.x
- [`scapy`](https://scapy.net/)
- Root/administrator privileges (required to send raw ARP packets)

## Installation

```bash
git clone https://github.com/samuelHenris/Network-Scanner.git
cd Network-Scanner
pip install scapy
```

## Usage

```bash
sudo python3 networkScanner.py -t 192.168.1.0/24
```

Replace `192.168.1.0/24` with your target IP or CIDR range. Root privileges are required because the scanner constructs and sends raw Ethernet/ARP frames.

## Example output

```
Discovered devices on network:
IP Address              MAC Address
192.168.1.1             aa:bb:cc:dd:ee:ff
192.168.1.24            11:22:33:44:55:66
```

## Notes

This tool only performs host discovery: it does not port-scan, fingerprint services, or attempt any exploitation. In a real assessment it's typically paired with follow-on tools (e.g. `nmap` for service enumeration) once live hosts are identified.
