#!/usr/bin/python

import socket
import json

s = socket.socket()
host = '10.0.0.4'
port = 12345

#message = '/Active_nodes'
message = '/Node_info'
print('request : %s to %s' % (message, host))
s.connect((host, port))
print('Sending data')
s.send(message.encode())
data = json.loads(s.recv(1024).decode())
print("received data:", data)
print('Connection close')
s.close

