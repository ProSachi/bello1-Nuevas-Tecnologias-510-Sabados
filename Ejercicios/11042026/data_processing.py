"""
Módulo de procesamiento y limpieza de datos.

Este módulo proporciona funciones para cargar, limpiar y transformar datos
desde archivos CSV, incluyendo manejo de valores nulos, estandarización de texto
y limpieza específica del proyecto.
"""

import pandas as pd
import numpy as np
import os


def cargar_datos(ruta_archivo: str) -> pd.DataFrame:
    """
    Carga datos desde un archivo CSV.
    
    Args:
        ruta_archivo: Ruta al archivo CSV
        
    Returns:
        DataFrame con los datos cargados
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        pd.errors.ParserError: Si hay error al parsear el CSV
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"Archivo no encontrado: {ruta_archivo}")
    
    try:
        df = pd.read_csv(ruta_archivo)
        print(f"✓ Datos cargados exitosamente desde: {ruta_archivo}")
        print(f"  - Filas: {len(df)}, Columnas: {len(df.columns)}")
        return df
    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"Error al parsear {ruta_archivo}: {str(e)}")


def manejar_valores_nulos(df: pd.DataFrame, estrategia: str = "eliminar") -> pd.DataFrame:
    """
    Maneja valores nulos (NaN) en el DataFrame.
    
    Args:
        df: DataFrame a procesar
        estrategia: "eliminar" (elimina filas con nulos) o "llenar" (rellena con defaults)
        
    Returns:
        DataFrame sin valores nulos
    """
    nulos_antes = df.isnull().sum().sum()
    
    if estrategia == "eliminar":
        df = df.dropna()
    elif estrategia == "llenar":
        # Rellenar valores nulos según el tipo de dato
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna("Desconocido")
            else:
                df[col] = df[col].fillna(0)
    
    nulos_despues = df.isnull().sum().sum()
    print(f"✓ Valores nulos manejados:")
    print(f"  - Antes: {nulos_antes} nulos")
    print(f"  - Después: {nulos_despues} nulos")
    print(f"  - Estrategia: {estrategia}")
    
    return df


def estandarizar_texto(df: pd.DataFrame, columnas: list = None) -> pd.DataFrame:
    """
    Estandariza texto en las columnas especificadas:
    - Convierte a minúsculas
    - Elimina espacios extra (inicio, fin y múltiples internos)
    - Elimina caracteres especiales no deseados
    
    Args:
        df: DataFrame a procesar
        columnas: Lista de columnas a estandarizar (si es None, procesa todas las de tipo object)
        
    Returns:
        DataFrame con textos estandarizados
    """
    if columnas is None:
        columnas = df.select_dtypes(include=['object']).columns.tolist()
    
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: 
                str(x).strip().lower() if pd.notna(x) else x
            )
            # Eliminar espacios múltiples internos
            df[col] = df[col].apply(lambda x: 
                ' '.join(str(x).split()) if pd.notna(x) else x
            )
    
    print(f"✓ Texto estandarizado en columnas: {columnas}")
    return df


def limpiar_campos_monetarios(df: pd.DataFrame, columnas: list = None) -> pd.DataFrame:
    """
    Limpia campos monetarios:
    - Elimina símbolos de moneda ($, €, etc.)
    - Convierte a números flotantes
    - Maneja formatos de separadores decimales
    
    Args:
        df: DataFrame a procesar
        columnas: Lista de columnas monetarias a limpiar
        
    Returns:
        DataFrame con campos monetarios limpios
    """
    if columnas is None:
        columnas = []
    
    for col in columnas:
        if col in df.columns:
            # Eliminar símbolos monetarios y espacios
            df[col] = df[col].apply(lambda x: 
                str(x).replace('$', '').replace('€', '').replace('¢', '').strip() 
                if pd.notna(x) else x
            )
            # Convertir a número flotante
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    print(f"✓ Campos monetarios limpiados: {columnas}")
    return df


def convertir_tipos_datos(df: pd.DataFrame, mapeo_tipos: dict = None) -> pd.DataFrame:
    """
    Convierte tipos de datos en el DataFrame.
    
    Args:
        df: DataFrame a procesar
        mapeo_tipos: Diccionario {columna: tipo_dato}
        
    Returns:
        DataFrame con tipos convertidos
    """
    if mapeo_tipos is None:
        mapeo_tipos = {}
    
    for col, tipo in mapeo_tipos.items():
        if col in df.columns:
            try:
                df[col] = df[col].astype(tipo)
            except ValueError:
                print(f"⚠ No se pudo convertir {col} a {tipo}")
    
    print(f"✓ Tipos de datos convertidos: {list(mapeo_tipos.keys())}")
    return df


def eliminar_duplicados(df: pd.DataFrame, columnas: list = None, mantener: str = 'first') -> pd.DataFrame:
    """
    Elimina filas duplicadas del DataFrame.
    
    Args:
        df: DataFrame a procesar
        columnas: Columnas a considerar para duplicados (None = todas)
        mantener: 'first', 'last' o False (elimina todas)
        
    Returns:
        DataFrame sin duplicados
    """
    duplicados_antes = df.duplicated(subset=columnas).sum()
    
    if columnas:
        df = df.drop_duplicates(subset=columnas, keep=mantener)
    else:
        df = df.drop_duplicates(keep=mantener)
    
    print(f"✓ Duplicados eliminados: {duplicados_antes} filas removidas")
    return df


def validar_email(email: str) -> bool:
    """
    Valida que un email tenga formato básico correcto.
    
    Args:
        email: String de email a validar
        
    Returns:
        True si es válido, False si no
    """
    if pd.isna(email):
        return False
    email_str = str(email).strip()
    return '@' in email_str and '.' in email_str


def limpiar_correos(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Limpia y valida la columna de correos electrónicos.
    
    Args:
        df: DataFrame a procesar
        columna: Nombre de la columna con correos
        
    Returns:
        DataFrame con correos limpios
    """
    if columna not in df.columns:
        print(f"⚠ Columna {columna} no encontrada")
        return df
    
    # Limpiar espacios y convertir a minúsculas
    df[columna] = df[columna].apply(lambda x: 
        str(x).strip().lower() if pd.notna(x) else x
    )
    
    # Contar correos inválidos
    correos_invalidos = df[~df[columna].apply(validar_email)].shape[0]
    
    print(f"✓ Correos limpiados en columna '{columna}'")
    print(f"  - Correos inválidos encontrados: {correos_invalidos}")
    
    return df


def obtener_estadisticas_limpieza(df: pd.DataFrame) -> dict:
    """
    Obtiene estadísticas básicas del DataFrame después de limpieza.
    
    Args:
        df: DataFrame a analizar
        
    Returns:
        Diccionario con estadísticas
    """
    stats = {
        'total_filas': len(df),
        'total_columnas': len(df.columns),
        'memoria_mb': df.memory_usage(deep=True).sum() / 1024**2,
        'columnas': df.columns.tolist(),
        'tipos': df.dtypes.to_dict(),
        'nulos_por_columna': df.isnull().sum().to_dict()
    }
    return stats


def resumen_limpieza(df: pd.DataFrame):
    """
    Imprime un resumen de la limpieza realizada.
    
    Args:
        df: DataFrame limpio
    """
    print("\n" + "="*60)
    print("RESUMEN DE LIMPIEZA")
    print("="*60)
    print(f"Total de filas: {len(df)}")
    print(f"Total de columnas: {len(df.columns)}")
    print(f"Memoria utilizada: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print(f"Valores nulos totales: {df.isnull().sum().sum()}")
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nPrimeras 5 filas:")
    print(df.head())
    print("="*60 + "\n")
