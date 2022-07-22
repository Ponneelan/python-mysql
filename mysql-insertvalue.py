import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'paari@123',
    database = 'mydatabase'
)

mycursor = db.cursor()

sql = 'INSERT INTO customer (name,address) VALUES(%s,%s)'
val = ('vasanth','pudukkottai') 

mycursor.execute(sql,val)
db.commit()

print(mycursor)