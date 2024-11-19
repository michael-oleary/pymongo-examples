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

    accounts_collection = db.accounts

    new_account = {
        "account_holder": "Linus Torvalds",
        "account_id": "MDB829001337",
        "account_type": "checking",
        "balance": 50352434,
        "last_updated": datetime.datetime.now(datetime.UTC),
    }

    result = accounts_collection.insert_one(new_account)

    document_id = result.inserted_id
    print(f"_id of inserted document: {document_id}")

    client.close()


if __name__ == "__main__":
    main()
