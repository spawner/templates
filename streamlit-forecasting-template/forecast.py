import streamlit as st
import pandas as pd 
import requests 
import urllib.request


#### Sidebar ####
st.sidebar.header("Spawner Forecasting Demo")
api_key = st.sidebar.text_input("Input API Key to get started.")
st.sidebar.info("Welcome to the Spawner Forecasting demo. We built this demo for explaining some of our core Forecasting endpoints.")
st.sidebar.info("If you need an API key visit: https://spawner.ai")

#### Main Page ####
st.title("Spawner + Forecasting = <3")

#### /forecast ####
st.header("Demand Forecasting")

st.write("Displaying first 5 rows...")
df = pd.read_csv('data/shampoo_orders.csv', nrows=5)
st.dataframe(df)

prior_forecast = st.text_input("Enter a prior set of inputs.")
forecast_submit_button = st.button("Forecast")

if forecast_submit_button:
    try: 
        response = requests.get("http://127.0.0.1:5000/forecast/" + prior_forecast + "/" + api_key)
        st.write(response.json())
    except: 
        st.write("bad query, try another question")


