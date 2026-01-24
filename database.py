import sqlite3
import os 
class Database:
    def __init__(self,db_name="FENR.DB"):
        project_folder = os.path.dirname(os.path.abspath(__file__))
        self.db_name = os.path.join(project_folder,db_name)
        self.conn = None
        self.cursor = None
        self.connect()
    
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name,check_same_thread=False)
            self.cursor = self.conn.cursor()
            print("connection successfull")
        except sqlite3.Error as e:
            print(f"connection error {e}")
            raise   
    
    def close(self):
        if self.conn :
            self.conn.close()
            print("close connection")