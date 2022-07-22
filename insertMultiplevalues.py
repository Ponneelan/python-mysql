import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'paari@123',
    database = 'mydatabase'
)

mycursor = db.cursor()

sql = 'INSERT INTO customer (name,address) VALUES(%s,%s)'
val = [
    ('ponneelan','pudukkottai'),
    ('loganathan','villupuram'),
    ('abinash','mayiladhuthurai')
] 

mycursor.executemany(sql,val)
db.commit()

print(mycursor)