import streamlit as st
import yfinance as yf
import pandas as pd

def show_stock_analysis_page():
    st.title("Stock Analysis")

    stock_symbol = st.text_input("Enter a stock symbol (e.g., AAPL, GOOG):")

    if stock_symbol:
        # Fetch stock data using yfinance
        stock_data = yf.Ticker(stock_symbol)
        df = stock_data.history(period="1d")

        # Display stock data
        st.write(f"Showing data for {stock_symbol}")
        st.dataframe(df)

        # Plot stock prices
        st.line_chart(df['Close'])
