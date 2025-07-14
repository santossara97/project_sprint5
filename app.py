# Bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

vehicles_data = pd.read_csv('C:/Users/Acer/project_sprint5/vehicles_clear.csv') #open df

st.title('Visualização de dados dos veículos')

# Cria as caixas de seleção
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

# Mostra o histograma se selecionado
if build_histogram:
    st.subheader("📊 Histograma Interativo")
    hist_legivel = st.selectbox("Escolha a variável para o eixo X", numeric_cols_legiveis, index=numeric_cols_legiveis.index("Dias para Venda"))
    hist_col = coluna_original(hist_legivel)
    bins = st.slider("Número de faixas (bins)", min_value=10, max_value=100, value=40)

    hist_fig = px.histogram(
        vehicles_data,
        x=hist_col,
        nbins=bins,
        labels={hist_col: hist_legivel}
    )

    hist_fig.update_layout(
        title=f"Distribuição de {hist_legivel}",
        title_font_size=20,
        title_x=0,
        xaxis_title=hist_legivel,
        yaxis_title="Frequência",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        height=500
    )

    hist_fig.update_traces(
        marker_color='green',
        marker_line_color='black',
        marker_line_width=1,
        opacity=0.8
    )

    st.plotly_chart(hist_fig)
    st.markdown("---")

# Gráfico de Dispersão Interativo
if build_scatter:
    fig_scatter_odometer_vs_price = px.scatter(vehicles_data, x='odometer', y='price', title='Dispersão odometer vs price')
    st.plotly_chart(fig_scatter_odometer_vs_price)