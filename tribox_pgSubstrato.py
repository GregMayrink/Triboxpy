import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import openpyxl as abrir

# Load data function
@st.cache_data
def main():
    df = pd.read_excel(tribox_dados_substrato.xlsx)
    return df

# Load data
df = main()

# Sidebar
with st.sidebar:
    st.title('Monitoramento TriBox')
    logo = Image.open('favicon (1).ico') 
    st.image(logo, use_column_width=True)
    st.subheader('Filtros')

    # Filtering options
    fbox = st.multiselect('BOX', options=df['box'].unique())
    fcliente = st.selectbox('CLIENTE', options=df['cliente'].unique())
    flote = st.selectbox('LOTE', options=df['lote'].unique())
    ftratamentos = st.multiselect('TRATAMENTOS', options=df['tratamentos'].unique())
    fvar = st.multiselect('VARIAVEIS', options=df['var'].unique())

# Apply filters
filtered_data = df.loc[
    (df['box'].isin(fbox)) &
    (df['cliente'] == fcliente) &
    (df['lote'] == flote) &
    (df['tratamentos'].isin(ftratamentos)) &
    (df['var'].isin(fvar))
]

# Line chart
if not filtered_data.empty:
    chart = alt.Chart(filtered_data).mark_line().encode(
        x='data:T',
        y='valor:Q',
        color='tratamentos:N',
        strokeWidth=alt.value(3)
    )
    st.header('Linha do tempo')
    st.markdown(fvar)
    st.altair_chart(chart)
else:
    st.warning('Nenhum dado encontrado com os filtros selecionados.')
