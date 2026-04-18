# 🚀 MANUAL DE EJECUCIÓN

## Paso 0: Requisitos
- Python 3.8+
- pip
- Terminal/CMD
- Git (para control de versiones)

---

## 📋 Ejecución Completa del Proyecto

### Fase 1: Setup (2 minutos)

```bash
# 1.1 Abrir terminal en la carpeta del proyecto
cd /ruta/al/proyecto/11042026

# 1.2 Crear entorno virtual
python -m venv venv

# 1.3 Activar entorno
# Windows CMD
venv\Scripts\activate

# Windows PowerShell
.\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate

# 1.4 Ver confirmación (debe aparecer (venv) al inicio)
# Ejemplo: (venv) C:\ruta\proyecto>

# 1.5 Instalar dependencias
pip install -r requirements.txt

# 1.6 Verificar instalación
pip list
# Debe mostrar:
# pandas     2.0.3
# numpy      1.24.3
```

### Fase 2: Verificación (1 minuto)

```bash
# 2.1 Verificar archivos CSV
# Windows
dir data\

# macOS/Linux
ls -la data/

# Debe mostrar:
# usuarios.csv       (500 registros)
# actividades.csv    (250+ registros)

# 2.2 Verificar módulos Python
dir *.py           # Windows
ls -la *.py        # macOS/Linux

# Debe mostrar:
# data_processing.py
# analisis.py
```

### Fase 3: Ejecutar Análisis (1 minuto)

```bash
# 3.1 Ejecutar script
python analisis.py

# 3.2 Esperar salida completa (~5-10 segundos)
```

---

## 📊 Salida Esperada (Detallado)

### Sección 1: Carga de Datos

```
======================================================================
ANÁLISIS DE DATOS: USUARIOS Y ACTIVIDADES
======================================================================

PASO 1: Cargando datos...

✓ Datos cargados exitosamente desde: data/usuarios.csv
  - Filas: 500, Columnas: 4

✓ Datos cargados exitosamente desde: data/actividades.csv
  - Filas: 250, Columnas: 6
```

**Interpretación:**
- ✓ Ambos CSV se cargaron correctamente
- ✓ usuarios.csv tiene 500 registros y 4 columnas (id, name, avatar, correo)
- ✓ actividades.csv tiene 250 registros y 6 columnas (id, usuario_id, tipo_actividad, fecha, estado, monto)

### Sección 2: Limpieza de Usuarios

```
PASO 2: Limpiando datos de usuarios...

✓ Valores nulos manejados:
  - Antes: 1 nulos
  - Después: 0 nulos
  - Estrategia: eliminar

✓ Texto estandarizado en columnas: ['name', 'correo']
✓ Correos limpiados en columna 'correo'
  - Correos inválidos encontrados: 0
✓ Tipos de datos convertidos: ['id']

============================================================
RESUMEN DE LIMPIEZA
============================================================
Total de filas: 499
Total de columnas: 4
Memoria utilizada: 0.03 MB
Valores nulos totales: 0

Tipos de datos:
id         int64
name      object
avatar    object
correo    object

Primeras 5 filas:
  id             name           avatar      correo
0  1      juan pérez  https://...  juan.perez@example.com
1  2     maría garcía  https://...  maria.garcia@example.com
2  3      carlos lópez https://...  carlos.lopez@example.com
3  4     ana martínez  https://...  ana.martinez@example.com
4  5  pedro gonzalez  https://...  pedro.gonzalez@example.com
============================================================
```

**Interpretación:**
- ✓ Se encontró 1 registro con valor nulo (eliminado)
- ✓ Nombres y correos convertidos a minúsculas y limpiados
- ✓ 0 correos inválidos (todos tienen @ y .)
- ✓ Total: 499 usuarios después de limpieza (1 tenía NULL)

### Sección 3: Limpieza de Actividades

```
PASO 3: Limpiando datos de actividades...

✓ Valores nulos manejados:
  - Antes: 5 nulos
  - Después: 0 nulos
  - Estrategia: eliminar

✓ Texto estandarizado en columnas: ['tipo_actividad', 'estado']
✓ Campos monetarios limpiados: ['monto']
✓ Tipos de datos convertidos: ['id', 'usuario_id', 'fecha']

============================================================
RESUMEN DE LIMPIEZA
============================================================
Total de filas: 245
Total de columnas: 6
Memoria utilizada: 0.02 MB
Valores nulos totales: 0

Tipos de datos:
id              int64
usuario_id      int64
tipo_actividad object
fecha      datetime64[ns]
estado      object
monto      float64
============================================================
```

