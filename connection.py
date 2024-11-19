import os 
from dotenv import load_dotenv
from pymongo import MongoClient


def main():
    
    load_dotenv()
    
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_options = os.getenv("DB_OPTIONS")

    MONGODB_URI = f"mongodb+srv://{db_user}:{db_pass}@{db_host}/{db_options}"

    print(MONGODB_URI)

    client = MongoClient(MONGODB_URI)

    for db_name in client.list_database_names():
        print(db_name)

    print(MONGODB_URI)

if __name__ == "__main__":
    main()