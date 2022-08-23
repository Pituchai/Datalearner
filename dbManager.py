from multiprocessing import connection
import sqlite3 
connection = sqlite3.connect("chinook.db") 
print("Hello") ; 
cursor = 
 connection.execute("SELECT * FROM Customers;")
for row in cursor : 
    print("Customer ID : ", row[0] ) 

