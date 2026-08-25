import socket

s = socket.socket()
s.bind(('0.0.0.0', 8080))
s.listen(5)
print("Server is listening on port 8080...")

conn, addr = s.accept()
print(f"Connection established with {addr}")

data = conn.recv(1024)
conn.send(b'Hello!')
conn.close()
