import socket

# Multicast configuration
MULTICAST_IP = '230.0.0.1'
PORT = 5000

# Create UDP socket
sender_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

print("Multicast Sender Started")
print(f"Multicast Group: {MULTICAST_IP}:{PORT}")

# Get message from user
message = input("Enter message to multicast: ")

# Send message to multicast group
sender_socket.sendto(
    message.encode(),
    (MULTICAST_IP, PORT)
)

print(f"Message sent to multicast group: {message}")

# Close socket
sender_socket.close()