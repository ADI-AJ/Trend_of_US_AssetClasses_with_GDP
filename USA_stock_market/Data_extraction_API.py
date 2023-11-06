import requests
import creds # Contains credentials (API key) 
import json # To write to json

# Ticker symbol for Russel 3000 index
tckr_symbol = 'RUA'

# Using TwelveData API to extract DJIA data

url = f'https://api.twelvedata.com/time_series?&start_date=1990-01-01&end_date=2023-11-01&symbol={tckr_symbol}&interval=1month&apikey={creds.api_key}'
#interval = 30 days
response = requests.get(url).json()
with open("USA_stock_market/stock_data.json", "w") as outfile:
    outfile.write(json.dumps(response))
