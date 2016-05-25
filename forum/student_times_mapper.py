#!/usr/bin/python

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    header = next(reader)

    for line in reader:
        data = line[8].strip().split()
        time = data[1].strip().split(":")
        print "{0}\t{1}".format(line[3],time[0])
        
def main():
    mapper()

main()
