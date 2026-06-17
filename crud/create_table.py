import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import create_connection

def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL,
                department VARCHAR(50));'''
            cursor.execute(create_table_query)
            conn.commit()
            print("Table 'employees' created successfully")
        except Exception as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()
            conn.close()
            

    create_table()