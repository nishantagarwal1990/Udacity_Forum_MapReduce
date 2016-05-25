#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv



def reducer():

    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    oldKey = None
    listA = list()
    listB = list()

    for line in sys.stdin:
        
        # YOUR CODE HERE
        data_mapped = line.strip().split("\t")
        
        if oldKey and oldKey != data_mapped[0]:
            comb_list = listA+listB
            writer.writerow(comb_list)
            listA = list()
            listB = list()
        
        oldKey = data_mapped[0]
        if data_mapped[1] == "A":
            listA = data_mapped[2:]
        else:
            listB = data_mapped[2:]
    
    if oldKey != None:
        comb_list = listA+listB
        writer.writerow(comb_list)

if __name__ == "__main__":
    reducer()