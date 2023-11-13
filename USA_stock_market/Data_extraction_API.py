import requests
import creds # Contains credentials (API key) 
import json # To write to json

# Ticker symbol for Russel 3000 index
tckr_symbol = 'RUA'

# Using TwelveData API to extract DJIA data
def main():
    api_endpoint = f'https://api.twelvedata.com/time_series?&start_date=1990-01-01&end_date=2023-11-01&symbol={tckr_symbol}&interval=1month&apikey={creds.api_key}'
    #interval = 30 days
    try:
        response = requests.get(api_endpoint).json()
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data:{e} ")
    with open("USA_stock_market/stock_data.json", "w") as outfile:
        outfile.write(json.dumps(response))

if __name__ == "__main__":
    main()