# Análisis de Datos: Usuarios y Actividades

## Descripción del Proyecto

Este proyecto es una aplicación de análisis de datos que carga información de usuarios y sus actividades desde archivos CSV, realiza una limpieza exhaustiva de los datos (incluyendo manejo de valores nulos, estandarización de texto y limpieza de campos monetarios), y responde preguntas clave mediante análisis de frecuencia, agregación y filtrado.

### Características principales

- **Limpieza de datos robusta**: Manejo de valores nulos, espacios extra, inconsistencias de texto
- **Procesamiento de múltiples archivos**: Carga y merge de datos relacionados (usuarios + actividades)
- **Análisis integral**: Responde 3 preguntas de negocio mediante operaciones groupby, merge y filtrado
- **Módulo reutilizable**: El módulo `data_processing.py` puede usarse en otros proyectos
- **Documentación completa**: Código comentado y docstrings descriptivos

### Preguntas de Análisis Respondidas

1. **Análisis de Frecuencia**: ¿Cuál es el usuario con más actividades registradas?
2. **Análisis de Agregación**: ¿Cuál es el monto total de actividades por tipo de actividad?
3. **Análisis con Filtrado y Conteo**: ¿Cuántas actividades están completadas vs pendientes?

---

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Acceso a terminal/CMD

---

## Instalación y Configuración

### 1. Clonar o descargar el proyecto

```bash
# Si está en GitHub
git clone <url-del-repositorio> analisis-datos
cd analisis-datos
```

### 2. Crear un Entorno Virtual

**En Windows (CMD):**

```bash
python -m venv venv
venv\Scripts\activate
```

**En Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Deberías ver `(venv)` al inicio de la línea de comando. Esto indica que el entorno virtual está activo.

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

Este comando instalará:
- **pandas**: Para manipulación de datos
- **numpy**: Para operaciones numéricas

Puedes verificar la instalación con:

```bash
pip list
```

---

## Estructura del Proyecto

```
analisis-datos/
├── venv/                    # Entorno virtual (no se sube a Git)
├── data/                    # Carpeta con archivos de datos
│   ├── usuarios.csv         # 500 registros de usuarios
│   └── actividades.csv      # 500+ registros de actividades
├── data_processing.py       # Módulo de limpieza y procesamiento
├── analisis.py              # Script principal de análisis
├── requirements.txt         # Dependencias del proyecto
├── .gitignore               # Archivos a ignorar en Git
└── README.md                # Este archivo
```

### Descripción de archivos principales

**`data_processing.py`**: Módulo con funciones de limpieza
- `cargar_datos()`: Carga CSV en DataFrame
- `manejar_valores_nulos()`: Elimina o rellena nulos
- `estandarizar_texto()`: Minúsculas, quita espacios
- `limpiar_campos_monetarios()`: Elimina símbolos $ y convierte a número
- `convertir_tipos_datos()`: Convierte tipos de columnas
- `limpiar_correos()`: Valida y estandariza emails
- `eliminar_duplicados()`: Remueve filas duplicadas

**`analisis.py`**: Script principal que:
1. Carga datos desde CSV
2. Limpia y procesa usuarios
3. Limpia y procesa actividades
4. Realiza merge de datos
5. Genera análisis y responde preguntas

**`data/usuarios.csv`**: 500 registros con problemas deliberados:
- Valores nulos en la columna 'name'
- Espacios extra en URLs y correos
- Inconsistencias en mayúsculas

**`data/actividades.csv`**: 500+ registros con problemas deliberados:
- Valores nulos en la columna 'usuario_id'
- Espacios extra en campos
- Símbolos $ en montos
- inconsistencias en estado ('completado', 'COMPLETADO', 'pendiente')

---

## Uso

### Ejecutar el Script de Análisis

Una vez activado el entorno virtual e instaladas las dependencias:

**En Windows:**

```bash
python analisis.py
```

**En macOS/Linux:**

```bash
python3 analisis.py
```

### Salida Esperada

El script mostrará:

1. **Información de carga**: Cantidad de filas y columnas
2. **Proceso de limpieza**: Nulos manejados, texto estandarizado, etc.
3. **Resultados de análisis**:
   - Usuario más activo
   - Montos por tipo de actividad
   - Estado de actividades (completadas vs pendientes)
4. **Estadísticas finales**: Totales y promedios

Ejemplo de salida:

```
======================================================================
ANÁLISIS DE DATOS: USUARIOS Y ACTIVIDADES
======================================================================

PASO 1: Cargando datos...

✓ Datos cargados exitosamente desde: data/usuarios.csv
  - Filas: 500, Columnas: 4

...

======================================================================
PREGUNTA 1: ANÁLISIS DE FRECUENCIA
======================================================================
¿Cuál es el usuario con más actividades registradas?

👤 Usuario más activo:
   - ID: 5
   - Nombre: juan pérez
   - Correo: juan.perez@example.com
   - Total de actividades: 5

...
======================================================================
RESUMEN FINAL DEL ANÁLISIS
======================================================================

📊 Estadísticas generales:
   - Total de usuarios: 500
   - Total de actividades: 250
   - Usuarios con actividades: 248
   - Monto total procesado: $1,234,567.89
   - Monto promedio por actividad: $4,938.27
   ...

✅ Análisis completado exitosamente
======================================================================
```

---

## Explicación de Conceptos Clave

### ¿Qué es un DataFrame?

