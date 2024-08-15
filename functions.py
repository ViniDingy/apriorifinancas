import streamlit as st
import pandas as pd 
import openpyxl
import plotly.graph_objects as go

#---------Código de Inicialização---------#

def extrac_excel(funcionario):
    funcionarios = [
        "carolina",
        "flavio",
        "josianne",
        "kalley",
        "leandro",
        "mari",
        "rita"
    ]

    for i in funcionarios:
        excel = "planilhas/Planilha de Faturamento - {i}.xlsx"
        df = pd.read_excel(excel)