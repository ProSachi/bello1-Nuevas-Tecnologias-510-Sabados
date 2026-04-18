import pandas as pd

def limpiezaVenta(df_ventas):
    print('Limpieza de espacio y texto en formato titulo')
    df_ventas['producto'] = df_ventas['producto'].str.strip().str.title()
    print('Eliminar datos duplicados')
    df_ventas = df_ventas.drop_duplicates()
    df_ventas.info()
    return df_ventas


def limpiezaCliente(df_cliente):
    print('Limpieza de espacio y texto en formato titulo')
    df_cliente['nombre'] = df_cliente['nombre'].str.strip().str.title()
    df_cliente['ciudad'] = df_cliente['ciudad'].str.strip().str.title()
    print('Eliminar datos duplicados')
    df_cliente = df_cliente.drop_duplicates()
    #df_cliente['edad'] = df_cliente['edad'].df_cliente('', "20")
    df_cliente['edad'] = df_cliente['edad'].fillna("20")
    df_cliente['ciudad'] = df_cliente['ciudad'].fillna("Desconocida")

    #Definimos nuestra lista estricta
    ciudades_oficiales = ['Medellin', 'Bogota', 'Cali', 'Barranquilla', 'Cartagena', 'Bucaramanga',
    'Pereira', 'Cucuta', 'Manizales', 'Ibague', 'Neiva', 'Soacha', 'Pasto']

    # Usamos ~ (NOT) para buscar a los que violan la regla de la lista
    mascara_infractores = ~df_cliente['ciudad'].isin(ciudades_oficiales)

    # Filtramos el DataFrame usando la máscara para ver los errores
    errores_detectados = df_cliente[mascara_infractores]
    #Hacemos un diccionario para aplicar una traducción
    traduccion = { 'bogota': 'Bogota', 'Bogotá': 'Bogota','Bogóta': 'Bogota', 'desconocida': 'Bogota','Bógota': 'Bogota'}

    # Aplicamos la traducción solo a la columna afectada
    df_cliente['ciudad'] = df_cliente['ciudad'].replace(traduccion)

    df_cliente.info()
    return df_cliente