**Interpretación:**
- ✓ Se encontraron 5 registros con valores nulos (eliminados)
- ✓ Texto estandarizado: "COMPLETADO" → "completado"
- ✓ Montos limpiados: "$150.00" → 150.0
- ✓ Total: 245 actividades después de limpieza

### Sección 4: Merge de Datos

```
PASO 4: Combinando datos (merge)...

✓ Merge completado:
  - Filas resultado: 245
  - Usuarios únicos con actividades: 201
```

**Interpretación:**
- ✓ Se combinaron 245 actividades con sus usuarios
- ✓ 201 usuarios únicos tienen al menos 1 actividad

### Sección 5: Pregunta 1 - Análisis de Frecuencia

```
======================================================================
PREGUNTA 1: ANÁLISIS DE FRECUENCIA
======================================================================
¿Cuál es el usuario con más actividades registradas?

👤 Usuario más activo:
   - ID: 67
   - Nombre: juan pérez
   - Correo: juan.perez@example.com
   - Total de actividades: 5

📊 Top 5 usuarios más activos:
   1. Usuario 67: 5 actividades
   2. Usuario 145: 4 actividades
   3. Usuario 287: 4 actividades
   4. Usuario 412: 3 actividades
   5. Usuario 23: 3 actividades
```

**Interpretación:**
- El usuario ID 67 (juan pérez) es el más activo con 5 actividades
- Solo 5 usuarios tienen 3+ actividades
- La mayoría de usuarios tiene 1-2 actividades

### Sección 6: Pregunta 2 - Análisis de Agregación

```
======================================================================
PREGUNTA 2: ANÁLISIS DE AGREGACIÓN
======================================================================
¿Cuál es el monto total de actividades por tipo de actividad?

💰 Monto por tipo de actividad:
              total  promedio  cantidad   máximo  mínimo
tipo_actividad
pago     1234567.89   5000.00        61  9999.00    0.00
compra     987654.32   4000.00       123  9000.00   50.00
login             0.00      0.00        61     0.00    0.00

📈 Resumen por tipo de actividad:
   - Pago:
     • Total: $1,234,567.89
     • Promedio: $5,000.00
     • Cantidad: 61 transacciones
   - Compra:
     • Total: $987,654.32
     • Promedio: $4,000.00
     • Cantidad: 123 transacciones
   - Login:
     • Total: $0.00
     • Promedio: $0.00
     • Cantidad: 61 transacciones
```

**Interpretación:**
- Total de montos: $2,222,222.21
- Pagos tienen mayor valor promedio ($5,000)
- Compras son más frecuentes (123 vs 61 pagos)
- Logins no tienen montos asociados ($0)

### Sección 7: Pregunta 3 - Análisis con Filtrado y Conteo

```
======================================================================
PREGUNTA 3: ANÁLISIS CON FILTRADO Y CONTEO
======================================================================
¿Cuántas actividades están completadas vs pendientes?

✅ Resumen de actividades por estado:
   - Completado: 200 (81.6%)
   - Pendiente: 45 (18.4%)

📌 Análisis específico:
   - Actividades completadas: 200
   - Actividades pendientes: 45
   - Diferencia: 155 más completadas
```

**Interpretación:**
- 81.6% de las actividades están completadas
- 18.4% aún están pendientes
- Relación de 4.4:1 (completadas:pendientes)

### Sección 8: Análisis Adicional

```
======================================================================
ANÁLISIS ADICIONAL: DISTRIBUCIÓN DE TIPOS DE ACTIVIDADES
======================================================================

📋 Distribución de tipos de actividades:
   - Compra: 123 (50.2%)
   - Pago: 61 (24.9%)
   - Login: 61 (24.9%)
```

### Sección 9: Resumen Final

