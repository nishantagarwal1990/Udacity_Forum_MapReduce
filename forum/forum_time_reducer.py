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
		for key,value in sorted(time.iteritems(), key = lambda (k,v): (v,k)):
			if count == 0:
				count = value
				print oldKey, "\t", str(key), "\t", str(value)
			elif value == count:
				print oldKey, "\t", str(key), "\t", str(value)
		oldKey = thisKey
		time = dict()

	oldKey = thisKey
	if thisId not in time.keys():
		time[int(thisId)] = 1
	else:
		time[int(thisId)] += 1

if oldKey != None:
	count = 0
	for key,value in sorted(time.iteritems(), key = lambda (k,v): (v,k)):
		if count == 0:
			count = value
			print oldKey, "\t", str(key), "\t", str(value)
		elif value == count:
			print oldKey, "\t", str(key), "\t", str(value)

