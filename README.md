# 📊 Project_sprint5

## 📝 Nome do Projeto  
**Projeto Final do Sprint 5: Visualização Interativa de Dados**

## 📌 Descrição  
Este projeto cria um aplicativo web interativo utilizando o **Streamlit**, no qual o usuário consegue interagir com histogramas e gráficos de dispersão com base em informações extraídas do **DataFrame vehicles.csv**.

Essas visualizações podem ser muito úteis para aplicação de estratégias de vendas, tomada de decisões e análise de comportamento de produtos por N parâmetros.

---

## 📦 Requisitos  

- Python  
- Bibliotecas: pandas, plotly, streamlit

---

## 📁 Estrutura do Projeto  

project_sprint5/
├── notebooks/
│ └── EDA.ipynb # Notebook com EDA e insights
├── streamlite/
│ └── config.toml # Arquivo de configuração do Streamlit
├── vehicles.csv # Arquivo de dados original
│   vehicles_clear.csv # Arquivos de dados limpo após análise
├── app.py # Código principal do app Streamlit
├── requirements.txt # Bibliotecas utilizadas
└── README.md # Explicação do projeto

---

## ⚙️ Funcionalidades  

- 📂 Upload e carregamento de dados CSV de veículos  
- 📊 Visualização interativa via histogramas e gráficos de dispersão  
- ✅ Caixas de seleção para escolher quais gráficos gerar

---

## 🚀 Como usar  

1. Instale as dependências:
    pip install pandas plotly streamlit
2. Execute o app:
streamlit run app.py
3. O navegador será aberto automaticamente. Interaja com a aplicação e explore os dados!

👩‍💻 Autor
Sara Santos
https://github.com/santossara97
