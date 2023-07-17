import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passd = ''
)

mycoursur = con.cursor()
mycoursur.execute("CREATE DATABASE hasan ")

