import sqlite3

class Database:
    def __init__(self, db_uri):
        self.conn = sqlite3.connect(db_uri)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            data BLOB
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_data(self, data):
        query = 'INSERT INTO sensor_data (data) VALUES (?)'
        self.conn.execute(query, (data,))
        self.conn.commit()

    def close(self):
        self.conn.close()