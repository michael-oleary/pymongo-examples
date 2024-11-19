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

    # selection filter
    document_to_find = {"account_type": "savings" }

    set_file = { "$set": { "minimum_balance": 200 }}

    results = accounts_collection.update_many(document_to_find, set_file)

    print(f"_id of modified field count: {results.modified_count}")
    print(f"_id of modified field count: {results.modified_count}")

    client.close()


if __name__ == "__main__":
    main()
