# 📈 Simple Trading Agent

A beginner-friendly automated trading agent built using Python.  
This project fetches real cryptocurrency market data, analyzes recent price movements, and generates a basic **BUY / SELL / HOLD** decision.

The goal of this project is to understand how automated trading systems work without using complex machine learning models or advanced strategies.

---

## 🚀 Features
- Fetches real cryptocurrency market data using the **Alpha Vantage API**
- Secure API key handling with **environment variables**
- Lightweight analysis using only recent price data
- Simple and transparent **trend-based trading logic**

---

## 🛠️ Tech Stack
- Python  
- Alpha Vantage API  
- Pandas  
- Requests  
- python-dotenv  

---

## ⚙️ How It Works
1. The program connects to the Alpha Vantage API using an API key  
2. It fetches daily cryptocurrency price data  
3. Only the most recent prices are selected for analysis  
4. The system checks whether the price trend is increasing or decreasing  
5. Based on the trend, a **BUY / SELL / HOLD** decision is displayed  

---

## 🎯 Purpose
This project is designed for learning and educational purposes only.  
It helps beginners understand the basics of:
- Market data fetching  
- Trend analysis  
- Decision-making logic in trading systems  

---

## ⚠️ Disclaimer
This project is **not financial advice** and should not be used for real trading. It is intended only for educational and practice purposes.
