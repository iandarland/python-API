import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    database="testdatabase"
)

mycursor = db.cursor()


# mycursor.execute("CREATE TABLE User (name VARCHAR(50), age smallint UNSIGNED, userID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("INSERT INTO User (name, age) VALUES (%s,%s)", ("Joe", 33))
# this saves our above command to the database and ensures that it stays 
db.commit()


mycursor.execute("SELECT * FROM USER")

for x in mycursor:
    print(x)