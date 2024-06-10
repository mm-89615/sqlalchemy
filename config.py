import os
from dotenv import load_dotenv

load_dotenv()


def database_url():
    db = os.getenv('DB')
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    return f"{db}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
