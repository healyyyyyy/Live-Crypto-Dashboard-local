# load.py
import sqlite3

def load_data(data, db_path='crypto_data.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS crypto_prices (
        coin TEXT,
        price_usd REAL,
        timestamp TEXT
    )''')

    for entry in data:
        c.execute('INSERT INTO crypto_prices VALUES (?, ?, ?)', 
                  (entry['coin'], entry['price_usd'], entry['timestamp']))

    conn.commit()
    conn.close()
