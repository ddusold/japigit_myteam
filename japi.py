import urllib.request
import json


def main():
    user_input = input("Enter a stock symbol: ")
    while (user_input != "quit"):
        print("The current price of " + user_input +  " is: $" + getStockData(user_input))
        user_input = input("Enter another stock symbol: ")


def getStockData(ticker):
    api_key = "M649LU6ARZFQXM4U"
    url = "https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=" + ticker + "&apikey=" + api_key
    connection = urllib.request.urlopen(url)
    response = connection.read().decode()
    python_response = json.loads(str(response))
    current_price = python_response['Stock Quotes'][0]['2. price']
    return current_price

main()
    
