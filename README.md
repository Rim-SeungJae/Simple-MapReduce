<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/apachehadoop-66CCFF?style=flat&logo=apachehadoop&logoColor=white"/>
# Simple-MapReduce
This repository contains two simple MapReduce framework projects that are from SKKU's 2021 spring Introduction to Database course. Projects uses Hadoop streaming whith Python.
# proj1: Implementing SQL statement using MapReduce
Assuming that there are two tables(student, dept) in database. This project is an implementation of the following SQL statement as MapReduce framework.
'''sql
SELECT d.dname, max(s.gpa), d.campus
FROM student s
JOIN dept d ON s.deptno = d.deptno
GROUP BY d.dname
HAVING avg(s.gpa) > 3.5;
'''
## Mapper
When using Dept data, deptno is key, and table name(dept), dname, and campus are values.
![db1](https://github.com/dipreez/Simple-MapReduce/assets/50349104/4cc5ed44-1ee0-4aae-ad84-a1745d7a1bf8)
When using Student data, deptno is key, and table name(student) and gpa are values.
![db2](https://github.com/dipreez/Simple-MapReduce/assets/50349104/8e3effc7-4483-4ac0-b7e3-dc4949cd30ff)
## Reducer
Match dname, campus with gpa. Use For loop to access each key, value pair. Calculates the average gpa and
maximum gpa for a group with the same dname. Only if the average gpa is over 3.5 will the reducer output
![db3](https://github.com/dipreez/Simple-MapReduce/assets/50349104/1b76937c-bd52-4d4d-bc00-cbbe04b8e0c3)
# proj2: Finding dominant set
Given example data below, this project finds dominant set of tuples.
![db4](https://github.com/dipreez/Simple-MapReduce/assets/50349104/29b5676d-eb97-421f-99f9-b2d3dc010537)
## Mapper
