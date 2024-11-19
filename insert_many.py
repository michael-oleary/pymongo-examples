import os
import datetime

from dotenv import load_dotenv
from pymongo import MongoClient

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

    account_collection = db.accounts

    new_accounts = [
        {
            "account_holder": "Linus Torvalds",
            "account_id": "XXXXXXXXXXXX",
            "account_type": "checking",
            "balance": 503524,
            "last_updated": datetime.datetime.now(datetime.UTC),
        },
        {
            "account_holder": "Bill Gates",
            "account_id": "YYYYYYYYYYYY",
            "account_type": "checking",
            "balance": 100000,
            "last_updated": datetime.datetime.now(datetime.UTC),
        },
        {
            "account_holder": "Bill Gates",
            "account_id": "ZZZZZZZZZZZZ",
            "account_type": "savings",
            "balance": 100000,
            "last_updated": datetime.datetime.now(datetime.UTC),
        },
    ]


    result = account_collection.insert_many(new_accounts)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_id of inserted document: {document_ids}")
    client.close()


if __name__ == "__main__":
    main()