import streamlit as streamlit
import pandas as pd
import numpy as np

# Load the data from json file
df = pd.read_json('data.json')

st.df(df)

