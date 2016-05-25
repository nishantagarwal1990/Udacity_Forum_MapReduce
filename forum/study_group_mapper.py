#!/usr/bin/python

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    header = next(reader)
    
    for line in reader:
        if line[5] == "question":
        	print "{0}\t{1}".format(line[0],line[3])
        elif line[5] == "answer":
            print "{0}\t{1}".format(line[6],line[3])
        elif line[5] == "comment":
            print "{0}\t{1}".format(line[6],line[3])

def main():
    mapper()

main()
