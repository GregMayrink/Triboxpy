import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image


@st.cache_data
def gerar_df():
    df = pd.read_excel(
        io = "tribox_dados_substrato.xlsx",
        engine= "openpyxl",
        sheet_name= "Plan1",
        usecols= "A:G",
        nrows=100

    )
    return df

df = gerar_df()
colunasUteis = ['box','tratamentos','cliente','data', 'lote', 'var', "valor"]
df = df[colunasUteis]

with st.sidebar:
    st.subheader('TriBox')
    logo = Image.open('favicon (1).ico') 
    st.image(logo, use_column_width=True)
    st.subheader('Filtros')
    fbox = st.multiselect('Box', options=df['box'].unique())
    fcliente = st.multiselect('Cliente', options=df['cliente'].unique())
    flote = st.multiselect('Lote', options=df['lote'].unique())
    fTratamentos = st.multiselect('Tratamentos', options=df['tratamentos'].unique())
    fvar = st.multiselect('var', options=df['var'].unique())

    dadoUsuarios = df.loc[
        (df['box'].isin(fbox)) &
        (df['tratamentos'].isin(fTratamentos)) &
        (df['cliente'].isin( fcliente)) &
        (df['lote'].isin(flote)) &
        (df['var'].isin(fvar))
        ]

   

    nomedoografico = alt.Chart(dadoUsuarios).mark_line().encode(
        x='data:T',
        y='valor:Q',
        color='tratamentos:N',
        strokeWidth=alt.value(3)
    

    
)
st.header('Linha do tempo')
st.markdown(fvar)
st.altair_chart(nomedoografico)