import socket
import threading

# Get local details
MY_IP = input("Enter your IP address: ")
MY_PORT = int(input("Enter your port number: "))

# Get peer details
PEER_IP = input("Enter peer IP address: ")
PEER_PORT = int(input("Enter peer port number: "))

# Create listening socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((MY_IP, MY_PORT))
server.listen(1)

print(f"\nPeer started at {MY_IP}:{MY_PORT}")

choice = input("Do you want to initiate the connection? (y/n): ")

if choice.lower() == "y":
    # Initiator
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((PEER_IP, PEER_PORT))
    print(f"Connected to peer at {PEER_IP}:{PEER_PORT}")

else:
    # Receiver
    sock, address = server.accept()
    print(f"Connected to peer at {address}")

# Question 2
# Function to continuously receive messages
def receive():
    while True:
        try:
            message = sock.recv(1024).decode()

            if message:
                print(f"\nPeer: {message}")
                print("You: ", end="", flush=True)
            else:
                break

        except:
            break


# Start receiving thread
thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()


# Send messages
while True:
    message = input("You: ")

    if message.lower() == "exit":
        break

    sock.sendall(message.encode())


sock.close()
server.close()