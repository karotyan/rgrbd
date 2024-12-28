# db_connection.py
import psycopg
from db_config import DB_CONFIG

def get_connection():
    try:
        conn = psycopg.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None
