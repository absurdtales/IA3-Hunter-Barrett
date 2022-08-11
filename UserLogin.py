import sqlite3
import hashlib
class UserGet:
    def __init__(self):
        self.filename = "userDB.db"
        self.conn = sqlite3.connect(self.filename)
        self.cursor = self.conn.cursor()
    def getUsername(self, userName):
        self.cursor.execute("""
                            SELECT email
                            FROM User
                            WHERE email = :name
                            """,
                            {"name":userName}
                            )
    def getPassword(self, passWord):
        self.cursor.execute("""
                            SELECT password
                            FROM User
                            WHERE password = :password
                            """,
                            {"password":passWord}
                            )
class User:
    def __init__(self):
        self.filename = "userDB.db"
        self.conn = sqlite3.connect(self.filename)
        self.cursor = self.conn.cursor()
        self.userGet = UserGet()
    def register(self):
        username = input("Username: ")
        password = str(hashlib.md5(input("Password: ").encode()).hexdigest())
        if (self.userGet.getUsername(username) == None) and (self.userGet.getPassword(password) == None):
            print("Username and Password successfully registered")
            params = (username, password)
            self.cursor.execute(
                """
                INSERT INTO User(
                    email,
                    password,
                    wins,
                    losses
                )
                VALUES (?, ?, 0, 0)
                
                """, params
            )
            self.conn.commit()
        else:
            print("Username and Password already preset in system.")
    def login(self):
        username = input("Username: ")
        password = str(hashlib.md5(input("Password: ").encode()).hexdigest())
        if (self.userGet.getUsername(username) != None) and (self.userGet.getPassword(password) != None):
            return True
        else: 
            return False