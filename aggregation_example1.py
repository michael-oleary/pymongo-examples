import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()


def run_pipeline(collection):
    # cursor = collection.find({})
    # for result in cursor:
    #     print('test')
    #     print(result)

    selected_balance = {
        '$match': {
            'balance': {'$lt': 1000}
        }
    }

    cursor = collection.find({
            'balance': {'$lt': 1000}
        })

    for result in cursor:
        print('test')
        print(result)


    seperate_by_account_calculate_avg_balance = {
        '$group': {
            '_id': '$account_type',
            'avg_balance': {'$avg': '$balance'}
        }
    }

    pipeline = [
        selected_balance,
        seperate_by_account_calculate_avg_balance
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