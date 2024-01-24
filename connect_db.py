from dotenv import load_dotenv
import os
from mongoengine import connect, disconnect


class MongoDBConnection:
    def __init__(self):
        load_dotenv()
        self.db_name = os.getenv('DBNAME')
        self.host = os.getenv('HOST')
        self.username = os.getenv('USER_NAME')
        self.password = os.getenv('PASSWORD')
        self.connected = False

    def open_connection(self):
        connect(
            db=self.db_name,
            host=self.host,
            username=self.username,
            password=self.password
        )

    def close_connection(self):
        if self.connected:
            disconnect()
            self.connected = False
            print("Disconnected from MongoDB.")
        else:
            print("No active MongoDB connection to close.")

    def is_connected(self):
        return self.connected
