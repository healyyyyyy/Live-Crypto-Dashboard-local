# extract.py
import requests

def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum',
        'vs_currencies': 'usd',
        'include_last_updated_at': 'true'
    }
    response = requests.get(url, params=params)
    print (response.json())
    return response.json()
