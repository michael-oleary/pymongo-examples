import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()


def run_pipeline(collection):


    selected_accounts = { 
        "$match": { 
            "account_type": "checking",
            "balance": {"$gt": 1500} 
        }
    }

    conversion_rate = 1.3

    organized_by_balance = {
        "$sort": {
            "balance": -1
        }
    }

    return_specific_fields = {
        "$project": {
            "_id": 0,
            "account_type": 1,
            "balance": 1,
            "converted_balance": {"$divide": ["$balance", conversion_rate]}
        }
    }

    pipeline = [
        selected_accounts,
        organized_by_balance,
        return_specific_fields
    ]
    
    print("Aggregation Pipeline: ")
    result = collection.aggregate(pipeline)

    print("Result: ")
    for document in result:
        pprint.pp(document)


def create_connection():
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_options = os.getenv("DB_OPTIONS")
    MONGODB_URI = f"mongodb+srv://{db_user}:{db_pass}@{db_host}/{db_options}"
    return MONGODB_URI


if __name__ == "__main__":
    MONGO_URI = create_connection()
    client = MongoClient(MONGO_URI)
    db = client.bank
    accounts_collection = db.accounts
    run_pipeline(accounts_collection)
    client.close()