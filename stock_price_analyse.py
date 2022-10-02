import pandas as pd
import streamlit as st
import yfinance as yf
import datetime


st.image("./images/apple_logo.png", width=100)

st.write("""

# Stock Price Analyser

Shown are the Apple Stock's **closing prices** and **volume of shares** traded.

""")


ticker_symbol = "AAPL"


## date filter
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Input starting date", datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input("Input ending date", datetime.date(2019, 7, 6))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start=f"{start_date}", end=f"{end_date}")

## showcasing dataframes
st.dataframe(ticker_df)


## showcasing charts
st.write("""
## Daily closing price chart
""")
st.line_chart(ticker_df.Close)

st.write("""
## Volume of shares traded
""")
st.line_chart(ticker_df.Volume)

with st.expander("See explanation"):
    st.write("""
        - The chart above shows the Apple stock's closing prices from 2010-2022.
        - It's a line chart and hovering over a particular point will show the details in a tooltip.
        - You can also zoom in and out to play witht the detailing of the chart.
    """)
    st.image("./images/apple.jpeg", width = 50)