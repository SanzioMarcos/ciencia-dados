import pandas as pd

df_vendas = pd.read_csv("vendas.csv")
print(df_vendas.head(), '\n')

df_clientes = pd.read_excel("clientes.xlsx")
print(df_clientes.head(), '\n')

# Juntando a tabela de vendas com a de clientes usando a coluna 'ID_Cliente' como elo
df_consolidado = pd.merge(df_vendas, df_clientes, on="ID_Cliente", how="inner")

# Agora a tabela 'df_consolidado' tem os dados da venda E o nome/e-mail do cliente na mesma linha!
print(df_consolidado.head())
