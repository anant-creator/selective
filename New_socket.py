''' socket with clients in another file '''


import socket

s = socket.socket()
print("Socket Created")

s.bind(("localhost", 9999))

s.listen(5)
print("Waiting for connection")

while True:
	c, addr = s.accept()
	name = c.recv(1024).decode()
	print("connected with ", addr, name)
	
	c.send(bytes("welcome to somewhere" "utf-8"))
