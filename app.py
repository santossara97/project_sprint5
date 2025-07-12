import pandas as pd
import plotly.express as px
import streamlit as st

vehicles_data = pd.read_csv('vehicles_clear.csv') #open df

st.title('Visualização de dados dos veículos')

# Cria as caixas de seleção
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

# Mostra o histograma se selecionado
if build_histogram:
    fig_hist_odometer = px.histogram(vehicles_data, x='odometer', nbins=10, title='Histograma do odometer')
    st.plotly_chart(fig_hist_odometer)

# Mostra o gráfico de dispersão se selecionado
if build_scatter:
    fig_scatter_odometer_vs_price = px.scatter(vehicles_data, x='odometer', y='price', title='Dispersão odometer vs price')
    st.plotly_chart(fig_scatter_odometer_vs_price)
