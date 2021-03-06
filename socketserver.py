#!/usr/bin/env python
import socket
import threading
import time

def accept(sock,addr):
    print "Recive from %s:%s" %addr
    sock.send("welcome")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == "exit" or not data:
            print "Disconnect from %s:%s" %addr
            break
        sock.send("Hello! %s." %data)
    sock.close()


port = input("Please input port which watched!\n")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",int(port)))
s.listen(5)
print "Waiting for connection"

while True:
   sock, addr  = s.accept()
   t = threading.Thread(target=accept, args=(sock,addr))
   t.start()


