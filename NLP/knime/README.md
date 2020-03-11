# Streamlit Demo

Streamlit demo for using the Spawner.AI API for finance. You can use Streamlit to create interactive Data Science pages, deployable to the web through all major deployment surfaces. 

![Current State](https://user-images.githubusercontent.com/33185528/74096257-7ed5a000-4aca-11ea-9d92-0369ba728b86.png)

## Getting Started

If you need an API key you can get it from [Spawner](https://spawner.ai)

Using a python3 environment, run the following to install all the libraries used in this repository:
```
pip install -r requirements.txt
```
Recommend using conda or virtualenv to sandbox your work

### Manual Install 
If you go the manual route instead of requirements we recommend using [Anaconda](https://www.anaconda.com/distribution/). 
```
pip install streamlit pandas numpy pillow urllib requests
```

For additional information on Streamlit: [Docs](https://streamlit.io/docs/)

### Running Streamlit App
From command line navigate to your application's directory and use:
```
streamlit run finance_streamlit.py
```



