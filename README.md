# 🕵️‍♂️ CTF Challenge: Hidden in the Traffic

Your mission: **Find the flag hidden inside this PCAP file**.

The flag is **encoded** and buried in a stream of packets. You’ll need to inspect the packet payloads carefully to find it.

---

## 📁 File Provided

- `ctf_hidden_flag.pcap` – A network capture file containing the hidden flag

---

## 🧩 Challenge Details

- The flag has already been encoded.
- It has been split into chunks and embedded in several **TCP packets**.
- Other packets are included as noise to throw off easy detection.

---

## 🛠️ Tools Needed

- **Wireshark** (GUI)
- or **TShark** (CLI)
- or **Python + Scapy** (if scripting)
