from APIrequest import API
import requests
import json
import sqlite3
import os
reqAPI = API()
class Parse:
    def __init__(self):
            
            """
            initialise datastore
            """
            self.filename = "superheroDB.db"
            
            if not os.path.exists(self.filename):
                # if db is not present create it then connect to it
                self.conn = sqlite3.connect(self.filename)
                self.cursor = self.conn.cursor()
                self.create_superhero_db()
            else:
                # if db is present connect to it
                self.conn = sqlite3.connect(self.filename)
                self.cursor = self.conn.cursor()
    def parse(self, t=0):
        parse=json.loads(requests.get("https://akabab.github.io/superhero-api/api/all.json").text)
        while t <= 20:
            t+=1
            if reqAPI.request(t, parse) != False:
                Aparams = (reqAPI.request(t, parse)[2], t)
                Sparams = (reqAPI.request(t, parse)[1], reqAPI.request(t, parse)[3], reqAPI.request(t, parse)[4], reqAPI.request(t, parse)[5], reqAPI.request(t, parse)[6], reqAPI.request(t, parse)[7], reqAPI.request(t, parse)[8], reqAPI.request(t, parse)[9])
                self.cursor.execute("""
                INSERT INTO Alias (
                    name,
                    superhero
                )
                VALUES (?, ?)
                """, Aparams)
                self.cursor.execute("""
                INSERT INTO Superhero (
                    name,
                    intelligence,
                    strength,
                    speed,
                    durability,
                    power,
                    combat,
                    image
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, Sparams)
                self.conn.commit()
            else:
                t+=1