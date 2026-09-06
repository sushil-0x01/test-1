import socket

HOST = '0.0.0.0'
PORT = 5000

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server socket
server_socket.bind((HOST, PORT))

# Listen for client
server_socket.listen(1)

print("Server started.")
print(f"Listening on port {PORT}")
print("Waiting for client connection...")

# Accept client connection
client_socket, client_address = server_socket.accept()

print(f"Client connected from {client_address}")

# Receive message
message = client_socket.recv(1024).decode()

print(f"Message received from client: {message}")

# Send response
response = "Message received successfully by server."
client_socket.send(response.encode())

# Close sockets
client_socket.close()
server_socket.close()

print("Connection closed.")