#!/usr/bin/env python

import sys

last_deptno=None
campus=None
dname=None
gpas=[]

lines=sys.stdin.readlines()
for key_value in lines:
	key_value=key_value.strip()
	deptno,value=key_value.split("\t")

	values=value.split(",")
	#print("%s,%s"%(key,value))

	if last_deptno==deptno:
		if values[0]=='student':
			gpas.append(values[1])
		else:
			dname=values[1]
			campus=values[2]
	else:
		if last_deptno and dname and campus and gpas:
			total=0.0
			max_gpa=0.0
			for gpa in gpas:
				total+=float(gpa)
				if float(gpa)>max_gpa:
					max_gpa=float(gpa)
			avg=total/len(gpas)

			if avg>3.5:
				print("%s,%s,%s"%(dname,max_gpa,campus))

		campus=None
		dname=None
		gpas=[]

		if values[0]=='student':
			gpas=[values[1]]
		else:
			dname=values[1]
			campus=values[2]

		last_deptno=deptno
if last_deptno and dname and campus and gpas:
	total=0.0
	max_gpa=0.0
	for gpa in gpas:
		total+=float(gpa)
		if float(gpa)>max_gpa:
			max_gpa=float(gpa)
	avg=total/len(gpas)

	if avg>3.5:
		print("%s,%s,%s"%(dname,max_gpa,campus))
