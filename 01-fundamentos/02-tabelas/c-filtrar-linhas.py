import pandas as pd

df_vendas = pd.read_csv("vendas.csv")
print(df_vendas.head(), '\n')

# Criando um filtro: queremos apenas as linhas onde o Valor_Total é maior que 500
vendas_grandes = df_vendas[df_vendas["Valor_Total"] > 500]

print('Valor_Total > 500:\n', vendas_grandes, '\n')

# Outro exemplo: filtrando por texto (apenas produtos que sejam "Notebook")
vendas_notebooks = df_vendas[df_vendas["Produto"] == "Notebook"]

print('Notebook:\n', vendas_notebooks)