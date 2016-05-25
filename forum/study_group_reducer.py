#!/usr/bin/python

import sys


oldKey = None
sort_list = list()


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	thisKey, thisId = data_mapped

	if oldKey and oldKey != thisKey:
		sort_list.sort()
		print "{0}\t{1}".format(oldKey,str(sort_list))
		oldKey = thisKey
		sort_list = list()

	oldKey = thisKey
	sort_list.append(int(thisId))

if oldKey != None:
	sort_list.sort()
	print "{0}\t{1}".format(oldKey,str(sort_list))
