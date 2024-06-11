import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f"Starting scan on host: {target}")

    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scanning completed in: {total_time}")

if __name__ == "__main__":
    target = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    if not target:
        print("Invalid IP address. Please enter a valid IP address.")
    elif start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Please enter a valid range (1-65535).")
    else:
        scan_ports(target, start_port, end_port)