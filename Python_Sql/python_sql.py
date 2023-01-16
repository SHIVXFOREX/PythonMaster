import mysql.connector
  
mydb = mysql.connector.connect(
  host="156.67.222.169",
  user="u733493607_pythondb",
  password="python@3NGINE",
)

print(mydb) 

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='156.67.222.169',
                                         database='u733493607_pythondb',
                                         user='u733493607_pythondb',
                                         password='python@3NGINE')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        sql = "INSERT INTO shiv (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        cursor.execute(sql, val)

        mydb.commit()

        print(cursor.rowcount, "record inserted.")

        cursor.execute("SELECT * FROM shiv")

        myresult = cursor.fetchall()

        for x in myresult:
          print(x)
        