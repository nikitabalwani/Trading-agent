import requests
import pandas as pd
import os
from dotenv import load_dotenv

#load api key

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY or API_KEY == "ADD_YOUR_KEY":
    print("❌ API KEY NOT FOUND or is placeholder. Check your .env file and replace ADD_YOUR_KEY with a valid Alpha Vantage API key.")
    exit()

BASE_URL = "https://www.alphavantage.co/query"
SYMBOL = "BTC"
MARKET = "USD"


#fetch market price

def get_price_data():
    print("Fetching data from Alpha Vantage...")

    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": SYMBOL,
        "market": MARKET,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("❌ HTTP Error:", response.status_code)
        return None

    data = response.json()

    if "Time Series (Digital Currency Daily)" not in data:
        print("❌ API error or rate limit reached")
        print("🔍 Response:", data)
        return None

    prices = data["Time Series (Digital Currency Daily)"]

    df = pd.DataFrame.from_dict(prices, orient="index")
    df.index = pd.to_datetime(df.index)

    close_column = None
    for col in df.columns:
        if "close" in col.lower():
            close_column = col
            break

    if close_column is None:
        print("❌ Close price column not found")
        print("Available columns:", df.columns)
        return None

    df = df[[close_column]]
    df.columns = ["close"]
    df["close"] = df["close"].astype(float)

    return df.sort_index()



def compress_data(df):
    print("Compressing data (last 5 days)...")
    return df.tail(5)



def check_trend(df):
    first_price = df["close"].iloc[0]
    last_price = df["close"].iloc[-1]

    if last_price > first_price:
        return "BUY"
    elif last_price < first_price:
        return "SELL"
    else:
        return "HOLD"



def trade():
    df = get_price_data()

    if df is None:
        print("⚠️ Program stopped due to API issue.")
        return

    small_df = compress_data(df)

    print("\nRecent Prices:")
    print(small_df)

    decision = check_trend(small_df)

    print("\n📈 FINAL DECISION:", decision)



if __name__ == "__main__":
    print("=== Trading Agent Started ===")
    trade()
    print("=== Trading Agent Finished ===")
