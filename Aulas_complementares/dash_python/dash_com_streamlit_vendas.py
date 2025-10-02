'''
# Dash de Vendas com Streamlit

O Streamlit é uma biblioteca para construir aplicativos web interativos. 

Ele não imprime resultados no console ou diretamente no notebook, mas sim constrói 
    uma interface de usuário no navegador web.

Este script cria um dashboard interativo para visualizar dados de vendas usando a biblioteca Streamlit.

Ele carrega os dados de um arquivo CSV, permite a seleção de um mês específico e
 exibe gráficos de faturamento por diferentes categorias.

As visualizações incluem:
    # Faturamento por mês e por loja
    # Faturamento por produto
    # Faturamento por formas de pagamento
    # Faturamento por loja

Para executar este script, você precisará ter o Streamlit instalado.
pip install streamlit pandas plotly

Para rodar o aplicativo, use o comando:
streamlit run dash_vendas.py

 '''

import streamlit as st        # Importa a biblioteca Streamlit para criar aplicativos web interativos
import pandas as pd           # Importa a biblioteca Pandas para manipulação de dados
import plotly.express as px # Importa Plotly Express para criar gráficos dinâmicos

# Configura o layout da página do Streamlit para "wide",
# o que significa que o conteúdo ocupará a largura total da tela.
st.set_page_config(layout="wide")

# Carrega os dados do arquivo CSV 'dados_vendas.csv'.
# O delimitador é ';', e a codificação é "ISO-8859-1" para lidar com caracteres especiais.
df = pd.read_csv('dados_vendas.csv', delimiter=';', encoding="ISO-8859-1")

# Converte a coluna "DATA_VENDA" para o formato de data e hora do Pandas.
df["DATA_VENDA"] = pd.to_datetime(df["DATA_VENDA"])

# Ordena o DataFrame pela coluna "DATA_VENDA" em ordem crescente.
df = df.sort_values("DATA_VENDA")

# Cria uma nova coluna "MES" que combina o mês e o ano da "DATA_VENDA".
# Isso é útil para agrupar e filtrar os dados por mês.
df["MES"] = df["DATA_VENDA"].apply(lambda x: str(x.month) + "-" + str(x.year))

# Cria uma caixa de seleção na barra lateral do Streamlit para que o usuário escolha um mês.
# Os valores únicos da coluna "MES" são usados como opções.
mes_selecionado = st.sidebar.selectbox("Selecione o Mês", df["MES"].unique())

# Filtra o DataFrame original com base no mês selecionado pelo usuário na barra lateral.
df_filtro = df[df["MES"] == mes_selecionado]

# Exibe o DataFrame filtrado. Em um aplicativo Streamlit, isso seria uma tabela.
st.subheader(f"Dados de Vendas para o Mês: {mes_selecionado}")
st.dataframe(df_filtro) # Usamos st.dataframe para exibir a tabela de forma mais amigável

# Cria um layout com 2 colunas para organizar os gráficos no dashboard.
# col1 e col2 estarão na primeira linha.
col1, col2 = st.columns(2)
# col3 e col4 estarão na segunda linha.
col3, col4 = st.columns(2)

# --- Gráfico 1: Faturamento por dia ---
# Cria um gráfico de barras com o faturamento diário, colorido por loja.
fig_date = px.bar(df_filtro, x="DATA_VENDA", y="VALOR_TOTAL", color="LOJA", title="Faturamento por Dia")
# Exibe o gráfico na primeira coluna.
col1.plotly_chart(fig_date, use_container_width=True) # use_container_width=True para ajustar ao tamanho da coluna

# --- Gráfico 2: Faturamento por produto ---
# Cria um gráfico de barras horizontal com o faturamento por produto, colorido por loja.
fig_prod = px.bar(df_filtro, x="VALOR_TOTAL", y="PRODUTO", color="LOJA", title="Faturamento por Produto", orientation="h")
# Exibe o gráfico na segunda coluna.
col2.plotly_chart(fig_prod, use_container_width=True)

# --- Gráfico 3: Faturamento por Loja ---
# Agrupa o DataFrame filtrado por "LOJA" e soma o "VALOR_TOTAL" para cada loja.
loja_total = df_filtro.groupby("LOJA")[["VALOR_TOTAL"]].sum().reset_index()
# Cria um gráfico de barras mostrando o faturamento total por loja.
fig_loja = px.bar(loja_total, x="LOJA", y="VALOR_TOTAL", title="Faturamento por Loja")
# Exibe o gráfico na terceira coluna.
col3.plotly_chart(fig_loja, use_container_width=True)

# --- Gráfico 4: Faturamento por tipo de pagamento ---
# Cria um gráfico de pizza mostrando a proporção do faturamento por forma de pagamento.
fig_pagto = px.pie(df_filtro, values="VALOR_TOTAL", names="FORMA_PAGAMENTO", title="Faturamento por Tipo de Pagamento")
# Exibe o gráfico na quarta coluna.
col4.plotly_chart(fig_pagto, use_container_width=True)
# Fim do código