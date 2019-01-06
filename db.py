import sqlite3
import os

class DB():
    def __init__(self):
        self.connection = sqlite3.connect(self.file_name())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def execute(self, query, *query_args):
        return self.cursor.execute(query, query_args)

    def execute_and_fetch(self, query, *query_args):
        return self.execute(query, *query_args).fetchall()

    def file_name(self):
        env = os.getenv('ENV', 'development')
        file = f"{env}.db"
        return os.path.join(self.app_dir(), 'db', file)

    def app_dir(self):
        return os.path.dirname(os.path.realpath(__file__))
