import streamlit as st
import pandas as pd 
import requests 
import urllib.request


#### Sidebar ####
st.sidebar.header("Spawner NLP Demo")
api_key = st.sidebar.text_input("Input API Key to get started.")
st.sidebar.info("Welcome to the Spawner NLP demo. We built this demo for explaining some of our core NLP endpoints.")
st.sidebar.info("If you need an API key visit: https://spawner.ai")

#### Main Page ####
st.title("Spawner + Streamlit = <3")

#### /sentiment ####
st.header("Sentiment Analysis")
sentiment_text_entry = st.text_input("Enter your text for sentiment analysis.")
sent_submit_button = st.button("Get Sentiment")

if sent_submit_button:
    try: 
        url = 'https://spawnerapi.com/sentiment/' + token
        data = {'text': sentiment_text_entry}
        headers = {'Content-type': 'application/json'}

        x = requests.post(url, data=json.dumps(data), headers=headers)
        st.write(x.text)
    except: 
        st.write("bad query, try another question")

#### /understand ####
st.header("Keyword Extraction")
keyword_text_entry = st.text_input("Enter your text for keyword extraction.")
understand_submit_button = st.button("Get Keywords")

if understand_submit_button:
    try: 
        url = 'https://spawnerapi.com/understand/' + token
        data = {'text': keyword_text_entry}
        headers = {'Content-type': 'application/json'}

        x = requests.post(url, data=json.dumps(data), headers=headers)
        st.write(x.text)
    except: 
        st.write("bad query, try another question")
        
#### /clean ####
st.header("Clean Text")
clean_text_entry = st.text_input("Enter your text for cleaning.")
clean_submit_button = st.button("Clean Text")

if clean_submit_button:
    try: 
        url = 'https://spawnerapi.com/clean/' + token
        data = {'text': clean_text_entry}
        headers = {'Content-type': 'application/json'}

        x = requests.post(url, data=json.dumps(data), headers=headers)
        st.write(x.text)
    except: 
        st.write("bad query, try another question")

