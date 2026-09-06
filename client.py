import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

CLIENT_HOST = '127.0.0.1'
CLIENT_PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((CLIENT_HOST, CLIENT_PORT))

print(f"Client socket bound to {CLIENT_HOST}:{CLIENT_PORT}")
print(f"Connecting to server at {SERVER_HOST}:{SERVER_PORT}...")

try:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to server successfully.")

    message = input("Enter message to send: ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Response from server: {response}")

except ConnectionRefusedError:
    print("Connection failed: Server is not running or server port is unavailable.")
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    client_socket.close()
