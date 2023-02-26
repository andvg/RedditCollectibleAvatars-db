import streamlit as st
import pandas as pd
import numpy as np
import json

with open('data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['data'])

# spacchetta le colonne che contengono liste
df = pd.concat([df.drop(['tags'], axis=1), df['tags'].apply(pd.Series)], axis=1)

st.title("Analisi del database JSON")
st.multiselect("Seleziona le colonne da visualizzare", df.columns)

# Mostra la tabella dei dati
st.dataframe(df)
