#!/usr/bin/env python3
import socket
import random
import threading
import time
import sys
import os
import subprocess


class NetworkStressTool:
    def __init__(self):
        self.target_ip = ""
        self.target_port = 0
        self.attack_running = False
        self.attack_threads = []

    def print_banner(self):
        """Print the tool banner once at the beginning"""
        banner = """
    ╔═══════════════════════════════════════════════╗
    ║                 NetFloodX                     ║
    ║         Network Stress Testing Tool           ║
    ║        Tool v1.2 (Open Source Edition)        ║
    ║                                               ║
    ║   Desined By : @Cyber_Squad6351               ║
    ║   Insta Id   : Cyber__Squad6351               ║
    ║   youTube    : Cyber_Squad6351                ║
    ║   Website    : cybersquad6351.netlify.app     ║
    ║   E-Mail     : mishraaditya.skm14@gmail.com   ║
    ║                                               ║
    ║   Note : "If U Find Any Error, Bug Or Want    ║
    ║   Help For Using This Tool, You Can Use Above ║
    ║   Information For Contacting Us."             ║ 
    ║                                               ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
           """
        print(banner)

    def get_target_info(self):
        """Get target information from user"""
        print("\n[*] Enter target details:")
        self.target_ip = input("[+] Target IP Address: ")

        while True:
            try:
                port_input = input("[+] Target Port (1-65535): ")
                self.target_port = int(port_input)
                if 1 <= self.target_port <= 65535:
                    break
                else:
                    print("[!] Error: Port must be between 1 and 65535")
            except ValueError:
                print("[!] Error: Please enter a valid port number")

        print(f"\n[*] Target set to {self.target_ip}:{self.target_port}")
        input("\nPress Enter to continue...")

    def start_attack(self, attack_type):
        """Start the specified attack with external scripts"""
        self.attack_running = True
        self.attack_threads = []

        num_threads = 4  # Number of attack threads

        print(f"\n[*] Starting attack on {self.target_ip}:{self.target_port}")

        # Start the respective attack based on the selected attack type
        if attack_type == 1 or attack_type == 3:  # SYN or both
            print("[*] Starting SYN attack...")
            for _ in range(num_threads):
                t = threading.Thread(target=self.run_external_script, args=("Syn.py",))
                t.daemon = True
                t.start()
                self.attack_threads.append(t)

        if attack_type == 2 or attack_type == 3:  # UDP or both
            print("[*] Starting UDP attack...")
            for _ in range(num_threads):
                t = threading.Thread(target=self.run_external_script, args=("Udp.py",))
                t.daemon = True
                t.start()
                self.attack_threads.append(t)

        print(f"[*] Attack started with {len(self.attack_threads)} threads")
        print("[*] Press Ctrl+C to stop the attack")

        try:
            while self.attack_running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_attack()

    def run_external_script(self, script_name):
        """Run the external script (SYN or UDP attack)"""
        try:
            # Get the directory of the current script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Construct the full path to the script
            script_path = os.path.join(current_dir, script_name)
            
            # Check for different case variations of the filename
            if not os.path.exists(script_path):
                # Try with lowercase name
                lowercase_path = os.path.join(current_dir, script_name.lower())
                if os.path.exists(lowercase_path):
                    script_path = lowercase_path
                else:
                    # Try with uppercase first letter
                    capitalized_path = os.path.join(current_dir, script_name.capitalize())
                    if os.path.exists(capitalized_path):
                        script_path = capitalized_path
                    else:
                        print(f"[!] Error: Could not find {script_name}. Make sure it's in the same directory as NetFloodX.py.")
                        return
            
            # Pass correct command line arguments with flags as expected by the scripts
            if script_name.lower() == "syn.py":
                command = ["python3", script_path, "-t", self.target_ip, "-p", str(self.target_port)]
            elif script_name.lower() == "udp.py":
                command = ["python3", script_path, "-t", self.target_ip, "-p", str(self.target_port)]
            else:
                command = ["python3", script_path, "-t", self.target_ip, "-p", str(self.target_port)]
                
            subprocess.call(command)
        except Exception as e:
            print(f"[!] Error running {script_name}: {e}")

    def stop_attack(self):
        """Stop all running attacks"""
        self.attack_running = False
        print("\n[*] Stopping all attacks...")

        for t in self.attack_threads:
            t.join(timeout=1)

        self.attack_threads = []
        print("[*] All attacks stopped")
        input("\nPress Enter to continue...")

    def main_menu(self):
        """Display the main menu and handle user input"""

        self.print_banner()  # Print banner only once
        self.get_target_info()  # Ask for target immediately

        while True:
            print("\nMAIN MENU:")
            print("1. SYN Flood Attack")
            print("2. UDP Flood Attack")
            print("3. Combined Attack (SYN + UDP)")
            print("4. Change Target")
            print("5. Exit")

            choice = input("\nSelect an option (1-5): ")

            if choice in ['1', '2', '3']:  # Attack options
                self.start_attack(int(choice))

            elif choice == '4':  # Change target
                self.get_target_info()

            elif choice == '5':  # Exit
                print("\n[*] Exiting program...")
                sys.exit(0)

            else:
                print("\n[!] Invalid option. Please try again.")
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    tool = NetworkStressTool()

    # Check if running with administrator/root privileges
    try:
        is_admin = os.geteuid() == 0
    except AttributeError:
        is_admin = False  # Windows does not have geteuid, assume not admin

    if not is_admin:
        print("[!] Warning: This tool may require administrator/root privileges to work properly")
        input("Press Enter to continue anyway...")

    # Display disclaimer
    print("\n" + "="*70)
    print("DISCLAIMER: This tool is for educational and testing purposes only.")
    print("Using this tool against targets without explicit permission is illegal")
    print("and may result in legal consequences.")
    print("The author is not responsible for any misuse of this software.")
    print("="*70)

    agree = input("\nDo you agree to use this tool responsibly? (y/n): ")
    if agree.lower() != 'y':
        print("Exiting program...")
        sys.exit(0)

    try:
        tool.main_menu()
    except KeyboardInterrupt:
        print("\n[*] Program interrupted by user. Exiting...")
        sys.exit(0)
