import sqlite3
import os

class DB():
    def __init__(self):
        self.connection = sqlite3.connect(self.file_name())
        self.cursor = self.connection.cursor()

    def execute(self, query):
        return self.cursor.execute(query)

    def execute_and_fetch(self, query):
        return self.execute(query).fetchall()

    def __del__(self):
        self.connection.close()

    def file_name(self):
        env = os.getenv('ENV', 'development')
        file = f"{env}.db"
        return os.path.join(self.app_dir(), 'db', file)

    def app_dir(self):
        return os.path.dirname(os.path.realpath(__file__))