Un **DataFrame** es una estructura de datos de pandas similar a una tabla de Excel o base de datos SQL:
- Tiene filas (registros) y columnas (campos)
- Cada columna puede tener un tipo de dato diferente (texto, número, fecha, etc.)
- Permite hacer operaciones complejas como filtrado, agregación, merge, etc.

### ¿Por qué usar Entornos Virtuales?

Un **entorno virtual** es un directorio con una copia aislada de Python y sus librerías:

**Ventajas:**
- ✅ Evita conflictos de versiones entre proyectos
- ✅ Facilita reproducibilidad en diferentes máquinas
- ✅ No interfiere con Python del sistema
- ✅ Fácil de eliminar sin afectar el sistema

**Ejemplo de conflicto sin venv:**

```
Proyecto A necesita: pandas 2.0
Proyecto B necesita: pandas 1.5
Sin venv: Imposible tener ambos al mismo tiempo
Con venv: Cada proyecto tiene su propia versión
```

### Operaciones de Pandas Utilizadas

1. **Carga**: `pd.read_csv()` - Lee archivos CSV
2. **Limpieza**: `.dropna()`, `.fillna()`, `.apply()` - Maneja nulos y transforma datos
3. **Transformación**: `.groupby()` - Agrupa y resume datos
4. **Merge**: `.merge()` - Combina dos DataFrames por columna común
5. **Filtrado**: `.loc[]`, `.query()` - Selecciona filas según condiciones
6. **Agregación**: `.sum()`, `.mean()`, `.count()` - Calcula estadísticas

---

## Gestión de Git y Workflow

### Estructura de Ramas

```
main (rama principal protegida)
 ↑
develop (rama de desarrollo)
 ↑
feature/limpieza-datos (ramas de features)
feature/analisis-usuarios
release/analisis-v1 (rama de release)
```

### Flujo de Trabajo Recomendado

1. **Crear rama de feature** desde develop:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/nueva-funcionalidad
   ```

2. **Hacer cambios y commit**:
   ```bash
   git add .
   git commit -m "Descripción clara del cambio"
   ```

3. **Push y Pull Request**:
   ```bash
   git push origin feature/nueva-funcionalidad
   # Luego crear PR en GitHub desde feature → develop
   ```

4. **Merge a develop y luego a main**:
   ```bash
   # En GitHub, merge la PR
   # Crear release branch para versión final
   git checkout -b release/analisis-v1
   ```

### Archivo .gitignore

El archivo `.gitignore` evita que se suban a GitHub:
- `venv/` - Todo el entorno virtual
- `__pycache__/` - Archivos de caché de Python
- `*.pyc` - Archivos compilados
- `.DS_Store` - Archivos del sistema macOS
- `*.log` - Archivos de log

---

## Troubleshooting

### "No module named 'pandas'"

```bash
# Asegúrate de que el venv esté activo (deberías ver (venv) en el prompt)
# Reinstala las dependencias
pip install -r requirements.txt
```

### "ModuleNotFoundError: No module named 'data_processing'"

```bash
# Asegúrate de estar en la carpeta raíz del proyecto
# El script debe estar en el mismo directorio que data_processing.py
cd /ruta/del/proyecto
python analisis.py
```

### "FileNotFoundError: data/usuarios.csv"

```bash
# Verifica que la carpeta 'data/' existe y tiene los archivos CSV
ls -l data/           # En Linux/macOS
dir data\             # En Windows
```

### El entorno virtual no se activa

**Windows (CMD):**
```bash
# Si da error de permisos
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
# Intenta con source
source venv/bin/activate

# O si está en zsh
. venv/bin/activate
```

---

## Glosario de Términos

| Término | Definición |
|---------|-----------|
| **DataFrame** | Estructura de datos bidimensional (tabla) en pandas |
| **venv** | Entorno virtual de Python |
| **pip** | Gestor de paquetes de Python |
| **CSV** | Formato de archivo de valores separados por coma |
| **Merge** | Combinar dos DataFrames basado en una columna común |
| **groupby** | Agrupar datos por una o más columnas |
| **iloc** | Indexación por posición en pandas |
| **NaN/null** | Valor faltante o nulo |
| **Git Flow** | Rama de desarrollo que sigue un patrón estructurado |

---

## Evaluación (Rúbrica)

### Conocimiento (Conceptos)
- ✓ Explicar qué es un DataFrame y sus operaciones
- ✓ Explicar por qué se usan entornos virtuales
- ✓ Entender merge, groupby y filtrado de pandas

### Desempeño (Habilidades)
- ✓ Instalar librerías con pip
- ✓ Gestionar dependencias en requirements.txt
- ✓ Crear y activar venv
- ✓ Usar Git Flow correctamente

### Producto (Entrega)
- ✓ Script `.py` sin errores de sintaxis
- ✓ Repositorio GitHub con estructura correcta
- ✓ Rama main protegida, develop y features
- ✓ Pull Requests documentadas
- ✓ README.md completo

---

## Contacto y Soporte

Para preguntas o problemas:
1. Revisa el apartado de Troubleshooting
2. Consulta la documentación de [pandas](https://pandas.pydata.org/docs/)
3. Revisa el código comentado en `data_processing.py` y `analisis.py`

---

**Última actualización**: Abril 2026

**Versión**: 1.0 (release/analisis-v1)

**Estado**: ✅ Production Ready
