import socket

#msg = input("Message:")
#print(output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")
#socket.SOCK_STREAM indicates TCP
#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serversocket.bind(("localhost", 8888))
#serversocket.listen(1)

port = 8888
s.bind(('', port))

s.listen(5)
print("socket bind to " + str(port))

msg = """
HTTP/1.1
Content-Type: text/html

<html>
<body>
<b>Hello World</b>
</body>
</html>

"""
#msg = str.encode()

#while True:
c, addr = s.accept()
c.send(msg)
#print("Got connection from " + str(addr))

	#msg = s.recv(4096)
	#print("server received" + msg)

	#msg = input("input:")
	#c.send(b'Thank you for connecting')
#c.send(b'Hello World from server')

#msg = c.recv(4096)
#print(msg)

	#msg = s.recv(4096)
	#print("server received" + msg)
	#s.send(msg)


#(clientsocket, address) = serversocket.accept()
#msg = clientsocket.recv(1024)
#print ("server received" + msg)

c.close()
s.close()
