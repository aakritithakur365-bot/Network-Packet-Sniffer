import sys
from scapy.all import sniff, IP, conf

def packet_callback(packet):
    if packet.haslayer(IP):
        print(f"[+] Packet: {packet[IP].src} ----> {packet[IP].dst}")

def main():
    print("[*] Starting Network Sniffer...")
    print("[*] Searching on all interfaces... Kuch search karke check karein.")
    
    # Layer 3 par socket set karne se Windows par har interface bypass ho jata hai
    conf.L3socket
    
    try:
        # count=100 kar diya hai taaki aapko aaram se packets dikhein
        sniff(prn=packet_callback, count=100, store=0)
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()