# transform.py
from datetime import datetime

def transform_data(raw_data):
    transformed = []
    for coin, info in raw_data.items():
        price = info['usd']
        timestamp = datetime.fromtimestamp(info['last_updated_at']).isoformat()
        transformed.append({
            'coin': coin,
            'price_usd': price,
            'timestamp': timestamp
        })
    return transformed
