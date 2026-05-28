from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password = ''
data_base= 'db_mod2_aula05_2'

engine = create_engine(

    f'mysql+pymysql://{user}:{password}@{host}/{data_base}'
)

try:

    df_clientes = pd.read_sql('tb_clientes', engine)
    df_pedidos = pd.read_sql('tb_pedidos', engine)
    df_itens = pd.read_sql('tb_itens', engine)
    df_produtos = pd.read_sql('tb_produtos', engine)

    

    # print(df_clientes.head())

except Exception as e:
    print(f'Falha de conexão {e}')

try:

    df_merge1 = pd.merge(df_clientes, df_pedidos , on= 'codigo_cliente')
    df_merge2 = pd.merge(df_merge1, df_itens , on= 'codigo_pedido')
    df_final = pd.merge(df_merge2, df_produtos , on= 'codigo_produto')

    # print(df_final)

    filtro = (
        (df_final['cidade'] == 'Sao Paulo')
    )
    df_clientes_sp = df_final [filtro]
    
    print (df_clientes_sp)
   
   
except Exception as e:
    print(f'Erro nos dados {e}')    
