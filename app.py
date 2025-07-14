# Bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar dados
vehicles_data = pd.read_csv('vehicles_clear.csv')

# Garantir que 'model_year' seja categórica
vehicles_data['model_year'] = vehicles_data['model_year'].astype(str)

# Identificar colunas numéricas e categóricas
numeric_cols = vehicles_data.select_dtypes(include='number').columns.tolist()
categorical_cols = vehicles_data.select_dtypes(include='object').columns.tolist()

# Dicionário de tradução das colunas
nomes_colunas = {
    "price": "Preço (R$)",
    "odometer": "Quilometragem (km)",
    "days_listed": "Dias para Venda",
    "model_year": "Ano de Fabricação",
    "cylinders": "Número de Cilindros",
    "is_4wd": "Tração 4x4",
    "paint_color": "Cor do Veículo",
    "condition": "Condição"
}

# Funções de tradução
def traduzir_coluna(nome_tecnico):
    return nomes_colunas.get(nome_tecnico, nome_tecnico)

def coluna_original(nome_legivel):
    inverso = {v: k for k, v in nomes_colunas.items()}
    return inverso.get(nome_legivel, nome_legivel)

# Listas de colunas traduzidas
numeric_cols_legiveis = [traduzir_coluna(col) for col in numeric_cols]
categorical_cols_legiveis = [traduzir_coluna(col) for col in categorical_cols]

# Título da página
st.title('📊 Visual Analytics Interativo: Mercado de Veículos Usados')
st.markdown("---")
st.markdown("#### Selecione as variáveis e visualize os gráficos interativos abaixo. 🧭")
st.markdown("---")

# Caixas de seleção para gráficos
build_histogram = st.checkbox("📌 Histograma")
build_scatter = st.checkbox("📌 Gráfico de Dispersão")
build_bar = st.checkbox("📌 Gráfico de Barras")

# Histograma Interativo
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
    st.subheader("🔍 Gráfico de Dispersão Interativo")

    x_legivel = st.selectbox("Eixo X", numeric_cols_legiveis, index=numeric_cols_legiveis.index("Quilometragem (km)"))
    y_legivel = st.selectbox("Eixo Y", numeric_cols_legiveis, index=numeric_cols_legiveis.index("Preço (R$)"))
    color_legivel = st.selectbox("Colorir por", numeric_cols_legiveis + categorical_cols_legiveis, index=(numeric_cols_legiveis + categorical_cols_legiveis).index("Ano de Fabricação"))

    x_axis = coluna_original(x_legivel)
    y_axis = coluna_original(y_legivel)
    color_by = coluna_original(color_legivel)

    scatter_fig = px.scatter(
        vehicles_data,
        x=x_axis,
        y=y_axis,
        color=color_by,
        color_continuous_scale="Cividis" if vehicles_data[color_by].dtype != 'object' else None,
        labels={
            x_axis: x_legivel,
            y_axis: y_legivel,
            color_by: color_legivel
        },
        hover_data=["paint_color", "condition"]
    )

    scatter_fig.update_layout(
        title=f"{y_legivel} vs {x_legivel} colorido por {color_legivel}",
        title_font_size=20,
        title_x=0,
        height=500,
        xaxis=dict(range=[0, vehicles_data[x_axis].max()])
    )

    st.plotly_chart(scatter_fig)
    st.markdown("---")

# Gráfico de Barras Interativo
if build_bar:
    st.subheader("📈 Gráfico de Barras Interativo")

    group_legivel = st.selectbox("Agrupar por", categorical_cols_legiveis)
    metric_legivel = st.selectbox("Métrica de média", numeric_cols_legiveis, index=numeric_cols_legiveis.index("Dias para Venda"))

    group_col = coluna_original(group_legivel)
    metric_col = coluna_original(metric_legivel)

    df_grouped = vehicles_data.groupby(group_col)[metric_col].mean().reset_index().sort_values(group_col)

    bar_fig = px.bar(
        df_grouped,
        x=group_col,
        y=metric_col,
        color=metric_col,
        color_continuous_scale="Cividis",
        labels={
            group_col: group_legivel,
            metric_col: f"Média de {metric_legivel}"
        }
    )

    bar_fig.update_layout(
        title=f"Média de {metric_legivel} por {group_legivel}",
        title_font_size=20,
        title_x=0,
        xaxis=dict(type="category"),
        height=500
    )

    st.plotly_chart(bar_fig)
    st.markdown("---")