import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Cargar los datos desde el repositorio de GitHub
url = "https://raw.githubusercontent.com/Taidded/Proyecto/refs/heads/main/Datos_proyecto_modificado.csv"
data = pd.read_csv(url)

# Cálculo de los ratios
data['Liquidity_Ratio'] = data['Current_Assets'] / data['Current_Liabilities']
data['Debt_to_Equity_Ratio'] = (data['Short_Term_Debt'] +
                                data['Long_Term_Debt']) / data['Equity']
data['Financial_Coverage'] = data['Total_Revenue'] / data['Financial_Expenses']


# Función para filtrar datos
def filter_data(industry, country, company_size):
    filtered_data = data
    if industry != "All":
        filtered_data = filtered_data[filtered_data['Industry'] == industry]
    if country != "All":
        filtered_data = filtered_data[filtered_data['Country'] == country]
    if company_size != "All":
        filtered_data = filtered_data[filtered_data['Company_Size'] ==
                                      company_size]
    return filtered_data


# Títulos de las opciones de filtro
industries = ['All'] + data['Industry'].unique().tolist()
countries = ['All'] + data['Country'].unique().tolist()
company_sizes = ['All'] + data['Company_Size'].unique().tolist()

# Seleccionar filtros
selected_industry = st.selectbox('Selecciona la Industria:', industries)
selected_country = st.selectbox('Selecciona el País:', countries)
selected_company_size = st.selectbox('Selecciona el Tamaño de la Empresa:',
                                     company_sizes)

# Filtrar los datos
filtered_data = filter_data(selected_industry, selected_country,
                            selected_company_size)

# Gráfico de barras para Ratio de Liquidez
st.header('Ratio de Liquidez')
liquidity_bar_fig = px.bar(filtered_data,
                           x='Company_ID',
                           y='Liquidity_Ratio',
                           title='Ratio de Liquidez (Barras)',
                           labels={'Liquidity_Ratio': 'Ratio de Liquidez'})
st.plotly_chart(liquidity_bar_fig)

# Gráfico de líneas para Ratio de Liquidez
liquidity_line_fig = px.line(filtered_data,
                             x='Company_ID',
                             y='Liquidity_Ratio',
                             title='Ratio de Liquidez (Líneas)',
                             labels={'Liquidity_Ratio': 'Ratio de Liquidez'})
st.plotly_chart(liquidity_line_fig)

# Gráfico de círculo para Ratio de Liquidez
liquidity_circle_fig = px.pie(filtered_data,
                              names='Company_ID',
                              values='Liquidity_Ratio',
                              title='Ratio de Liquidez (Círculos)')
st.plotly_chart(liquidity_circle_fig)

# Gráfico de barras para Ratio de Deuda a Patrimonio
st.header('Ratio de Deuda a Patrimonio')
debt_to_equity_bar_fig = px.bar(
    filtered_data,
    x='Company_ID',
    y='Debt_to_Equity_Ratio',
    title='Ratio de Deuda a Patrimonio (Barras)',
    labels={'Debt_to_Equity_Ratio': 'Ratio de Deuda a Patrimonio'})
st.plotly_chart(debt_to_equity_bar_fig)

# Gráfico de líneas para Ratio de Deuda a Patrimonio
debt_to_equity_line_fig = px.line(
    filtered_data,
    x='Company_ID',
    y='Debt_to_Equity_Ratio',
    title='Ratio de Deuda a Patrimonio (Líneas)',
    labels={'Debt_to_Equity_Ratio': 'Ratio de Deuda a Patrimonio'})
st.plotly_chart(debt_to_equity_line_fig)

# Gráfico de círculo para Ratio de Deuda a Patrimonio
debt_to_equity_circle_fig = px.pie(
    filtered_data,
    names='Company_ID',
    values='Debt_to_Equity_Ratio',
    title='Ratio de Deuda a Patrimonio (Círculos)')
st.plotly_chart(debt_to_equity_circle_fig)

# Gráfico de barras para Cobertura de Gastos Financieros
st.header('Cobertura de Gastos Financieros')
financial_coverage_bar_fig = px.bar(
    filtered_data,
    x='Company_ID',
    y='Financial_Coverage',
    title='Cobertura de Gastos Financieros (Barras)',
    labels={'Financial_Coverage': 'Cobertura de Gastos Financieros'})
st.plotly_chart(financial_coverage_bar_fig)

# Gráfico de líneas para Cobertura de Gastos Financieros
financial_coverage_line_fig = px.line(
    filtered_data,
    x='Company_ID',
    y='Financial_Coverage',
    title='Cobertura de Gastos Financieros (Líneas)',
    labels={'Financial_Coverage': 'Cobertura de Gastos Financieros'})
st.plotly_chart(financial_coverage_line_fig)

# Gráfico de círculo para Cobertura de Gastos Financieros
financial_coverage_circle_fig = px.pie(
    filtered_data,
    names='Company_ID',
    values='Financial_Coverage',
    title='Cobertura de Gastos Financieros (Círculos)')
st.plotly_chart(financial_coverage_circle_fig)

# Comparar Ratios por Company_ID
st.header('Comparación de estadísticas entre dos Compañías')

company_id_1 = st.selectbox('Selecciona la primera Company_ID:',
                            data['Company_ID'].unique())
company_id_2 = st.selectbox('Selecciona la segunda Company_ID:',
                            data['Company_ID'].unique())

st.header('Ratio de Liquidez Corriente')
if company_id_1 != company_id_2:
    liquidity_comparison = data[data['Company_ID'].isin(
        [company_id_1, company_id_2])][['Company_ID', 'Liquidity_Ratio']]
    st.table(liquidity_comparison)

st.header('Ratio de Deuda a Patrimonio')
if company_id_1 != company_id_2:
    debt_equity_comparison = data[data['Company_ID'].isin(
        [company_id_1, company_id_2])][['Company_ID', 'Debt_to_Equity_Ratio']]
    st.table(debt_equity_comparison)

st.header('Cobertura de Gastos Financieros')
if company_id_1 != company_id_2:
    financial_coverage_comparison = data[data['Company_ID'].isin(
        [company_id_1, company_id_2])][['Company_ID', 'Financial_Coverage']]
    st.table(financial_coverage_comparison)
