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

    new_accounts = [
        {
            "account_id": "MDB011235813",
            "account_holder": "Ada Lovelace",
            "account_type": "checking",
            "balance": 60218,
            "last_updated": datetime.datetime.now(datetime.UTC),
        },
        {
            "account_id": "MDB829000001",
            "account_holder": "Muhammad ibn Musa al-Khwarizmi",
            "account_type": "savings",
            "balance": 267914296,
            "last_updated": datetime.datetime.now(datetime.UTC),
        },
        {
            "account_holder": "Bill Gates",
            "account_id": "MDB829000002",
            "account_type": "savings",
            "balance": 100000,
            "last_updated": datetime.datetime.now(datetime.UTC),
        },
        {
            "account_holder": "Tom Sawyer",
            "account_id": "MDB829000002",
            "account_type": "savings",
            "balance": 966,
            "last_updated": datetime.datetime.now(datetime.UTC),
        },
        {
            "account_holder": "Jane Doe",
            "account_id": "MDB829000002",
            "account_type": "savings",
            "balance": 511,
            "last_updated": datetime.datetime.now(datetime.UTC),
        },
    ]


    result = accounts_collection.insert_many(new_accounts)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_id of inserted document: {document_ids}")
    client.close()


if __name__ == "__main__":
    main()
