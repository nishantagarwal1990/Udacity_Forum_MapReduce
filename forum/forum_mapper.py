#!/usr/bin/python

import sys
import csv
import re


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    #writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    header = next(reader)

    for line in reader:
        #print line
        data = re.split(r"\.|,|\!|\?|\:|;|\"|\(|\)|\<|\>|\[|\]|\#|\$|\=|-|/|\s",line[4])
        #data = re.split(r"(\W+)",line[4])
        for d in data:
            if d and not d.isdigit() and len(d) > 5:
                print "{0}\t{1}".format(d.lower(),line[0])
        
        

def main():
    mapper()

main()
