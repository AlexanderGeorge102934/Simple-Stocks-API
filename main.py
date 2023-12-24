import requests
import time 

#Change ticker to what you want
ticker = "MSFT"

#Go to twelvedata.com, make an account and use the api key and have it set to api_key
api_key = ""

def getStockPrice(ticker_symbol, api):
    try:
        url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        price = data.get('price', 'N/A')[:-3]
        return price
    except requests.RequestException as e:
        print(f"Error fetching stock price: {e}")
        return None

def getStockQuote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response

name = getStockQuote(ticker, api_key)['name']
stockPrice = getStockPrice(ticker, api_key)

print (name, stockPrice)

