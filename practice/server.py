import socket

# Server configuration
host = '127.0.0.1'  # Localhost
port = 12345        # Port to listen on

# Create and configure server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server is listening on port", port)

# Wait for client connection
conn, addr = server_socket.accept()
print("Connected by", addr)

# Receive and print data from client
data = conn.recv(1024).decode()  # Buffer size of 1024
messages = data.split("\n")
data1=messages[0] if messages[0] else "No message"
data2=messages[1] if len(messages)>1 else "No message"
print("Received from client:", data1)
print("Received from client:", data2)

# Close the connection
conn.close()
server_socket.close()
