import sqlite3

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        if not self.tables_exist(conn):
            self.create_tables(conn)
        return conn

    def tables_exist(self, conn):
        cursor = conn.cursor()
        required_tables = ['user','message']
        existing_tables = []
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for row in cursor.fetchall():
            existing_tables.append(row[0])
        for table in required_tables:
            if table not in existing_tables:
                return False
        return True

    def create_tables(self, conn):
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            userid INTEGER NOT NULL,
            register DATETIME NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS message (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            key TEXT NOT NULL,
            userid INTEGER NOT NULL,
            register DATETIME NOT NULL
        )
        ''')
        conn.commit()
        cursor.close()
