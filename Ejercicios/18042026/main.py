import pandas as pd
import carga
import limpieza

isLoader = False 

while True:
    opcion = input("Seleccione la opción deseada: ")
    match opcion:
        case '1':
            df_clientes = carga.cargaClientes()
            df_ventas = carga.cargaVentas()
            isLoader = True
            df_clientes.info()
            df_ventas.info()
            print("Carga Completa")
        case '2':
            if isLoader:
                df_clientes_Limpio = limpieza.limpiezaCliente(df_clientes)
                df_ventas_Limpio = limpieza.limpiezaVenta(df_ventas)
                print("Limpieza completa")
            else:
                print("Primero debes realizar la carga")  
        case '3':
            print("Analisis")
        case '4':
            print("Preguntas Resueltas")
        case '5':
            print("Saliendo del sistema")
            break        
        case _:
            print("Opción Invalida") 
