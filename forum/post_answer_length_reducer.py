#!/usr/bin/python

import sys


oldKey = None
q_len = 0
ans_len = 0
count = 0

print "Question Node ID | Question Length | Average Answer Length"

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 3:
		continue
	
	thisKey, thisId, thisLen = data_mapped

	if oldKey and oldKey != thisKey:
		if count != 0:
			print "{0}\t\t\t{1}\t\t\t{2}".format(oldKey, q_len, str(ans_len/float(count)))
		else:
			print "{0}\t\t\t{1}\t\t\t{2}".format(oldKey, q_len, "0")
		oldKey = thisKey
		time = dict()
		count = 0
		ans_len = 0

	oldKey = thisKey
	if thisId == "Q":
		q_len = thisLen
	else:
		ans_len += int(thisLen)
		count += 1

if oldKey != None:
	if count != 0:
		print "{0}\t\t\t{1}\t\t\t{2}".format(oldKey, q_len, str(ans_len/float(count)))
	else:
		print "{0}\t\t\t{1}\t\t\t{2}".format(oldKey, q_len, "0")

