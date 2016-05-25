#!/usr/bin/python

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    header = next(reader)

    for line in reader:
        if line[5] == "question":
        	print "{0}\t{1}\t{2}".format(line[0],"Q",str(len(line[4])))
        elif line[5] == "answer":
        	print "{0}\t{1}\t{2}".format(line[6],"A",str(len(line[4])))
        
def main():
    mapper()

main()
