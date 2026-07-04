from scapy.all import ARP, Ether, srp
from argparse import ArgumentParser

# Setting up help menu
parser = ArgumentParser(description="Network Scanner using ARP requests")
parser.add_argument("-t", "--target", type=str, required=True, help="Target IP address or range")

args = parser.parse_args()

# Extracting the target IP from command line arguments
target_ip = args.target

# Creating an ARP request packet
arp = ARP(pdst=target_ip)

# Creating Ethernet broadcast packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp

result = srp(packet, timeout=2, verbose=False)[0]

# List of clients, each client is a dictionary with IP and MAC
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# Printing the results
print("Discovered devices on network:")
print("IP Address\t\tMAC Address")
for client in clients:
    print(f"{client['ip']}\t\t{client['mac']}")
