import streamlit as st 
import pandas as pd 
import json 
import numpy as np 
import urllib.request
from PIL import Image
import requests 
import plotly.graph_objects as go


#### Sidebar ####
st.sidebar.header("Spawner Finance Demo")
token = st.sidebar.text_input("Input API Key to get started.")
st.sidebar.info("Welcome to the Spawner finance demo. We built this demo for explaining some of our core financial endpoints.")
st.sidebar.info("If you need an API key visit: https://spawner.ai")

#### Main Page ####
st.title("Spawner.AI Trading Dashboard")

#### /answer ####
st.header("Financial Data Miner - uses /answer endpoint")
financial_question = st.text_input("Enter a stock, question about a stock, or question about a market.")
submit_button = st.button("Ask")

if submit_button:
    try: 
        url = 'https://spawnerapi.com/answer/' + token
        data = {'text': financial_question}
        headers = {'Content-type': 'application/json'}
        x = requests.post(url, data=json.dumps(data), headers=headers)
        result = json.loads(x.text)
        for i in result:
            st.write(i['text']) 
    except: 
        st.write("bad query, try another question")

#### /fundamentals ####
st.header("ML-driven trading signal - uses /fundamentals endpoint")
fundamentals_submit_button = st.button("Get Ratings")

if fundamentals_submit_button: 
    try: 
        url = "https://spawnerapi.com/fundamentals/" + token
        response = requests.get(url)
        result = response.json()
        st.success("S&P 500 ratings sorted by ticker.")
        st.write(result)
    except: 
        st.write("bad token or out of messages")


#### /portfolio ####
st.header("Portfolio optimizer - uses /portfolio endpoint")
portfolio_tickers = st.text_input("Enter the name of a company, stock ticker, or multiple companies/tickers.")
submit_button2 = st.button("Optimize")
if submit_button2: 
    response = requests.get("https://spawnerapi.com/portfolio/" + portfolio_tickers + "/" + token)
    st.write(response.json())

#### /backtest ####
st.header("Stock Backtester - uses /backtest endpoint")
backtest_tickers = st.text_input("Enter the ticker, company name, or multiple companies/tickers. (Ex: ge, aapl)")

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
st.subheader("Start Date (Year-Month-Day)")
start_year = st.slider("Pick the start year for your test.", min_value=1970, max_value=2020)
start_month = st.slider("Pick the start month for your test.", min_value=1, max_value=12)
start_day = st.slider("Pick the start day for your test.", min_value=1, max_value=31)
st.subheader("End Date (Year-Month-Day)")
end_year = st.slider("Pick the end year for your test.", min_value=1970, max_value=2020)
end_month = st.slider("Pick the end month for your test.", min_value=1, max_value=12)
end_day = st.slider("Pick the end day for your test.", min_value=1, max_value=31)

start = str(start_year) + "-" + str(start_month) + "-" + str(start_day)
end = str(end_year) + "-" + str(end_month) + "-" + str(end_day)
st.write("run backtest for " + start  + " to " + end)
submit_button2 = st.button("Backtest")
if submit_button2: 
    #try:
    response = requests.get("https://spawnerapi.com/backtest/" + str(start) + "/" + str(end) + "/" + backtest_tickers + "/" + token)
    st.write(response.json())
    #except:
        #st.write("bad date range or tickers")
        

