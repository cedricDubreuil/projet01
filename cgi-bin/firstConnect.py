#!/usr/bin/env python3
import datetime
import mysql.connector

"""
connection = mysql.connector.connect(host='localhost',
                             database='toys_and_models',
                             user='root',
                             password='password', connection_timeout= 180)
"""

connection = mysql.connector.connect(host='toys-and-models.cv4cjezixxdu.us-east-2.rds.amazonaws.com',
                             database='toys_and_models',
                             user='cKlP01p0320',
                             password='lpWcS2k20', connection_timeout= 180)


cursor = connection.cursor()
"""
query = ("SELECT firstName, lastName FROM employees "
             "WHERE reportsTo IS NOT Null")
"""
query = ("SELECT orderdetails.productCode, SUM(orderdetails.quantityOrdered) AS ttlqty "
	"FROM orderdetails "
	"GROUP BY orderdetails.productCode "
	"ORDER BY ttlqty DESC "
	"LIMIT 5")
"""
query = ("SELECT orderdetails.productCode, SUM(orderdetails.quantityOrdered) AS ttlqty "
	"FROM orderdetails "
	"INNER JOIN products "
	"ON orderdetails.productCode = products.productCode "
	"ORDER BY ttlqty ASC "	
	"GROUP BY productCode "
	)
"""
cursor.execute(query)
print("<h2>Produits les plus vendus:</h2>")
print("<br/>")
print("<p style='border:red 1px solid'>")
for (first_name, tr) in cursor:
	print("{} -> {} |</br>".format(first_name, tr))
print("</p>")


cursor.close()
connection.close()
