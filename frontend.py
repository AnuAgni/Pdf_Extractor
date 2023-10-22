import streamlit as st
import urllib.parse
from urllib.parse import unquote
import requests
import json
import pandas as pd

st.title("Pdf Extractor")
url=st.text_input("Enter Url")
encoded_url = urllib.parse.quote(url, safe='')
request_url=f"http://127.0.0.1:8000/pdf/{encoded_url}"


if st.button("Result"):
    response=requests.get(request_url)
    ans=response.json()
    df=pd.DataFrame(ans)
    st.dataframe(df)

