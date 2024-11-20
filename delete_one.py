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


def print_records(collection):
    cursor = accounts_collection.find({})

    num_docs = 0
    for document in cursor: 
        num_docs += 1
        pprint.pp(document)
        print()
    
    print("# of documents found: " + str(num_docs))


def delete_record(collection):

    record_id = input("What record would you like to delete: ")
    print("Searching for target document before deleting: ")
    pprint.pprint(collection.find_one({ "_id": ObjectId(record_id) }))

    delete_record = False
    prompt = input("Are tou happy to delete this record? (y/N): ")

    if prompt == 'Y' or prompt == 'y':
        delete_record = True

        print("Delete Record")
        result = accounts_collection.delete_one(
            { "_id": ObjectId(record_id) })

        print(result)


if __name__ == "__main__":
    MONGO_URI = create_connection()
    client = MongoClient(MONGO_URI)
    db = client.bank
    accounts_collection = db.accounts
    print_records(accounts_collection)
    delete_record(accounts_collection)
    client.close()
