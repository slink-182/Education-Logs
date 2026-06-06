# following code pasted from ChatGPT


import socket

TARGET = "127.0.0.1"
PORTS = range(1, 1025)

print(f"Scanning {TARGET}...")

for port in PORTS:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((TARGET, port))

    if result == 0:
        print(f"Port {port} is open")

    sock.close()

print("Scan complete.")

