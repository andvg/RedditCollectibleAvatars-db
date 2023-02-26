import pandas as pd
import streamlit as st

with open('database.json') as f:
    data = json.load(f)

df = pd.json_normalize(data['data'])

st.dataframe(df)

filters = st.sidebar.multiselect('Seleziona le colonne', df.columns)
filtered_df = df[filters]
st.dataframe(filtered_df)

chart_type = st.sidebar.selectbox('Seleziona il tipo di grafico', ['line', 'bar', 'area'])

if chart_type == 'line':
    st.line_chart(filtered_df)
elif chart_type == 'bar':
    st.bar_chart(filtered_df)
else:
    st.area_chart(filtered_df)

sort_by = st.sidebar.selectbox('Seleziona la colonna da ordinare', filtered_df.columns)
sort_order = st.sidebar.selectbox('Seleziona l\'ordine', ['crescente', 'decrescente'])

if sort_order == 'crescente':
    sorted_df = filtered_df.sort_values(sort_by)
else:
    sorted_df = filtered_df.sort_values(sort_by, ascending=False)

st.dataframe(sorted_df)

if st.sidebar.button('Esporta in CSV'):
    csv = filtered_df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_data.csv">Download CSV file</a>'
    st.markdown(href, unsafe_allow_html=True)

st.write('Statistiche del dataframe:')
st.write(filtered_df.describe())
