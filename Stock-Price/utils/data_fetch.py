import yfinance as yf
import requests

def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1y")

def fetch_stock_news(symbol, api_key):
    news_url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={api_key}"
    response = requests.get(news_url)
    return response.json()
