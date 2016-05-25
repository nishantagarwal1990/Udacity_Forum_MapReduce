#!/usr/bin/python

import sys


oldKey = None
count = 0
sort_list = list()
tup = ()


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	thisKey, thisId = data_mapped

	if oldKey and oldKey != thisKey:
		tup = (oldKey,count)
		sort_list.append(tup)
		tup = ()
		if len(sort_list) > 10:
			sort_list.sort(key= lambda t : t[1],reverse = True)
			sort_list = sort_list[:10]
		else:
			sort_list.sort(key= lambda t : t[1],reverse = True)
		oldKey = thisKey
		count = 0

	oldKey = thisKey
	count += int(thisId)

if oldKey != None:
	tup = (oldKey,count)
	sort_list.append(tup)
	tup = ()
	if len(sort_list) > 10:
		sort_list.sort(key= lambda t : t[1],reverse = True)
		sort_list = sort_list[:10]
	else:
		sort_list.sort(key= lambda t : t[1],reverse = True)

for key,value in sort_list:
	print "{0}\t{1}".format(key,str(value))
