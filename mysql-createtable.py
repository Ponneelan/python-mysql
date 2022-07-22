import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'paari@123',
    database = 'mydatabase'
)

mycursor = db.cursor()
print(mycursor)

mycursor.execute("CREATE TABLE STUDENT (name VARCHAR(255),regno INT(15))")

print(mycursor)




