import mysql.connector

con = mysql.connector.connect(
    user = "user1",
    password = "qwerASDF12#",
    host = "192.168.254.129",
    database = "mytests",
    auth_plugin='mysql_native_password'
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")