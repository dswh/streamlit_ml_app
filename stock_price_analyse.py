import pandas as pd
import streamlit as st
import yfinance as yf


st.image("./images/apple_logo.png", width=100)

st.write("""
# Stock Price Analyser

Shown are the Apple stock's *closing prices* and *volume* of Apple!
""")



ticker_symbol = 'AAPL'

ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period='1d', start='2010-01-01', end='2022-01-01')

st.dataframe(ticker_df)

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)


with st.expander("See explanation"):
    st.write("""
        - The chart above shows the Apple stock's closing prices from 2010-2022.
        - It's a line chart and hovering over a particular point will show the details in a tooltip.
        - You can also zoom in and out to play witht the detailing of the chart.
    """)
    st.image("./images/apple.jpeg")