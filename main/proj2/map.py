#!/usr/bin/env python

import sys

for line in sys.stdin:
	line=line.strip()
	tuple_list=line.split(",")

	price=tuple_list[1]
	dist=tuple_list[2]
	rest_name=tuple_list[0]
	print('{0}\t{1}'.format(rest_name,price+','+dist))

