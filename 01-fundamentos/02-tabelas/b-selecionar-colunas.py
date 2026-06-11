import pandas as pd

### 1. Abrir Arquivos de Dados

# Abrindo um arquivo CSV
df_vendas = pd.read_csv("vendas.csv")

# Abrindo um arquivo Excel
df_clientes = pd.read_excel("clientes.xlsx")

# Comando essencial para dar uma "espiada" nas primeiras 5 linhas da tabela
print(df_vendas.head())
print('---')

# Selecionando apenas UMA coluna (retorna uma série de dados)
coluna_produtos = df_vendas["Produto"]
print(coluna_produtos)
print('---')

# Selecionando MÚLTIPLAS colunas (use colchetes duplos [[ ]])
colunas_analise = df_vendas[["Produto", "Valor_Total"]]
print(colunas_analise)
