import streamlit as st
import pandas as pd
import numpy as np
import json

with open('data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['data'])

st.title("Analisi del database JSON")

# Mostra la tabella dei dati
st.write(df)
