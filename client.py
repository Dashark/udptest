#!/usr/bin/env python

from socket import *

HOST = '219.221.196.27'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	file = raw_input('please input file name:')
	with open(file, 'rb') as f:
 		udpCliSock.sendto(f.read(), ADDR)
 
udpCliSock.close() 