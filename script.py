from scapy.all import *
import random

# ROT47-encoded flag
flag = "7=28LzbbA0:E0$:>A=60$EFA`5N"

# Split flag into chunks (e.g. 5 chars each)
chunk_size = 5
flag_chunks = [flag[i:i + chunk_size] for i in range(0, len(flag), chunk_size)]

# IPs for realism
src_ip = "10.10.10.5"
dst_ip = "10.10.10.10"

# Port where the flag is hidden
flag_port = 31337

packets = []

# Create flag-carrying packets
for i, chunk in enumerate(flag_chunks):
    pkt = IP(src=src_ip, dst=dst_ip) / TCP(sport=random.randint(1024, 65535),
                                           dport=flag_port, seq=1000 + i) / Raw(load=chunk)
    packets.append(pkt)

# Add some decoy packets (random payloads)
for _ in range(10):
    payload = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=random.randint(4, 8)))
    pkt = IP(src=src_ip, dst=dst_ip) / TCP(sport=random.randint(1024, 65535),
                                           dport=random.randint(1000, 9999), seq=random.randint(0, 9999)) / Raw(load=payload)
    packets.append(pkt)

# Shuffle all packets
random.shuffle(packets)

# Save to a pcap file
wrpcap("ctf_hidden_flag.pcap", packets)

print("[+] PCAP saved as ctf_hidden_flag.pcap")
