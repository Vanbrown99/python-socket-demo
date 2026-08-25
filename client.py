import socket

s = socket.socket()
s.connect(('127.0.0.1', 8080))
s.send(b'Hello!')

data = s.recv(1024)
print(f"Server response: {data.decode()}")
s.close()
