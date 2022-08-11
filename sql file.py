import sqlite3
import os
# connect to database
filename = "superheroDB.db"
# create cursor
conn = sqlite3.connect(filename)
cursor = conn.cursor()
# execute sql query
cursor.execute("SELECT * FROM Superhero")

rows = cursor.fetchall()
# print results in rows
for row in rows:
    print(row)
