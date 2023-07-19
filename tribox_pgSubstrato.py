import pandas as pd
import streamlit as st

def import_xls_file():
    file = st.file_uploader("tribox_dados_substrato.xlsx", type=["xls"])
    if file is not None:
        try:
            df = pd.read_excel(file)
            return df
        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}")
    
    return None

# Aplicação Streamlit
st.title("Importar arquivo .xls para DataFrame")
df = import_xls_file()
if df is not None:
    st.write("Dados importados:")
    st.write(df)
