import streamlit as st
import pandas as pd


def main():
    
    st.set_page_config(page_title="AprioriRH Faturamento",
                    page_icon="https://apriorirh.com.br/wp-content/uploads/2024/04/cropped-fav-priori-32x32.png",
                    layout="wide"
                    )

    st.title("Apriori Faturamento:")
    st.logo("external/Logo.png")

    # Nome do arquivo Excel
    excel_leandro = "planilhas/Planilha de Faturamento - Leandro.xlsx"

    # Ler todas as planilhas a partir da linha 8
    file = pd.read_excel(excel_leandro, sheet_name=None, skiprows=7)

    # Lista de meses disponíveis
    meses = list(file.keys())
    meses.insert(0, "Todos os meses")

    # Seleção do mês
    mes_selecionado = st.selectbox("Selecione o mês", meses)

    # Caixa de inserção de texto para o filtro
    filtro = st.text_input("Digite o termo para filtrar")

    # Função para exibir dados com filtros
    def exibir_dados(df, filtro):
        if df.empty:
            st.write("Nenhum dado disponível para exibir.")
            return

        # Aplicar filtro em todas as colunas
        df_filtrado = df[df.apply(lambda row: row.astype(str).str.contains(filtro, case=False).any(), axis=1)]
        st.dataframe(df_filtrado)

    # Exibir dados do mês selecionado ou de todos os meses
    if mes_selecionado == "Todos os meses":
        # Concatenar todos os DataFrames
        df_todos_meses = pd.concat(file.values(), ignore_index=True)
        st.subheader("Todos os meses")
        exibir_dados(df_todos_meses, filtro)
        
    else:
        df = file[mes_selecionado]
        st.subheader(f"Mês: {mes_selecionado}")
        exibir_dados(df, filtro)

        
if __name__ == "__main__":
    main()