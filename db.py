import psycopg2
from psycopg2 import sql, OperationalError
from dotenv import load_dotenv
import os
load_dotenv()
import psycopg2.extras

conn = None

# Function to connect to the PostgreSQL database
def create_connection():
    try:
        conn = psycopg2.connect(
            host = os.getenv("HOST"),
            port = os.getenv("PORT"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            database = os.getenv("DATABASE")
        )
        print("Connection to PostgreSQL database successful")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None 
    
# conn = create_connection()