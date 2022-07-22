import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'paari@123'
)

print(db)

mycursor = db.cursor()
print(mycursor)

#mycursor.execute("CREATE DATABASE mydatabase")

print(mycursor)

mycursor.execute('SHOW DATABASES')

print(mycursor)

for i in mycursor:
    print(i)