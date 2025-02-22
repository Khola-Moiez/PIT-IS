from scapy.all import sniff, IP, TCP, UDP, Ether
import argparse

def packet_callback(packet):
    """
    Callback function to process each captured packet.
    """
    if packet.haslayer(IP):
        # Extract IP layer information
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        print(f"\n[+] IP Packet: {ip_src} -> {ip_dst}")

        # Check for TCP layer
        if packet.haslayer(TCP):
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f"    Protocol: TCP")
            print(f"    Source Port: {tcp_sport}")
            print(f"    Destination Port: {tcp_dport}")

        # Check for UDP layer
        elif packet.haslayer(UDP):
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            print(f"    Protocol: UDP")
            print(f"    Source Port: {udp_sport}")
            print(f"    Destination Port: {udp_dport}")

        # Display payload data (first 100 bytes)
        if packet.haslayer(Raw):
            payload = packet[Raw].load[:100]  # Limit payload display to 100 bytes
            print(f"    Payload (first 100 bytes): {payload}")

def start_sniffer(interface=None, count=0):
    """
    Starts the packet sniffer on the specified interface.
    """
    print(f"Starting packet sniffer on interface: {interface}")
    print("Press Ctrl+C to stop.")

    print("\nWARNING: This packet sniffer is for educational purposes only.")
    print("Do not use it without explicit permission from the network owner.")
    print("By running this program, you agree to use it responsibly.")

    # Start sniffing
    sniff(iface=interface, prn=packet_callback, count=count)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Basic Packet Sniffer")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on", required=True)
    parser.add_argument("-c", "--count", type=int, help="Number of packets to capture (0 for unlimited)", default=0)
    args = parser.parse_args()

    # Start the packet sniffer
    start_sniffer(interface=args.interface, count=args.count)