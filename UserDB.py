import sqlite3
import os
class UserDB:
    def __init__(self):
            
            """
            initialise datastore
            """
            self.filename = "userDB.db"
            
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
        # create superhero table
        self.cursor.execute("""
                            CREATE TABLE User(
                                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                email TEXT NOT NULL,
                                password TEXT NOT NULL,
                                wins INTEGER,
                                losses INTEGER
                            )
                            """)


userDB = UserDB()
userDB.create_superhero_db