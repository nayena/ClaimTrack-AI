import sqlite3

def init_db():
    conn = sqlite3.connect("eduai.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            subjects TEXT
        )
    """)
    conn.commit()
    conn.close()