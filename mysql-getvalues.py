import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'paari@123',
    database = 'mydatabase'
)

mycursor = db.cursor()

sql = 'SELECT * FROM customer'

mycursor.execute(sql)

for x in mycursor.fetchall():
    print (x)