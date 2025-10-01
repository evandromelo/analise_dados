import pandas as pd
import numpy as np

print("--- Exemplo 1: Criação de DataFrame com Dados Agrícolas ---")
# Cenário: Análise de produção de culturas por região
data = {
    'cultura': np.random.choice(['Milho', 'Soja', 'Trigo', 'Café'], 100),
    'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste', 'Central'], 100),
    'tipo_solo': np.random.choice(['Arenoso', 'Argiloso', 'Humoso'], 100),
    'irrigacao': np.random.choice(['Gotejamento', 'Aspersão', 'Nenhuma'], 100),
    'producao_ton': np.random.normal(50, 15, 100), # Produção em toneladas
    'area_hectare': np.random.uniform(10, 100, 100), # Área em hectares
    'umidade_solo': np.random.uniform(20, 80, 100), # Umidade do solo em %
    'temperatura_media': np.random.normal(25, 5, 100) # Temperatura média em °C
}
df = pd.DataFrame(data)
print("DataFrame de exemplo (primeiras 5 linhas):")
print(df.head())
print("\n" + "-"*70 + "\n")

print("--- Exemplo 2: GroupBy Básico - Média de Produção por Região ---")
# Agrupando por região e calculando a média de produção
producao_por_regiao = df.groupby('regiao')['producao_ton'].mean()
print("Média de produção por região:")
print(producao_por_regiao)
print("\n" + "-"*70 + "\n")

print("--- Exemplo 3: Estatísticas Descritivas com GroupBy ---")
# Média de produção por tipo de solo
media_producao_solo = df.groupby('tipo_solo')['producao_ton'].mean()
print("Média de produção por tipo de solo:")
print(media_producao_solo)

# Desvio padrão de umidade por tipo de irrigação
desvio_padrao_umidade_irrigacao = df.groupby('irrigacao')['umidade_solo'].std()
print("\nDesvio padrão de umidade por tipo de irrigação:")
print(desvio_padrao_umidade_irrigacao)
print("\n" + "-"*70 + "\n")

print("--- Exemplo 4: Múltiplos Agrupamentos ---")
# Produção média por cultura e tipo de solo
producao_cultura_solo = df.groupby(['cultura', 'tipo_solo'])['producao_ton'].mean()
print("Produção média por cultura e tipo de solo:")
print(producao_cultura_solo)
print("\n" + "-"*70 + "\n")

print("--- Exemplo 5: Agregação Personalizada com .agg() ---")
# Aplicando diferentes funções a diferentes colunas
agg_personalizada = df.groupby('cultura').agg({
    'producao_ton': ['mean', 'std', 'min', 'max'],
    'area_hectare': 'sum',
    'umidade_solo': ['mean', 'median'],
    'temperatura_media': 'mean'
})
print("Resultado da agregação personalizada por cultura (primeiras 5 linhas):")
print(agg_personalizada.head())

# Exemplo de função personalizada para produtividade
def produtividade(x):
    if x['area_hectare'].sum() == 0:
        return 0
    return x['producao_ton'].sum() / x['area_hectare'].sum()

produtividade_por_cultura = df.groupby('cultura').apply(produtividade)
print("\nProdutividade calculada por cultura (função personalizada):")
print(produtividade_por_cultura)
print("\n" + "-"*70 + "\n")

print("--- Exemplo 6: Visualização (exemplo básico com Pandas) ---")
# Para visualização, geralmente se usaria bibliotecas como Matplotlib ou Seaborn.
# Aqui, um exemplo simples de como o Pandas pode gerar um plot diretamente.

# Calculando a média de produção por cultura
producao_por_cultura_plot = df.groupby('cultura')['producao_ton'].mean()

# O comando abaixo geraria um gráfico se executado em um ambiente interativo (ex: Jupyter Notebook)
# producao_por_cultura_plot.plot(kind='bar', title='Média de Produção por Cultura')
# import matplotlib.pyplot as plt
# plt.ylabel('Produção (ton)')
# plt.xlabel('Cultura')
# plt.show()

print("Para visualização, o Pandas pode gerar gráficos diretamente (requer Matplotlib/Seaborn para exibição).")
print("Exemplo: df.groupby('cultura')['producao_ton'].mean().plot(kind='bar')")
print("\n" + "-"*70 + "\n")