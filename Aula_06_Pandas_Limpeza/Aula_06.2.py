# Exemplo de DataFrame com duplicatas
dados_duplicados = {
    'Sensor': ['A', 'B', 'A', 'C'],
    'Valor': [10, 20, 10, 30]
}
df_duplicados = pd.DataFrame(dados_duplicados)

# Identificar duplicatas
print(df_duplicados.duplicated())

# Remover duplicatas
df_sem_duplicatas = df_duplicados.drop_duplicates()
print(df_sem_duplicatas)