<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/apachehadoop-66CCFF?style=flat&logo=apachehadoop&logoColor=white"/>
# Simple-MapReduce
This repository contains two simple MapReduce framework projects that are from SKKU's 2021 spring Introduction to Database course. Projects uses Hadoop streaming whith Python.
# proj1: Implementing SQL statement using MapReduce
Assuming that there are two tables(student, dept) in database. This project is an implementation of the following SQL statement as MapReduce framework.
'''(sql)
SELECT d.dname, max(s.gpa), d.campus
FROM student s
JOIN dept d ON s.deptno = d.deptno
GROUP BY d.dname
HAVING avg(s.gpa) > 3.5;
'''
## Mapper
When using Dept data, deptno is key, and table name(dept), dname, and campus are values.
