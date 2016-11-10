#!/usr/bin/env python
# -*- coding: utf-8 -*

file = raw_input('Please input inputFile name:')
file2 = raw_input('Please input outputFile name:')
with open(file, 'r') as f:
	s = f.read()
	n = len(s) / 126
with open(file2, 'a') as f2:
	for j in range(n):
		k = j * 126
		f2.write('Type:' + s[0+k: 2+k] + '\n')
		f2.write('Length:' + str(int(s[2+k: 6+k], 16)) + '\n')
		f2.write('MT ID:' + s[6+k: 8+k])
		for i in range(4, 9):
			f2.write('-' + s[i*2+k: i*2+2+k])
		f2.write('\n')
		f2.write('Sequence ID:' + str(int(s[18+k: 26+k], 16)) + '\n')
		f2.write('Gps Longitude:')
		for i in range(13, 18):
			f2.write(s[i*2+k: i*2+2+k] + ' ')
		f2.write('\n')
		f2.write('Gps Latitude:')
		for i in range(18, 23):
			f2.write(s[i*2+k: i*2+2+k] + ' ')
		f2.write('\n')
		f2.write('Gps Attitude:')
		for i in range(23, 28):
			f2.write(s[i*2+k: i*2+2+k] + ' ')
		f2.write('\n')
		f2.write('X-axle:')
		for i in range(28, 31):
			f2.write(s[i*2+k: i*2+2+k] + ' ')
		f2.write('\n')
		f2.write('Y-axle:')
		for i in range(31, 34):
			f2.write(s[i*2+k: i*2+2+k] + ' ')
		f2.write('\n')
		f2.write('Z-axle:')
		for i in range(34, 37):
			f2.write(s[i*2+k: i*2+2+k] + ' ')
		f2.write('\n')
		f2.write('Buildingid:' + str(int(s[74+k: 82+k], 16)) +'\n')
		f2.write('Floor:')
		for i in range(41, 53):
			f2.write(s[i*2+k: i*2+2+k] + ' ')
		f2.write('\n')
		f2.write('IP:' + str(int(s[106+k: 108+k], 16)) + '.' + str(int(s[108+k: 110+k], 16)) + '.' + str(int(s[110+k: 112+k], 16)) + '.' + str(int(s[112+k: 114+k], 16)) + '\n')
		f2.write('PORT:' + str(int(s[112+k: 120+k], 16)) + '\n')
		f2.write('CRC:' + s[120+k: 122+k] + ' ' + s[122+k: 124+k] + '\n')
		f2.write('\n')