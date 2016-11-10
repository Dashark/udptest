#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

file = raw_input('Please input file name:')
while True:
	print 'waitting for data...'
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	ba =  bytearray(data)
	with open(file, 'ab') as f:
		for b in ba:
			nb = hex(b).replace('0x', '')
			if len(nb) == 2:
				f.write(nb)
			else:
				f.write('0' + nb)
	print 'received...'

udpSerSock.close() 