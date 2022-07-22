import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="paari@123",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customer SET address = 'kuthalam' WHERE name = 'abinash'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")