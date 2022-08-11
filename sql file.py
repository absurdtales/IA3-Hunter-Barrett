import sqlite3
import os


filename = "superheroDB.db"
        

conn = sqlite3.connect(filename)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Superhero")

rows = cursor.fetchall()

for row in rows:
    print(row)
