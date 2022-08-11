from APIrequest import API
import requests
import json
import sqlite3
import os
reqAPI = API()
class parsing:
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
    def parsing(self, t=0):
        # get json data and transform into text
        parsing = json.loads(requests.get("https://akabab.github.io/superhero-api/api/all.json").text)
        # continue this loop for 20 entries
        while t <= 20:
            t+=1
            if reqAPI.request(t, parsing) != False:
                # set alias table parameters as text lines from API
                AliasParameters = (reqAPI.request(t, parsing)[2], t)
                # set superhero table parameters as text lines from API
                SuperheroParameters = (reqAPI.request(t, parsing)[1], reqAPI.request(t, parsing)[3], reqAPI.request(t, parsing)[4], reqAPI.request(t, parsing)[5], reqAPI.request(t, parsing)[6], reqAPI.request(t, parsing)[7], reqAPI.request(t, parsing)[8], reqAPI.request(t, parsing)[9])
                # insert parameters into alias database
                self.cursor.execute("""
                INSERT INTO Alias (
                    name,
                    superhero
                )
                VALUES (?, ?)
                """, AliasParameters)
                # insert parameters into superhero database
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
                """, SuperheroParameters)
                self.conn.commit()
            else:
                t+=1