#!/usr/bin/python

#socket
#setsockopt
#bind ip and port to socket
#listen for connnection
#accept connection

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("10.0.2.15", 54321))
s.listen(5)
print ('Listening for incoming connections')

target,ip=s.accept()
print ('Connected....')

s.close()
