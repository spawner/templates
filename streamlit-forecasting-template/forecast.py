import streamlit as st
import pandas as pd 
import requests 
import urllib.request
import json
import plotly.graph_objects as go


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
df = pd.read_csv('data/uni_shipments.csv', nrows=5)
st.dataframe(df)

periods = st.text_input("Enter number of periods to predict.")
forecast_submit_button = st.button("Forecast")

if forecast_submit_button:
    full_df = pd.read_csv('data/uni_shipments.csv')
    dates = full_df['Date'].values.tolist()
    sales = full_df['Sales'].values.tolist()

    prior_dates = ','.join(dates)
    prior_sales = ','.join(str(x) for x in sales)

    st.success("Forecasting...")
    response = requests.get("http://127.0.0.1:5000/forecast/" + prior_dates + "/" + prior_sales + "/" + periods + "/" + api_key)
    response_text = json.loads(response.text)

    date = []
    prediction = []
    lower_bound = []
    upper_bound = []
    for i in response_text:
        date.append(i['date'])
        prediction.append(i['prediction'])
        lower_bound.append(i['lower_bound'])
        upper_bound.append(i['upper_bound'])


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=date, y=prediction, name="Prediction",
                            line_color='blue'))

    fig.add_trace(go.Scatter(x=date, y=lower_bound, name="Lower Bound",
                            line_color='green'))

    fig.add_trace(go.Scatter(x=date, y=upper_bound, name="Upper Bound",
                            line_color='red'))

    fig.layout.update(title_text='Forecasting Demo', xaxis_rangeslider_visible=True)

    st.plotly_chart(fig)


