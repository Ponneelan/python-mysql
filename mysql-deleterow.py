import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="paari@123",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customer WHERE address = 'pudukkottai'"

try:
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

finally:   
    sql1 = 'SELECT * FROM customer'

    mycursor.execute(sql1)

for x in mycursor.fetchall():
    print(x)