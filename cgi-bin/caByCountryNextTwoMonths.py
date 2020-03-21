#!/usr/bin/env python3
import datetime
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                             database='toys_and_models',
                             user='root',
                             password='password', connection_timeout= 180)

cursor = connection.cursor()

query = ("SELECT customers.country, (priceEach * quantityOrdered) AS turnover "
	"FROM orderdetails "
	"JOIN orders "
	"ON orderdetails.orderNumber = orders.orderNumber "
	"JOIN customers " 
	"ON orders.customerNumber = customers.customerNumber "
	"WHERE MONTH(orders.orderDate) = MONTH(current_date()) - 1 or MONTH(orders.orderDate) = month(current_date()) - 2 "
	"GROUP BY customers.country "
	)

"""
query = ("SELECT orderdetails.orderNumber, orderdetails.priceEach "
	"FROM orderdetails ")

query = ("SELECT firstName, lastName FROM employees ")


query = ("SELECT orderdetails.productCode, SUM(orderdetails.quantityOrdered) AS ttlqty "
	"FROM orderdetails "
	"GROUP BY orderdetails.productCode "
	"ORDER BY ttlqty DESC "
	"LIMIT 5")



query = ("SELECT orderdetails.productCode, SUM(orderdetails.quantityOrdered) AS ttlqty "
	"FROM orderdetails "
	"INNER JOIN products "
	"ON orderdetails.productCode = products.productCode "
	"ORDER BY ttlqty ASC "	
	"GROUP BY productCode "
	)


query = ("SELECT customers.country, (orderdetails.priceEach * orderdetails.quantityOrdered) AS turnover"
	"FROM orderdetails"
	"INNER JOIN orders"
	"ON orderdetails.orderNumber = orders.orderNumber"
	"INNER JOIN customers" 
	"ON orders.customerNumber = customers.customerNumber"
	"WHERE MONTH(orders.orderDate) = MONTH(current_date()) - 1 or MONTH(orders.orderDate) = month(current_date()) - 2"
	"GROUP BY customers.country "
	)
"""
cursor.execute(query)

print("<h2>CA des deux derniers mois:</h2>")
print("<br/>")
print("<p style='border:purple 1px solid'>")
for (country, turnover) in cursor:
	print("{},{}|</br>".format(country, turnover))
print("</p>")



cursor.close()
connection.close()
