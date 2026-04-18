"""
Script principal de análisis de datos.

Este script carga datos desde CSV, realiza limpieza y procesamiento,
y responde preguntas clave sobre usuarios y sus actividades.
"""

import pandas as pd
import sys
from data_processing import (
    cargar_datos, manejar_valores_nulos, estandarizar_texto,
    limpiar_campos_monetarios, convertir_tipos_datos, 
    limpiar_correos, resumen_limpieza
)


def main():
    """Función principal del análisis."""
    
    print("\n" + "="*70)
    print("ANÁLISIS DE DATOS: USUARIOS Y ACTIVIDADES")
    print("="*70 + "\n")
    
    try:
        # ============================================================
        # PASO 1: CARGAR DATOS
        # ============================================================
        print("PASO 1: Cargando datos...\n")
        
        df_usuarios = cargar_datos('data/usuarios.csv')
        df_actividades = cargar_datos('data/actividades.csv')
        
        # ============================================================
        # PASO 2: LIMPIAR Y PROCESAR USUARIOS
        # ============================================================
        print("\nPASO 2: Limpiando datos de usuarios...\n")
        
        # Manejar nulos y estandarizar
        df_usuarios = manejar_valores_nulos(df_usuarios, estrategia='eliminar')
        df_usuarios = estandarizar_texto(df_usuarios, columnas=['name', 'correo'])
        df_usuarios = limpiar_correos(df_usuarios, columna='correo')
        df_usuarios = convertir_tipos_datos(df_usuarios, {'id': 'int64'})
        
        resumen_limpieza(df_usuarios)
        
        # ============================================================
        # PASO 3: LIMPIAR Y PROCESAR ACTIVIDADES
        # ============================================================
        print("PASO 3: Limpiando datos de actividades...\n")
        
        # Manejar nulos
        df_actividades = manejar_valores_nulos(df_actividades, estrategia='eliminar')
        
        # Estandarizar texto
        df_actividades = estandarizar_texto(
            df_actividades, 
            columnas=['tipo_actividad', 'estado']
        )
        
        # Limpiar campos monetarios
        df_actividades = limpiar_campos_monetarios(
            df_actividades, 
            columnas=['monto']
        )
        
        # Convertir tipos
        df_actividades = convertir_tipos_datos(
            df_actividades, 
            {'id': 'int64', 'usuario_id': 'int64', 'fecha': 'datetime64'}
        )
        
        resumen_limpieza(df_actividades)
        
        # ============================================================
        # PASO 4: MERGE DE DATOS
        # ============================================================
        print("PASO 4: Combinando datos (merge)...\n")
        
        df_analisis = df_actividades.merge(
            df_usuarios,
            left_on='usuario_id',
            right_on='id',
            how='left',
            suffixes=('_act', '_usr')
        )
        
        print(f"✓ Merge completado:")
        print(f"  - Filas resultado: {len(df_analisis)}")
        print(f"  - Usuarios únicos con actividades: {df_analisis['usuario_id'].nunique()}\n")
        
        # ============================================================
        # PREGUNTA 1: ANÁLISIS DE FRECUENCIA
        # ============================================================
        print("="*70)
        print("PREGUNTA 1: ANÁLISIS DE FRECUENCIA")
        print("="*70)
        print("¿Cuál es el usuario con más actividades registradas?\n")
        
        usuario_mas_activo = df_analisis['usuario_id'].value_counts().head(1)
        
        if not usuario_mas_activo.empty:
            id_usuario = usuario_mas_activo.index[0]
            cantidad_actividades = usuario_mas_activo.values[0]
            
            # Obtener info del usuario
            usuario_info = df_usuarios[df_usuarios['id'] == id_usuario]
            
            if not usuario_info.empty:
                nombre_usuario = usuario_info.iloc[0]['name']
                email_usuario = usuario_info.iloc[0]['correo']
                
                print(f"👤 Usuario más activo:")
                print(f"   - ID: {id_usuario}")
                print(f"   - Nombre: {nombre_usuario}")
                print(f"   - Correo: {email_usuario}")
                print(f"   - Total de actividades: {cantidad_actividades}")
        else:
            print("⚠ No se encontraron datos de actividades")
        
        print("\n📊 Top 5 usuarios más activos:")
        top_usuarios = df_analisis['usuario_id'].value_counts().head(5)
        for idx, (usuario_id, count) in enumerate(top_usuarios.items(), 1):
            print(f"   {idx}. Usuario {usuario_id}: {count} actividades")
        
        # ============================================================
        # PREGUNTA 2: ANÁLISIS DE AGREGACIÓN
        # ============================================================
        print("\n" + "="*70)
        print("PREGUNTA 2: ANÁLISIS DE AGREGACIÓN")
        print("="*70)
        print("¿Cuál es el monto total de actividades por tipo de actividad?\n")
        
        monto_por_tipo = df_analisis.groupby('tipo_actividad')['monto'].agg([
            ('total', 'sum'),
            ('promedio', 'mean'),
            ('cantidad', 'count'),
            ('máximo', 'max'),
            ('mínimo', 'min')
        ]).round(2).sort_values('total', ascending=False)
        
        print("💰 Monto por tipo de actividad:")
        print(monto_por_tipo.to_string())
        
        print("\n📈 Resumen por tipo de actividad:")
        for tipo in monto_por_tipo.index:
            total = monto_por_tipo.loc[tipo, 'total']
            promedio = monto_por_tipo.loc[tipo, 'promedio']
            cantidad = monto_por_tipo.loc[tipo, 'cantidad']
            print(f"   - {tipo.capitalize()}:")
            print(f"     • Total: ${total:,.2f}")
            print(f"     • Promedio: ${promedio:,.2f}")
            print(f"     • Cantidad: {int(cantidad)} transacciones")
        
        # ============================================================
        # PREGUNTA 3: ANÁLISIS CON FILTRADO Y CONTEO
        # ============================================================
        print("\n" + "="*70)
        print("PREGUNTA 3: ANÁLISIS CON FILTRADO Y CONTEO")
        print("="*70)
        print("¿Cuántas actividades están completadas vs pendientes?\n")
        
        # Contar actividades por estado
        actividades_por_estado = df_analisis['estado'].value_counts()
        
        print("✅ Resumen de actividades por estado:")
        for estado, cantidad in actividades_por_estado.items():
            porcentaje = (cantidad / len(df_analisis)) * 100
            print(f"   - {estado.capitalize()}: {cantidad} ({porcentaje:.1f}%)")
        
        completadas = actividades_por_estado.get('completado', 0)
        pendientes = actividades_por_estado.get('pendiente', 0)
        
        print(f"\n📌 Análisis específico:")
        print(f"   - Actividades completadas: {completadas}")
        print(f"   - Actividades pendientes: {pendientes}")
        
        if pendientes > 0:
            print(f"   - Diferencia: {completadas - pendientes} más completadas")
        
        # ============================================================
        # ANÁLISIS ADICIONAL: LOGIN POR USUARIO
        # ============================================================
        print("\n" + "="*70)
        print("ANÁLISIS ADICIONAL: DISTRIBUCIÓN DE TIPOS DE ACTIVIDADES")
        print("="*70 + "\n")
        
        tipos_actividad = df_analisis['tipo_actividad'].value_counts()
        print("📋 Distribución de tipos de actividades:")
        for tipo, cantidad in tipos_actividad.items():
            porcentaje = (cantidad / len(df_analisis)) * 100
            print(f"   - {tipo.capitalize()}: {cantidad} ({porcentaje:.1f}%)")
        
        # ============================================================
        # ANÁLISIS ADICIONAL: MONTO PROMEDIO POR ESTADO
        # ============================================================
        print("\n" + "="*70)
        print("ANÁLISIS ADICIONAL: MONTO PROMEDIO POR ESTADO")
        print("="*70 + "\n")
        
        monto_por_estado = df_analisis.groupby('estado')['monto'].agg([
            ('total', 'sum'),
            ('promedio', 'mean'),
            ('cantidad', 'count')
        ]).round(2)
        
        print("💵 Montos por estado de actividad:")
        for estado in monto_por_estado.index:
            total = monto_por_estado.loc[estado, 'total']
            promedio = monto_por_estado.loc[estado, 'promedio']
            cantidad = monto_por_estado.loc[estado, 'cantidad']
            print(f"   - {estado.capitalize()}:")
            print(f"     • Monto total: ${total:,.2f}")
            print(f"     • Monto promedio: ${promedio:,.2f}")
            print(f"     • Cantidad: {int(cantidad)}")
        
        # ============================================================
        # RESUMEN FINAL
        # ============================================================
        print("\n" + "="*70)
        print("RESUMEN FINAL DEL ANÁLISIS")
        print("="*70)
        print(f"\n📊 Estadísticas generales:")
        print(f"   - Total de usuarios: {len(df_usuarios)}")
        print(f"   - Total de actividades: {len(df_actividades)}")
        print(f"   - Usuarios con actividades: {df_analisis['usuario_id'].nunique()}")
        print(f"   - Monto total procesado: ${df_analisis['monto'].sum():,.2f}")
        print(f"   - Monto promedio por actividad: ${df_analisis['monto'].mean():,.2f}")
        print(f"   - Monto máximo: ${df_analisis['monto'].max():,.2f}")
        print(f"   - Monto mínimo: ${df_analisis['monto'].min():,.2f}")
        
        print("\n✅ Análisis completado exitosamente")
        print("="*70 + "\n")
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print("Asegúrate de que los archivos CSV existan en la carpeta 'data/'")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
