import mysql.connector

database =mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='harddy/09109'
)

#prepare cursor object
cursorObject = database.cursor()

#create database
cursorObject.execute('CREATE DATABASE db1')

print("all done")