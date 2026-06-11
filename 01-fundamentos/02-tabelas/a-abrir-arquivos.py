import pandas as pd

### 1. Abrir Arquivos de Dados

# Abrindo um arquivo CSV
df_vendas = pd.read_csv("vendas.csv")

# Abrindo um arquivo Excel
df_clientes = pd.read_excel("clientes.xlsx")

# Comando essencial para dar uma "espiada" nas primeiras 5 linhas da tabela
print(df_vendas.head())
print('---')
print(df_clientes.head())