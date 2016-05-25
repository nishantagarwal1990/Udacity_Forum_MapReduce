#!/usr/bin/python

import sys


oldKey = None
l = list()


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	thisKey, thisId = data_mapped

	if oldKey and oldKey != thisKey:
		#l.sort()
		#s = str(l).strip('[]')
		print oldKey, "\t", str(len(l)), "\t", l
		oldKey = thisKey
		l = list()

	oldKey = thisKey
	if thisId not in l:
		l.append(int(thisId))

if oldKey != None:
	#l.sort()
	#s = str(l).strip('[]')
	print oldKey, "\t", str(len(l)), "\t", l

