
from crud import create_table, delete,insert, read, update 

def main():
    create_table.create_table()
    insert.insert_employee(101, 'John Doe', 30, 'Engineering')
    insert.insert_employee(102, 'Jane Smith', 25, 'Marketing')  
    insert.insert_employee(103, 'Alice Johnson', 28, 'HR')
    read.read_employee(101)
    update.update_employee(101, "Berry", 29, "Engineering")
    delete.delete_employee(102)
    
if __name__ == "__main__":
    main()