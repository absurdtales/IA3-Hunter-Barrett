import sqlite3
import os


filename = "userDB.db"
        

conn = sqlite3.connect(filename)
cursor = conn.cursor()

cursor.execute("INSERT INTO")

rows = cursor.fetchall()

for row in rows:
    print(row)
