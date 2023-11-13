import requests
import creds # Contains credentials (API key) 
import json # To write to json

def main():
    # Using GoldAPI.io to extract yearly gold price data from 01/01/1990 to 01/10/2023
    initial_date = 19900101 # 01/01/1990
    headers = {
    'x-access-token': 'goldapi-1knrlov5z0z8-io'
}

    while initial_date != 20230101:
        api_endpoint = f"https://www.goldapi.io/api/XAU/USD/{initial_date}"
        output_path = f"USA_gold_price/gold_price_data_{initial_date}.json"
        try:
            response = requests.get(api_endpoint,headers=headers)
            response.raise_for_status() # To check if the HTTP request returned a successful status code or not. If the response status code indicates an error (4xx or 5xx), it will raise an HTTPError exception, providing information about the error
        except requests.exceptions.RequestException as e: #It is a convenient way to catch any exception that might occur during the execution of a request
            print(f"Error fetching data for date {initial_date}:{e} ")
            continue
        with open(output_path,"w") as outfile:
            json.dump(response.json(), outfile)
        
        initial_date += 10000 #Incrementing the initial date to get the same date next year 

if __name__ == "__main__":
    main()
