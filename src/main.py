import mysql.connector
from src.db.models import initialize_db
from src.cli.interface import start_interface

def main():
    # Initialize the database connection
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='*',
        database='app'
    )
    
    # Initialize the database schema
    initialize_db(conn)
    
    # Start the text-based interface
    start_interface(conn)

if __name__ == '__main__':
    main()