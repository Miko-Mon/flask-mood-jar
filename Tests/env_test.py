from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db = os.getenv('DB_NAME')
sk = os.getenv('SECRET_KEY')

print(type(db_host), db_host)
print(type(db_user), db_user)
print(type(db_password), db_password)
print(type(db), db)
print(type(sk), sk)