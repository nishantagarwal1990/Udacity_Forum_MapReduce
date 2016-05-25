#!/usr/bin/python

import sys


oldKey = None
time = dict()


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	thisKey, thisId = data_mapped

	if oldKey and oldKey != thisKey:
		count = 0
		l = list()
		for key,value in sorted(time.items(), key = lambda (k,v): (v,k), reverse = True):
			if count == 0:
				count = value
				l.append(key)
				
			elif value == count:
				l.append(key)
				
		l.sort()
		for k in l:
			print oldKey, "\t", str(k)

		oldKey = thisKey
		time = dict()

	oldKey = thisKey
	if int(thisId) not in time.keys():
		time[int(thisId)] = 1
	else:
		time[int(thisId)] += 1

if oldKey != None:
	count = 0
	l = list()
	for key,value in sorted(time.items(), key = lambda (k,v): (v,k), reverse = True):
		if count == 0:
			count = value
			l.append(key)
			
		elif value == count:
			l.append(key)

	l.sort()
	for k in l:
		print oldKey, "\t", str(k)

