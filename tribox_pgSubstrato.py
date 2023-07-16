import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

 
@st.cache_data
def gerar_df():
    df = pd.read_excel(
        io="tribox_dados_substrato.xlsx",
        engine="openpyxl",
        sheet_name="Plan1",
        usecols="A:G",
        nrows=100 
    )
    return df

df = gerar_df()
colunasUteis = ['box','tratamentos','cliente','data', 'lote', 'var', "valor"]
df = df[colunasUteis]

with st.sidebar:
    st.title('Monitoramento TriBox')
    logo = Image.open('favicon (1).ico') 
    st.image(logo, use_column_width=True)
    st.subheader('Filtros')
    fbox = st.multiselect('BOX', options=df['box'].unique())
    fcliente = st.selectbox('CLIENTE', options=df['cliente'].unique())
    flote = st.selectbox('LOTE', options=df['lote'].unique())
    fTratamentos = st.multiselect('TRATAMENTOS', options=df['tratamentos'].unique())
    fvar = st.multiselect('VARIAVEIS', options=df['var'].unique())
 
    dadoUsuarios = df.loc[
        (df['tratamentos'].isin(fTratamentos)) &
        (df['box'].isin(fbox)) &
        (df['cliente'] == fcliente) &
        (df['lote'] == flote) &
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


