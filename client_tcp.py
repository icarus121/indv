import socket

#socket.SOCK_STREAM indicates TCP
#clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
print("Socket created")

port = 8888
s.connect(('192.168.0.103', port))
#clientsocket.connect(("localhost", 8888))
#clientsocket.connect(("192.168.0.102", 8888))

#msg = "Hello world from client"
#print("Client sending:" + msg)
#s.send(b'Hellow world from client')

data = s.recv(4096)
print(data)

#print("Client sending reply")
#s.send(b'Client received your message')

#msg = "Hello world from client"
#print("Client sending:" + msg)
#s.send(b(msg))

s.close()

#msg = "Hello World from client"

#print ("client sending:" + msg)
#clientsocket.send(msg)
