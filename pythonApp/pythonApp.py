import pyodbc
import sys

try:
    connection = pyodbc.connect('Driver={SQL Server};Server=VPALAGUMMIPC;Database=class;Trusted_Connection=yes;')
    cursor = connection.cursor()
    print "Successfully connected"
    SQLCommand = "exec InsertData @Name = 'Minni',@Age=21,@Branch='CSE',@Gender='F'"
    cursor.execute(SQLCommand)
    cursor.close()
    connection.commit()
    connection.close() 
except:
    print "Unexpected error"
