import os
import pprint
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

    document_to_find = {"_id": ObjectId("673d0caf8d4d4faf3ee2b270") }

    add_to_balance = { "$inc": { "balance": 1000 }}


    pprint.pprint(accounts_collection.find_one(document_to_find))

    result = accounts_collection.update_one(
        document_to_find, 
        add_to_balance)

    print(f"_id of modified field count: {result.modified_count}")

    client.close()


if __name__ == "__main__":
    main()
