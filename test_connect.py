from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables
load_dotenv()

DBNAME = os.getenv('DBNAME')
HOST = os.getenv('HOST')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# Connection URI
uri = f"mongodb://{USERNAME}:{PASSWORD}@{HOST}/{DBNAME}"

# Test Connection
try:
    client = MongoClient(uri)
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
