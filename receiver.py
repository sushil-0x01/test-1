import socket
import struct

# Multicast configuration
MULTICAST_IP = "230.0.0.1"
PORT = 5000

# 1. Create UDP socket
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# 2. Allow immediate reuse of the port
receiver_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 3. Bind to the port (Use MULTICAST_IP instead of '' if you are on Windows)
receiver_socket.bind(("", PORT))

# 4. Pack the ip_mreq structure (4 bytes multicast IP + 4 bytes interface IP)

multicast_request = struct.pack(
    "4s4s", socket.inet_aton(MULTICAST_IP), socket.inet_aton("0.0.0.0")
)

# 5. Join the multicast group
receiver_socket.setsockopt(
    socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, multicast_request
)

print("Multicast Receiver Started")
print(f"Joined multicast group: {MULTICAST_IP}:{PORT}")
print("Waiting for messages...\n")

try:
    # 6. Infinite loop to continuously listen for data
    while True:
        data, address = receiver_socket.recvfrom(1024)
        message = data.decode("utf-8")
        print(f"[{address[0]}:{address[1]}]: {message}")
except KeyboardInterrupt:
    print("\nReceiver stopped by user.")
finally:
    # 7. Clean up socket
    receiver_socket.close()
