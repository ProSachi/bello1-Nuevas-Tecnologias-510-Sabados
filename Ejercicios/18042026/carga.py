import pandas as pd

def cargaVentas():
    df_ventas = pd.read_csv('./data/raw/ventas.csv')
    df_ventas.info()
    return df_ventas

def cargaClientes():
    df_clientes = pd.read_csv('./data/raw/clientes.csv')
    df_clientes.info()
    return df_clientes



