import os
import datetime

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId

load_dotenv()

def create_connection():
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_options = os.getenv("DB_OPTIONS")
    MONGODB_URI = f"mongodb+srv://{db_user}:{db_pass}@{db_host}/{db_options}"
    return MONGODB_URI

def main():
    MONGO_URI = create_connection()
    client = MongoClient(MONGO_URI)
    db = client.bank

    accounts_collection = db.accounts

    document_to_find = { "_id": ObjectId("673d0cf1ad1716fe0a0aee72")}

    result = accounts_collection.find_one(document_to_find)

    print(result)

    client.close()


if __name__ == "__main__":
    main()
