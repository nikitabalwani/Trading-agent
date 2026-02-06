
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ADD_API_KEY")
SYMBOL = os.getenv("SYMBOL")

BASE_URL = "https://www.alphavantage.co/query"
