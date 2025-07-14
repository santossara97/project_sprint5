# 📊 Project_sprint5

## 📝 Nome do Projeto  
**Projeto Final do Sprint 5: Visualização Interativa de Dados**

## 📌 Descrição  
Este projeto desenvolve um aplicativo web interativo utilizando Streamlit, permitindo ao usuário explorar gráficos dinâmicos baseados nos dados do conjunto vehicles.csv.

A proposta é facilitar a análise de informações sobre veículos por meio de histogramas, gráficos de dispersão e gráficos de barras, promovendo insights que podem ser aplicados em:

- Estratégias de venda

- Tomada de decisões

- Análise de mercado automotivo.

---

## 📦 Requisitos  

- Python  
- Bibliotecas: pandas, plotly, streamlit

---

## 📁 Estrutura do Projeto  

project_sprint5/
├── notebooks/
│   └── EDA.ipynb             # Análise exploratória e limpeza dos dados
├── streamlit/
│   └── config.toml           # Configuração do perfil do Streamlit (opcional)
├── vehicles.csv              # Dados originais
├── vehicles_clear.csv        # Dados tratados para visualização
├── app.py                    # Aplicativo principal com Streamlit
├── requirements.txt          # Bibliotecas necessárias
└── README.md                 # Descrição e instruções do projeto

---

## ⚙️ Funcionalidades  

📥 Carregamento automático dos dados

📊 Geração de histogramas, gráficos de dispersão e de barras

✅ Interatividade via caixas de seleção

🔎 Visualização de padrões com base em:
    Quilometragem (odometer)
    Preço (price)
    Ano de fabricação (model_year)
    Tempo médio de venda (days_listed)

---

## 🚀 Como usar  

1. Instale as dependências:
    pip install pandas plotly streamlit
2. Execute o app:
streamlit run app.py
3. O navegador será aberto automaticamente. Interaja com a aplicação e explore os dados!

👩‍💻 Autora
Sara Santos
https://github.com/santossara97
https://project-sprint5-bix2.onrender.com/
