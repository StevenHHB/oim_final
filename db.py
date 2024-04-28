import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.close()


def add_entry(text, sentiment, score, date):
    conn = get_db_connection()
    conn.execute('INSERT INTO entries (text, sentiment, score, date) VALUES (?, ?, ?, ?)',
                 (text, sentiment, score, date))
    conn.commit()
    conn.close()


def get_entries():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM entries').fetchall()
    conn.close()
    return entries
