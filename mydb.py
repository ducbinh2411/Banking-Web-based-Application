#install Mysql in your computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import pymysql

dataBase = pymysql.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'S5takara'

	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a databse
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")