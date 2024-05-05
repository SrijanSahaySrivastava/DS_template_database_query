import os
import uvicorn
import sqlite3

PORT = 8000
HOST = "0.0.0.0"


def create_database_if_not_exists():
    if not os.path.exists("database.db"):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (name TEXT, id INTEGER)")
        conn.commit()
        conn.close()


if __name__ == "__main__":
    create_database_if_not_exists()
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)
