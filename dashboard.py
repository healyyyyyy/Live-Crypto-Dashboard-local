# dashboard.py
import sqlite3
import pandas as pd
import streamlit as st

def load_from_db():
    conn = sqlite3.connect('crypto_data.db')
    df = pd.read_sql_query("SELECT * FROM crypto_prices", conn)
    conn.close()
    return df

st.title("📊 Live Crypto Price Tracker")
df = load_from_db()
df_deduped = df.drop_duplicates(subset=['timestamp', 'coin'])
pivoted = df_deduped.pivot(index='timestamp', columns='coin', values='price_usd')
st.line_chart(pivoted)

