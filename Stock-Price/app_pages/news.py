import streamlit as st
import requests

def show_news_page():
    st.title("Stock News")

    stock_symbol = st.text_input("Enter a stock symbol to get news:")

    if stock_symbol:
        api_key = 'YOUR_NEWSAPI_KEY'
        news_url = f"https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={api_key}"

        response = requests.get(news_url)
        news_data = response.json()

        if news_data['status'] == 'ok':
            for article in news_data['articles'][:5]:
                st.subheader(article['title'])
                st.write(article['description'])
                st.write(f"[Read more]({article['url']})")
