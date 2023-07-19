import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# Load data function
@st.cache_data
def import_xls_file():
    file = st.file_uploader("tribox_dados_substrato.xlsx", type=["xls", "xlsx"])
    if file is not None:
        try:
            df = pd.read_excel(file)
            return df
        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}")
    return None

# Sidebar
st.sidebar.title('Monitoramento TriBox')
logo = Image.open('favicon (1).ico') 
st.sidebar.image(logo, use_column_width=True)
st.sidebar.subheader('Filtros')

# Load data
df = import_xls_file()

if df is not None:
    # Filtering options
    fbox = st.sidebar.multiselect('BOX', options=df['box'].unique())
    fcliente = st.sidebar.selectbox('CLIENTE', options=df['cliente'].unique())
    flote = st.sidebar.selectbox('LOTE', options=df['lote'].unique())
    ftratamentos = st.sidebar.multiselect('TRATAMENTOS', options=df['tratamentos'].unique())
    fvar = st.sidebar.multiselect('VARIAVEIS', options=df['var'].unique())

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
        st.markdown(f"**Variáveis selecionadas:** {', '.join(fvar)}")
        st.altair_chart(chart)
    else:
        st.warning('Nenhum dado encontrado! Selecione os filtros.')
else:
    st.warning('Nenhum arquivo carregado! Faça o upload de um arquivo Excel.')
