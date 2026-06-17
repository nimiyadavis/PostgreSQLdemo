import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import create_connection

def read_employee(id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            read_query ='''
            SELECT * FROM employees
            WHERE id = %s;'''
            cursor.execute(read_query,(id,))
            employee = cursor.fetchone()
            cursor.close()
            if employee:
                print(f"Employee with ID {id} already exists: {employee}")
            else: 
                print(f"No user found with ID {id}")
        except Exception as e:
            print(f"Error reading employee: {e}")
        finally:
            conn.close()
read_employee(101)