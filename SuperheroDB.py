import sqlite3
import os
import csv
import requests
import shutil
class SuperheroDB():
    
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
        
    
    def create_superhero_db(self):
            """
            Creates the data structure for the superhero database
            """
            # create publisher table
            self.cursor.execute("""
                                CREATE TABLE Publisher(
                                    pub_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL
                                )
                                """)
            
            # create alignment table
            self.cursor.execute("""
                                CREATE TABLE Alignment(
                                    align_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL
                                )
                                """)   
            
            
            # create superhero table
            self.cursor.execute("""
                                CREATE TABLE Superhero(
                                    super_hero_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    intelligence INTEGER,
                                    strength INTEGER,
                                    speed INTEGER,
                                    durability INTEGER,
                                    power INTEGER,
                                    combat INTEGER,
                                    image TEXT NOT NULL,
                                    publisher INTEGER,
                                    alignment INTEGER,
                                    FOREIGN KEY(publisher) REFERENCES Publisher(pub_id),
                                    FOREIGN KEY (alignment) REFERENCES Alignment(align_id)
                                )
                                """)
            
            # create alias id
            self.cursor.execute("""
                                CREATE TABLE Alias(
                                    alias_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL, 
                                    superhero INTEGER,
                                    FOREIGN KEY(superhero) REFERENCES Superhero(superhero_id)                                
                                )
                                """)

create = SuperheroDB()
create.create_superhero_db()
