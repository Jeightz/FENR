from database import Database
import sqlite3
import json
class models():
    def __init__(self):
        self.db = Database()
        self.createtable()
        self.autodeletekey()

    def checkTableExcist(self):
        try:
            self.db.cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='DATA';")
            result = self.db.cursor.fetchone()
            if result:
                return True
            else:
                return False
        except sqlite3.Error as e:
            print("unsuccessfuly to check the table to excist")
            
    def createtable(self):
        try:
            if self.checkTableExcist():
                print("table is excist")
                return None
            self.db.cursor.execute("""
            CREATE TABLE DATA (
                KEY TEXT PRIMARY KEY,
                VALUE TEXT,
                EXPIRES_AT DATE DEFAULT (DATE('now', '+1 day'))
            )
            """)
            self.db.conn.commit()
            
        except sqlite3.Error as e:
            print(f"Error to create the table {e}")
            return None
        except sqlite3.IntegrityError:
            return None
        
    def findkey(self,key):  
        try:
            self.db.cursor.execute("SELECT VALUE FROM DATA WHERE KEY=?;",(key,))
            result = self.db.cursor.fetchone()
            if result:
                try:
                    return json.loads(result[0])
                except json.JSONDecodeError as e:
                    print(f"error to convert to json {e}")
            else :
                return False
        except sqlite3.Error as e:
            return False
               
    def addkeyvalue(self,key,value):
        try:
            self.db.cursor.execute("INSERT INTO DATA (KEY,VALUE) VALUES (?,?);",(key,value))
            self.db.conn.commit()
            print("yawa successfully")
        except sqlite3.Error as e:
            print(f"Unsuccessful insert of data {e}")
            return False  
        except sqlite3.IntegrityError:
            print("unsuccessfull insert of data ")
            return False
        
        
    def deletekey(self ,key):
        try:
            self.db.cursor.execute("DELETE FROM DATA WHERE KEY=?;",(key,))
            self.db.conn.commit()
            return 
        except sqlite3.IntegrityError as s:
            print(f"error to delete the data {s}")
            return None
    
    
    def autodeletekey(self):
        try:
            print('checking data if there is an expire data')
            self.db.cursor.execute("DELETE FROM DATA WHERE EXPIRES_AT <= Date('now') ;")
            self.db.conn.commit()
            deleted_count = self.db.cursor.rowcount
            if deleted_count > 0:
                print(f"deleted {deleted_count} expired entries")
        except sqlite3.IntegrityError as s:
            print(f"error to delete the data {s}")
            return None
    