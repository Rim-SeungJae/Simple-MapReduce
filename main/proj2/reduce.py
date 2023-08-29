#!/usr/bin/env python

import sys
lines=sys.stdin.readlines()
for key_value in lines:
	key_value=key_value.strip()
	key,value=key_value.split("\t")

	price,dist=value.split(",")
	price=int(price)
	dist=int(dist)
	#print("%s,%s"%(key,value))

	is_Dom=True

	for inner_key_value in lines:
		inner_key_value=inner_key_value.strip()
		inner_key,inner_value=inner_key_value.split("\t")

		inner_price,inner_dist=inner_value.split(",")
		inner_price=int(inner_price)
		inner_dist=int(inner_dist)

		if inner_price<=price and inner_dist<=dist:
			if inner_price<price or inner_dist<dist:
				is_Dom=False
	
	if is_Dom:
		print("%s"%(key))
