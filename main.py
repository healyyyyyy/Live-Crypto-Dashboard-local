# main.py
import time
from extract import fetch_crypto_data
from transform import transform_data
from load import load_data

def run_pipeline():
    raw = fetch_crypto_data()
    cleaned = transform_data(raw)
    load_data(cleaned)
    print("ETL run complete.")

if __name__ == '__main__':
    while True:
        try:
            run_pipeline()
            time.sleep(120)  # Wait 5 minutes
        except Exception as e:
            print("Error during ETL run:", e)
            time.sleep(60)  # Wait 1 minute before retrying