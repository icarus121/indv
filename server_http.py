from http.server import HTTPServer, BaseHTTPRequestHandler
#import request
import socket
#import SimpleHTTPServer

#msg = input("Message:")
#print(output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")
#socket.SOCK_STREAM indicates TCP
#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serversocket.bind(("localhost", 8888))

port = 8888
#host = socket.gethostname()
s.bind(('', port))

s.listen(5)
print("socket bind to " + str(port))

msg =open('index.html', 'r')
message = msg.read()
print(type(msg))
#message = str.encode(msg)

while True:
	c, addr = s.accept()
	print("Got Connection from" + str(addr))
	#c.sendall(bytes(message.encoding = "utf-8"))
	c.send(str.encode(message))
s.close()
