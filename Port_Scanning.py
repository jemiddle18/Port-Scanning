import socket
import pyfiglet

# Display banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Input for the target IP
target = input("Enter target IP address: ")

# Perform port scanning
print(f"Scanning ports on {target}...")

for port in range(1, 1025):  # Scan well-known ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout to 1 second for better performance
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
    except Exception as e:
        print(f"Error on port {port}: {e}")
    finally:
        sock.close()
