from scapy.all import sniff, wrpcap
from datetime import datetime

# Store captured packets
packets = []

# Callback function to process each packet
def packet_callback(packet):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {packet.summary()}")
    packets.append(packet)

print("Sniffing started... Press Ctrl+C to stop.\n")

# Capture 20 packets (you can change this number)
sniff(prn=packet_callback, count=20)

# Save to a .pcap file (can be opened with Wireshark)
wrpcap("captured_packets.pcap", packets)
print("\nPackets saved to 'captured_packets.pcap'")
