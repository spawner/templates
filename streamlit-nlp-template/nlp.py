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

#### /question-answer ####
st.header("Question & Answer")
question = st.text_input("Enter a question.")
source_context = st.text_input("Enter the source text. If the answer to your question is in the text the NLP will find it!")
qa_submit_button = st.button("Find Answer")

if qa_submit_button:
    try: 
        response = requests.get("https://spawnerapi.com/answer-question/" + question + "/" + source_context + "/" + api_key)
        st.write(response.json())
    except: 
        st.write("bad query, try another question")

#### /sentiment ####
st.header("Sentiment Analysis")
sentiment_text_entry = st.text_input("Enter your text for sentiment analysis.")
sent_submit_button = st.button("Get Sentiment")

if sent_submit_button:
    try: 
        response = requests.get("https://spawnerapi.com/sentiment/" + sentiment_text_entry + "/" + api_key)
        st.write(response.json())
    except: 
        st.write("bad query, try another question")

#### /understand ####
st.header("Keyword Extraction")
keyword_text_entry = st.text_input("Enter your text for keyword extraction.")
understand_submit_button = st.button("Get Keywords")

if understand_submit_button:
    try: 
        response = requests.get("https://spawnerapi.com/understand/" + keyword_text_entry + "/" + api_key)
        st.write(response.json())
    except: 
        st.write("bad query, try another question")
        
#### /clean ####
st.header("Clean Text")
clean_text_entry = st.text_input("Enter your text for cleaning.")
clean_submit_button = st.button("Clean Text")

if clean_submit_button:
    try: 
        response = requests.get("https://spawnerapi.com/clean/" + clean_text_entry + "/" + api_key)
        st.write(response.json())
    except: 
        st.write("bad query, try another question")

