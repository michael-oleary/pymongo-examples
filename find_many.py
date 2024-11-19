import os
import datetime
import pprint

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

    documents_to_find = { "balance": { "$gte": 0 }}

    cursor = accounts_collection.find({})

    num_docs = 0
    for document in cursor: 
        num_docs += 1
        pprint.pp(document)
        print()
    
    print("# of documents found: " + str(num_docs))
    client.close()


if __name__ == "__main__":
    main()






