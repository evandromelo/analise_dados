# -*- coding: utf-8 -*-
"""
Análise de Correlação entre Clima e Produtividade
Autor: Evandro Melo
Descrição: Este script analisa a relação entre variáveis climáticas e produtividade agrícola.
Localização: cd_2/exercicios/correlacao_clima_producao.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurações padrão de plotagem
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# -------------------------------
# 1. Definir caminhos relativos à localização do script
# -------------------------------

# Diretório do script (pasta 'exercicios')
script_dir = os.path.dirname(__file__) if '__file__' in locals() else os.getcwd()

# Caminho para a pasta datasets (irmã de 'exercicios')
datasets_dir = os.path.join(script_dir, '..', 'datasets')

clima_path = os.path.join(datasets_dir, 'clima_exc16.csv')
producao_path = os.path.join(datasets_dir, 'prod_cult_exc16.csv')

# -------------------------------
# 2. Carregar os dados
# -------------------------------

# Dados climáticos horários
try:
    clima = pd.read_csv(clima_path, parse_dates=['data_hora'])
    print("✅ Dados climáticos carregados com sucesso!")
    print("Colunas disponíveis em clima:", list(clima.columns))
    print(clima.head())
except FileNotFoundError:
    raise FileNotFoundError(f"Arquivo não encontrado: {clima_path}")

# Dados de produção
try:
    producao = pd.read_csv(producao_path, parse_dates=['data_colheita'])
    producao.rename(columns={'data_colheita': 'data'}, inplace=True)
    print("✅ Dados de produção carregados com sucesso!")
    print("Colunas disponíveis em produção:", list(producao.columns))
    print(producao.head())
except FileNotFoundError:
    raise FileNotFoundError(f"Arquivo não encontrado: {producao_path}")

# -------------------------------
# 3. Pré-processamento dos dados climáticos
# -------------------------------

# Renomear colunas para nomes simples (sem caracteres especiais)
clima_clean = clima[['data_hora', 'radiacao_wm2', 'temperatura_c', 'umidade_rel_%', 'vento_ms']].copy()
clima_clean.rename(columns={
    'temperatura_c': 'temperatura',
    'umidade_rel_%': 'umidade',
    'radiacao_wm2': 'radiacao_solar',
    'vento_ms': 'vento'
}, inplace=True)

# Extrair data (sem hora) para agrupar por dia
clima_clean['data'] = pd.to_datetime(clima_clean['data_hora']).dt.date
clima_clean['data'] = pd.to_datetime(clima_clean['data'])

# Calcular médias diárias (precipitação seria soma, mas não temos aqui)
# Vamos manter: temperatura, umidade, radiação e vento como média diária
clima_diario = clima_clean.groupby('data').agg({
    'temperatura': 'mean',
    'umidade': 'mean',
    'radiacao_solar': 'mean',
    'vento': 'mean'
}).reset_index()

print("\nDados climáticos diários calculados:")
print(clima_diario.head())

# -------------------------------
# 4. Preparar dados de produção
# -------------------------------

if 'produtividade_t_ha' not in producao.columns:
    print("Colunas disponíveis em produção:", list(producao.columns))
    raise KeyError("Coluna 'produtividade_t_ha' não encontrada!")

# Converter 'data' para datetime.date para compatibilidade
producao['data'] = pd.to_datetime(producao['data']).dt.date
producao['data'] = pd.to_datetime(producao['data'])

# Agrupar por data (caso haja múltiplas observações)
producao_diaria = producao.groupby('data')['produtividade_t_ha'].mean().reset_index()
producao_diaria.rename(columns={'produtividade_t_ha': 'produtividade'}, inplace=True)

print("\nProdução diária:")
print(producao_diaria.head())

# -------------------------------
# 5. Mesclar dados climáticos e de produção
# -------------------------------

dados_combinados = pd.merge(clima_diario, producao_diaria, on='data', how='inner')

if dados_combinados.empty:
    raise ValueError("""
    ❌ Nenhum dado comum encontrado entre clima e produção.
    Verifique se as datas nos dois arquivos têm sobreposição.
    Datas em clima: {} até {}
    Datas em produção: {} até {}
    """.format(
        clima_diario['data'].min().date(),
        clima_diario['data'].max().date(),
        producao_diaria['data'].min().date(),
        producao_diaria['data'].max().date()
    ))

print("\n✅ Dados combinados com sucesso! Tamanho:", dados_combinados.shape)
print(dados_combinados.head())

# -------------------------------
# 6. Calcular correlação
# -------------------------------

colunas_numericas = ['temperatura', 'umidade', 'radiacao_solar', 'vento', 'produtividade']
dados_corr = dados_combinados[colunas_numericas]

correlation_matrix = dados_corr.corr()

print("\n📊 Matriz de Correlação (em relação à produtividade):")
print(correlation_matrix['produtividade'].sort_values(key=abs, ascending=False).to_string())

# -------------------------------
# 7. Visualização: Heatmap
# -------------------------------

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, fmt='.2f', cbar_kws={"shrink": .8})
plt.title('Correlação entre Variáveis Climáticas e Produtividade')
plt.tight_layout()
output_plot = os.path.join(script_dir, 'correlacao_clima_producao.png')
plt.savefig(output_plot, dpi=200, bbox_inches='tight')
plt.show()

print(f"🖼️ Gráfico salvo em: {output_plot}")

# -------------------------------
# 8. Salvar resultados
# -------------------------------

output_csv = os.path.join(script_dir, 'analise_correlacao_completa.csv')
dados_combinados.to_csv(output_csv, index=False)

print(f"\n✅ Análise concluída!")
print(f"📁 Resultados salvos em: {output_csv}")
print(f"🖼️  Gráfico salvo em: {output_plot}")