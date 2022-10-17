from optparse import Values
import mysql.connector as mysql

class db:
    mydb= mysql.connect(
        host='127.0.0.1',
        user='root',
        password='Rajith1234@',
        database='test'
    )

    mycursor = mydb.cursor()

    # print(db)

    #cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    #cursor.execute("SHOW TABLES")
    # for tables in cursor:
    #     print(tables)

    # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # val = ("John", "Highway 21")
    # cursor.execute(sql, val)
    # db.commit()

    # mycursor.execute("SELECT * FROM customers")
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

    # mycursor.execute("SELECT name, address FROM customers")
    # myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)

    #only print the first result of the row
    # mycursor.execute("SELECT * FROM customers")
    # myresult = mycursor.fetchone()
    # print(myresult)

    # sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
    # mycursor.execute(sql)
    # myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)

    # sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
    # mycursor.execute(sql)
    # mydb.commit()
    # print(mycursor.rowcount, "record(s) deleted")

    # sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    # mycursor.execute(sql)
    # mydb.commit()
    # print(mycursor.rowcount, "record(s) affected")

