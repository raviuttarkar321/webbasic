import socket
print("hi")
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server
print("hi")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(s.connect((HOST, PORT)))
    print("connection successful")
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))