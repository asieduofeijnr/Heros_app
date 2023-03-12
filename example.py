import sqlite3
from matplotlib.pyplot import connect

# Establish a connection and a cursor
connection = sqlite3.connect("heros_data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM Parents WHERE Parent_Last_Name='Agyepong'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Maxwell', 'Arthur', 'maxart@gmail.com', 37467218, '12345'), 
            ('Eunice', 'Arthur', 'eunart@gmail.com', 34567418, '12345')]


cursor.executemany("INSERT INTO Parents VALUES(?,?,?,?,?)", new_rows)
connection.commit()