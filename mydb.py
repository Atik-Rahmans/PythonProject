# Install Mysql on my computer
# https://dev.mysql.com/download/installer/
# pip install mysql
# pip install mysql-connector 
# pip install mysql-connector-python

import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '28A@77R=ar'
   )
# prepare a cursor object
cursorObject = dataBase.cursor()

#create.a.databade
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")