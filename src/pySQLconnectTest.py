# -*- coding: utf-8 -*-
#!/usr/bin/python3

import mysql.connector as database
from config import *

# set the database connector
connection = database.connect(
	user = dbLoginUser,
	password = dbLoginPassword,
	host = dbHostURL
)

cursor = connection.cursor(dictionary = True)

cursor.execute("SHOW DATABASES")
return_all_db = cursor.fetchall()

connection.close()

# print all found databases
for row in return_all_db:
	print (row['Database'])
