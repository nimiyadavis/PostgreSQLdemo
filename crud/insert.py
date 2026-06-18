
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import create_connection

def insert_employee(id, name, age, department):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            insert_query ='''
            INSERT INTO employees(id, name, age, department)
            VALUES(%s, %s, %s, %s);'''
            cursor.execute(insert_query,(id, name, age, department))
            conn.commit()
            print("Employee inserted successfully")
        except Exception as e:
            print(f"Error inserting employee: {e}")
        finally:
            cursor.close()
            conn.close()

# insert_employee(101, 'John Doe', 30, 'Engineering')
# insert_employee(102, 'Jane Smith', 25, 'Marketing')
# insert_employee(103, 'Alice Johnson', 28, 'HR')