import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
        )
        if mydb.is_connected():
            query = mydb.cursor()
            query.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully")
    except Error as e:
        print(f"Error is {e}")

    finally:
        if mydb.is_connected():
            mydb.close()
            query.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()



