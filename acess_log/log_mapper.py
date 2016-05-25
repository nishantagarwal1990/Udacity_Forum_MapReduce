#!/usr/bin/python

import sys

for line in sys.stdin:
	if "\"GET" in line:
		data = line.strip().split("\"GET")
		method = "GET"
	elif "\"HEAD" in line:
		data = line.strip().split("\"HEAD")
		method = "HEAD"
	elif "\"POST" in line:
		data = line.strip().split("\"POST")
		method = "POST"
	
	meta_access = data[0].strip().split("[")
	meta = meta_access[0].strip().split()
	IP = meta[0]
	identity = meta[1]
	if len(meta) > 3:
		username = " ".join(meta[2:])
	else:
		username = meta[2]

	time_zone = (meta_access[1].strip()[:-1]).split()
	time = time_zone[0]
	zone = time_zone[1]
	path_query = data[1].strip().split()
	pathNquery = " ".join(path_query[:len(path_query)-3])
	#if "?" in pathNquery:
	#	path_query_split = pathNquery.split("?")
	#	path = path_query_split[0]
	#else:
	#	path = pathNquery
	path = pathNquery
	if "http://www.the-associates.co.uk" in path :
		
		if len(path) == len("http://www.the-associates.co.uk"):
			path = "/"
		elif path[0:31] == "http://www.the-associates.co.uk":
			path = path[31:]
		#print path
	
	protocol = path_query[len(path_query)-3][:-1]
	status = path_query[len(path_query)-2]
	size = path_query[len(path_query)-1]
	print "{0}\t{1}".format(path,status)

	'''
	data = line.strip().split()
	IP,identity,username = data[0],data[1],data[2]
	time = data[3][1:]
	zone = data[4][:-1]
	method = data[5][1:]
	path_query = data[6]
	if "?" in path_query:
		path_query_split = path_query.split("?")
		path = path_query[0]
	else:
		path = path_query
	protocol = data[7][:-1]
	status = data[8]
	size = data[9]
	if path == "\"GET":
		print line
	#print "{0}\t{1}".format(path,status)
	'''
