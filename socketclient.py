#!/usr/bin/env python
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

while True:
	port = input("Please input the port which want to connect!\n")
	try:
		s.connect(("127.0.0.1",port))
	except:
		print "Port error please try again."
	else:
		break
msg = s.recv(1024)
print "Recive message is %s" %msg
for i in ["Wang","Wan","Wa"]:
    s.send(i)
    print s.recv(1024)

s.send("exit")
s.close()

