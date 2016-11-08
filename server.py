#!/usr/bin/env python

from socket import *

HOST = '219.221.196.27'
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
		f.write('Type:' + str(bin(ba[0])) + '\n')
		f.write('Length:' + str(bin(ba[1])) + str(bin(ba[2])) + '\n')
		f.write('MT ID:' + str(bin(ba[3])) + str(bin(ba[4])) + str(bin(ba[5])) + str(bin(ba[6])) + str(bin(ba[7])) + str(bin(ba[8])) + '\n')
		f.write('Sequence ID:' + str(bin(ba[9])) + str(bin(ba[10])) + str(bin(ba[11])) + str(bin(ba[12])) + '\n')
		f.write('GPS Longitude:' + str(bin(ba[13])) + str(bin(ba[14])) + str(bin(ba[15])) + str(bin(ba[16])) + str(bin(ba[17])) + '\n')
		f.write('GPS Latitude:' + str(bin(ba[18])) + str(bin(ba[19])) + str(bin(ba[20])) + str(bin(ba[21])) + str(bin(ba[22])) + '\n')
		f.write('GPS Attitude:' + str(bin(ba[23])) + str(bin(ba[24])) + str(bin(ba[25])) + str(bin(ba[26])) + str(bin(ba[27])) + '\n')
		f.write('X-axle:' + str(bin(ba[28])) + str(bin(ba[29])) + str(bin(ba[30])) + '\n')
		f.write('Y-axle:' + str(bin(ba[31])) + str(bin(ba[32])) + str(bin(ba[33])) + '\n')
		f.write('Z-axle:' + str(bin(ba[34])) + str(bin(ba[35])) + str(bin(ba[36])) + '\n')
		f.write('Buildingid:' + str(bin(ba[37])) + str(bin(ba[38])) + str(bin(ba[39])) + str(bin(ba[40])) +'\n')
		f.write('Floor:' + str(bin(ba[41])) + str(bin(ba[42])) + str(bin(ba[43])) + str(bin(ba[44])) + str(bin(ba[45])) + str(bin(ba[46])) + str(bin(ba[47])) + str(bin(ba[48])) + str(bin(ba[49])) + str(bin(ba[50])) + str(bin(ba[51])) + str(bin(ba[52])) +'\n')
		f.write('IP:' + str(bin(ba[53])) + str(bin(ba[54])) + str(bin(ba[55])) + str(bin(ba[56])) + '\n')
		f.write('PORT:' + str(bin(ba[57])) + str(bin(ba[58])) + str(bin(ba[59])) + str(bin(ba[60])) + '\n')
		f.write('CRC:' + str(bin(ba[61])) + str(bin(ba[62])) + '\n')
		f.write('\n')
	print 'received...'

udpSerSock.close() 