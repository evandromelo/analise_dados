import pandas as pd

# Exemplo de DataFrame
dados = {
    'Temperatura': [25, 28, None, 30],
    'Umidade': [60, None, 70, 65],
    'Precipitação': [None, 5, 10, 15]
}
df = pd.DataFrame(dados)

# Identificar valores ausentes
print(df.isnull())
print(df.isnull().sum())  # Contagem de valores ausentes por coluna