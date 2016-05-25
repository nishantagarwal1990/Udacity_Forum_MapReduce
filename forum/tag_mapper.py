#!/usr/bin/python

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    header = next(reader)
    tag_dict = dict()
    for line in reader:
        if line[5] == "question":
        	tags = line[2].strip().split()
        	for tag in tags:
        		if tag not in tag_dict.keys():
        			tag_dict[tag] = 1
        		else:
        			tag_dict[tag] += 1
    count = 0
    for key,value in sorted(tag_dict.items(), key = lambda (k,v):(v,k), reverse = True):
        print "{0}\t{1}".format(key,str(value))
        count += 1
        if count >= 10:
        	break

def main():
    mapper()

main()