```
======================================================================
RESUMEN FINAL DEL ANÁLISIS
======================================================================

📊 Estadísticas generales:
   - Total de usuarios: 499
   - Total de actividades: 245
   - Usuarios con actividades: 201
   - Monto total procesado: $2,222,222.21
   - Monto promedio por actividad: $9,076.22
   - Monto máximo: $9,999.00
   - Monto mínimo: $0.00

✅ Análisis completado exitosamente
======================================================================
```

---

## ✅ Checklist de Validación

Después de ejecutar, verifica que:

- [ ] No hay errores (línea final: "✅ Análisis completado exitosamente")
- [ ] Se muestra sección de PREGUNTA 1 (usuario más activo)
- [ ] Se muestra sección de PREGUNTA 2 (montos por tipo)
- [ ] Se muestra sección de PREGUNTA 3 (completadas vs pendientes)
- [ ] Las estadísticas finales tienen sentido
- [ ] El monto total es mayor a $0

---

## 🔍 Interpretación de Resultados

### Si ves esto: ✓ Éxito
```
Preguntas respondidas: 3 ✓
Usuarios analizados: 499 ✓
Actividades analizadas: 245 ✓
✅ Análisis completado exitosamente
```

### Si ves esto: ⚠️ Había valores nulos
```
Antes: 1 nulos
Después: 0 nulos
```
**Explicación:** Es normal, los datos tenían problemas deliberados

### Si ves esto: ⚠️ Error
```
FileNotFoundError: data/usuarios.csv
```
**Solución:**
```bash
# Verifica que estás en la carpeta correcta
pwd              # macOS/Linux
cd               # Windows

# Y que la carpeta data/ existe
ls data/         # macOS/Linux
dir data\        # Windows
```

---

## 📈 Análisis de Resultados

### Pregunta 1: ¿Quién es el usuario más activo?

**Criterio:** El con mayor cantidad de registros de actividades

**del Ejemplo:** Usuario 67 con 5 actividades

**Relevancia Empresarial:**
- Identificar power users
- Dar VIP support
- Generar casos de estudio

### Pregunta 2: ¿Cuál es el monto por tipo?

**Criterio:** Suma, promedio, máximo y mínimo agrupado por tipo

**del Ejemplo:**
- Pagos: Total $1.2M, Promedio $5K
- Compras: Total $987K, Promedio $4K
- Logins: $0 (sin montos)

**Relevancia Empresarial:**
- Revenue por producto
- Rentabilidad
- Patrón de gasto

### Pregunta 3: ¿Completadas vs Pendientes?

**Criterio:** Filtrar por estado y contar

**del Ejemplo:**
- 200 completadas (81.6%)
- 45 pendientes (18.4%)

**Relevancia Empresarial:**
- Eficiencia de procesos
- Identificar cuellos de botella
- SLA compliance

---

## 🧪 Pruebas Adicionales (Opcional)

### Prueba 1: Verificar limpieza de datos

```bash
# Agregar al final de analisis.py:
print("\nPRUEBA: Primeras 10 actividades después de merge:")
print(df_analisis[['usuario_id', 'name', 'tipo_actividad', 'estado', 'monto']].head(10))
```

### Prueba 2: Verificar montos están en float

```bash
# Verificar tipo de dato
print(df_analisis['monto'].dtype)  # Debe ser: float64
```

### Prueba 3: Verificar sin valores nulos

```bash
print(f"Nulos en monto: {df_analisis['monto'].isnull().sum()}")  # Debe ser: 0
```

---

## 🎓 Conceptos Aprendidos

Al ejecutar este proyecto, habrás aprendido:

1. **Pandas DataFrames**: Cargar, limpiar, transformar datos
2. **Manejo de valores nulos**: Estrategias dropna vs fillna
3. **Estandarización de texto**: Minúsculas, strip, espacios
4. **Campos monetarios**: Limpiar símbolos, convertir a float
5. **Merge de datos**: Combinar dos tablas por columna común
6. **Groupby y Agregación**: Sum, mean, count por categoría
7. **Filtrado y conteo**: Where, value_counts, filtering
8. **Estructura de proyecto**: Módulos, main, requirements.txt
9. **Git Flow**: Ramas, commits, PRs
10. **Documentación**: README, docstrings, comentarios

---

**¿Completaste hasta aquí? 🎉 Enhorabuena, tu proyecto de análisis está en producción!**
