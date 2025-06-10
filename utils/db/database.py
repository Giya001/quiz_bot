import os

from dotenv import load_dotenv

load_dotenv()
PG_USER = os.getenv("POSTGRES_USER")
PG_PASSWORD = os.getenv("POSTGRES_PASS")
PG_DATABASE = os.getenv("")