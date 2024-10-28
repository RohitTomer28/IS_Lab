import socket

# Server configuration
host = '127.0.0.1'  # Server's hostname or IP address
port = 12345        # Port used by the server

# Create and configure client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Send a message to the server
message = "Hello, Server!\nBye Server!"
client_socket.sendall(message.encode())  # Convert string to bytes and send
print("Sent to server:", message)
client_socket.close()
