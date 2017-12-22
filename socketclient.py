#!/usr/bin/env python
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.67.110.204",9999))
msg = s.recv(1024)
print "Recive message is %s" %msg
for i in ["Wang","Wan","Wa"]:
    s.send(i)
    print s.recv(1024)

s.send("exit")
s.close()

