import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db = os.getenv('DB_NAME')

connection = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db
)

if connection.is_connected():
    print(f"Successfully connected to the {db} database")
    connection.close()