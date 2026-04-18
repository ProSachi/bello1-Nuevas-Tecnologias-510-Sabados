import pandas as pd

# Insumos (Pre-auditados)
df_clientes = pd.DataFrame({'id_cliente': [1, 2, 3], 'nombre': ['Ana', 'Luis', 'Marta']})

# Nota: Luis (ID 2) no tiene compras. El ID 1 compró dos veces.

df_ventas = pd.DataFrame({'id_venta': [101, 102, 103], 'id_cliente': [1, 1, 3], 'monto': [50, 150, 200]})


