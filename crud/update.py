import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import create_connection

def update_employee(id, name, age, department):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            update_query ='''
            UPDATE employees
            SET name = %s, age = %s, department = %s
            WHERE id = %s;'''
            cursor.execute(update_query,(name, age, department, id))
            conn.commit()
            print("Employee updated successfully")
        except Exception as e:
            print(f"Error updating employee: {e}")
        finally:
            conn.close()
            cursor.close()
# update_employee(101, "Berry", 29, "Engineering")