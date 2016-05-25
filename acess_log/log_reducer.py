#!/usr/bin/python

import sys

hit_count = 0
oldKey = None



for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisStatus = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hit_count
        hit_count = 0

    oldKey = thisKey
    #if float(thisStatus) == 200:
    hit_count += 1

if oldKey != None:
    print oldKey, "\t", hit_count