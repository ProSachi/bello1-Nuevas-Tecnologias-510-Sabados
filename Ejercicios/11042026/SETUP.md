# GUÍA RÁPIDA: CONFIGURACIÓN Y EJECUCIÓN

## ⚡ 5 Pasos para Empezar (5 minutos)

### Paso 1: Crear y Activar Entorno Virtual

**Windows (CMD):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 2: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 3: Verificar Instalación
```bash
python -c "import pandas; print('✓ Pandas instalado')"
python -c "import numpy; print('✓ NumPy instalado')"
```

### Paso 4: Ejecutar el Análisis
```bash
python analisis.py
```

### Paso 5: Ver Resultados
La consola mostrará:
- ✓ Datos cargados
- ✓ Limpieza completada
- ✓ Resultados de análisis
- ✓ Estadísticas finales

---

## 📁 Estructura de Carpetas

```
proyecto/
├── venv/                 ← Entorno virtual (ignorado en Git)
├── data/
│   ├── usuarios.csv      ← 500 registros
│   └── actividades.csv   ← 250+ registros
├── data_processing.py    ← Módulo de limpieza
├── analisis.py           ← Script principal
├── requirements.txt      ← Dependencias
├── .gitignore
├── README.md
└── init_gitflow.bat      ← Script para Git Flow
```

---

## 🔍 Verificar Estructura

**Windows:**
```bash
dir
dir data\
```

**macOS/Linux:**
```bash
ls -la
ls -la data/
```

Deberías ver:
- ✓ data_processing.py
- ✓ analisis.py
- ✓ carpeta data/ con .csv
- ✓ requirements.txt
- ✓ README.md
- ✓ .gitignore

---

## 🐛 Problemas Comunes

### "ModuleNotFoundError: No module named 'pandas'"

**Solución:**
```bash
# 1. Verifica que venv está activo (debes ver (venv) en el prompt)
# 2. Reinstala
pip install pandas numpy
```

### "FileNotFoundError: data/usuarios.csv"

**Solución:**
```bash
# Verifica que estás en la carpeta correcta
pwd              # macOS/Linux
cd               # Windows

# Y que existen los archivos
ls data/         # macOS/Linux
dir data\        # Windows
```

### "Permission denied" en macOS/Linux

**Solución:**
```bash
chmod +x analisis.py
python analisis.py
```

---

## 📊 Salida Esperada

```
======================================================================
ANÁLISIS DE DATOS: USUARIOS Y ACTIVIDADES
======================================================================

PASO 1: Cargando datos...

✓ Datos cargados exitosamente desde: data/usuarios.csv
  - Filas: 500, Columnas: 4

✓ Datos cargados exitosamente desde: data/actividades.csv
  - Filas: 250, Columnas: 6

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
PREGUNTA 1: ANÁLISIS DE FRECUENCIA
============================================================
¿Cuál es el usuario con más actividades registradas?

👤 Usuario más activo:
   - ID: 5
   - Nombre: juan pérez
   - Correo: juan.perez@example.com
   - Total de actividades: 5

📊 Top 5 usuarios más activos:
   1. Usuario 5: 5 actividades
   2. Usuario 67: 4 actividades
   ...

============================================================
PREGUNTA 2: ANÁLISIS DE AGREGACIÓN
============================================================
¿Cuál es el monto total de actividades por tipo de actividad?

💰 Monto por tipo de actividad:
                total    promedio  cantidad  máximo  mínimo
tipo_actividad
pago      1234567.89   5000.00        247  9999.00    0.00
compra      987654.32   4000.00        246  9000.00   50.00
login            0.00      0.00        247     0.00    0.00
...

============================================================
RESUMEN FINAL DEL ANÁLISIS
============================================================

📊 Estadísticas generales:
   - Total de usuarios: 500
   - Total de actividades: 250
   - Usuarios con actividades: 248
   - Monto total procesado: $2,222,222.21
   - Monto promedio por actividad: $8,888.89
   - Monto máximo: $9,999.00
   - Monto mínimo: $0.00

✅ Análisis completado exitosamente
======================================================================
```

---

## 🚀 Git Flow Setup (Opcional pero Recomendado)

### Opción 1: Automático (Windows)
```bash
init_gitflow.bat
```

### Opción 2: Manual

```bash
# 1. Inicializar git
git init
git add .
git commit -m "Initial commit"

# 2. Crear rama develop
git branch develop

# 3. Crear ramas de feature
git checkout -b feature/limpieza-datos
git checkout develop
git merge feature/limpieza-datos

# 4. Crear rama release
git checkout -b release/analisis-v1

# 5. Ver ramas
git branch -a
```

### 5. Conectar a GitHub

```bash
# Copiar la URL de tu repo GitHub
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git branch -M main    # Rename master a main si es necesario
git push -u origin main
git push -u origin develop
git push -u origin release/analisis-v1
```

---

## ✅ Checklist de Verificación

- [ ] Entorno virtual creado: `venv/Scripts/activate` o `. venv/bin/activate`
- [ ] Dependencias instaladas: `pip list` (debe mostrar pandas y numpy)
- [ ] Archivos CSV existen en `data/` (usuarios.csv y actividades.csv)
- [ ] Script ejecuta sin errores: `python analisis.py`
- [ ] Salida muestra 3 preguntas de análisis
- [ ] Git inicializado con ramas (main, develop, features, release)
- [ ] README.md presente con documentación completa
- [ ] .gitignore ignora venv y __pycache__

---

## 📚 Conceptos Clave Explicados

### DataFrame de Pandas
Tabla de datos bidimensional con:
- Filas (índice): cada fila es un registro
- Columnas: cada columna es un campo/atributo
- Tipos de datos: int, float, str, datetime, etc.

```python
import pandas as pd
df = pd.read_csv('data.csv')  # Cargar
df['columna'].sum()            # Sumar
df.groupby('categoria').mean() # Agrupar
```

### Entorno Virtual (venv)
Copia aislada de Python + librerías para cada proyecto:
- Evita conflictos de versiones
- Reproducible en otras máquinas
- Fácil de eliminar (solo borrar carpeta)

### Git Flow
Sistema de ramas estructurado:
- `main`: Código en producción (protegido)
- `develop`: Rama de desarrollo
- `feature/`: Nuevas funcionalidades
- `release/`: Preparación de versiones

---

## 🎯 Prácticas Recomendadas

1. **Siempre usar venv** para aislar dependencias
2. **Activar venv antes de trabajar** en el proyecto
3. **Actualizar requirements.txt** cuando instalas librerías nuevas
4. **Hacer commits pequeños** y descriptivos
5. **Usar feature branches** para nuevas funcionalidades
6. **Proteger rama main** en GitHub
7. **Documentar cambios** en commits y PRs

---

**¿Listo para empezar? → `python analisis.py`** 🚀
