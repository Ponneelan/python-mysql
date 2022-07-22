import mysql.connector

db = mysql.connector.connect(
    host = 'lcalhost',
    user = 'root',
    password = 'paari@123',
    database = 'mydatabase'
)

mycursor = db.cursor()
print(mycursor)