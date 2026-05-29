import pandas as pd
df_clientes = pd.read_sql('tb_clientes', engine)
df_pedidos = pd.read_sql('tb_pedidos', engine)
df_itens = pd.read_sql('tb_itens', engine)
df_produtos = pd.read_sql('tb_produtos', engine)

# Merge : Juntar dois dataframes

df_merge1= pd.merge(
    df_clientes, df_pedidos, on = 'codigo_produto'
)

#  Quando os nomes das colunas são diferentes é necessário informar o parâmetro left
df_merge1 = pd.merge(
    df_clientes
)