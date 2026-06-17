import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import create_connection

def delete_employee(id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            delete_query ='''
            DELETE FROM employees
            WHERE id = %s;'''
            cursor.execute(delete_query,(id,))
            conn.commit()
            print("Employee deleted successfully")
        except Exception as e:
            print(f"Error deleting employee: {e}")
        finally:
            conn.close()
            cursor.close()
delete_employee(102)