import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Thres,1fi!",
    database="projectdb"
)
# Showing all function put into mycursor.execute

# "CREATE DATADASE projectdb"
# "CREATE TABLE lunchmenu (item VARCHAR(255), price INTEGER(10))"
# sqlFormula = "INSERT INTO lunchmenu (item, price) VALUES (%s,%s)
# mycursor.executemany(sqlFormula, lunchitems)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS test")
mydb.commit()




