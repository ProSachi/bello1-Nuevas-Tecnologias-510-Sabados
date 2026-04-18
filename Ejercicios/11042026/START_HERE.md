# 👋 BIENVENIDO - COMIENZA AQUÍ

## 🎯 ¿QUÉ ES ESTO?

Una **aplicación completa de análisis de datos en Python** que:

✅ Carga 2 archivos CSV relacionados (usuarios + actividades)  
✅ Limpia datos automáticamente (nulos, espacios, mayúsculas)  
✅ Responde **3 preguntas clave** mediante análisis avanzados  
✅ Usa **Git Flow** para gestión profesional de versiones  
✅ Incluye **documentación completa** para aprender

**Tiempo para empezar: 5 minutos**

---

## 🚀 INICIO RÁPIDO (5 PASOS)

### Paso 1: Abrir Terminal
```
Windows: Buscar "cmd" o "PowerShell"
macOS: Buscar "Terminal"
Linux: Ctrl+Alt+T
```

### Paso 2: Navegar a la carpeta del proyecto
```bash
cd /ruta/a/la/carpeta/11042026
```

### Paso 3: Crear y Activar Entorno Virtual
```bash
# Crear
python -m venv venv

# Activar
# Windows - CMD:
venv\Scripts\activate

# Windows - PowerShell:
.\venv\Scripts\Activate.ps1

# macOS/Linux:
source venv/bin/activate
```

Deberías ver `(venv)` al inicio del prompt.

### Paso 4: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 5: ¡Ejecutar!
```bash
python analisis.py
```

**Resultado esperado:** Verás un análisis completo de los datos en 30 segundos 🎉

---

## 📚 DOCUMENTACIÓN POR TIPO DE USUARIO

### 👨‍💻 Quiero Ejecutar Rápido
```
1. Sigue los 5 pasos arriba
2. Lee: EXECUTION_GUIDE.md
3. Listo para ver resultados
```

### 📖 Quiero Aprender Todo
```
1. Lee: README.md (conceptos clave)
2. Sigue: SETUP.md (instalación)
3. Ejecuta: python analisis.py
4. Entiende: EXECUTION_GUIDE.md
5. Aprende: GIT_FLOW.md (control de versiones)
```

### 🔧 Quiero Personalizar
```
1. Ejecuta: python analisis.py (baseline)
2. Edita: data_processing.py (nuevas funciones)
3. Modifica: analisis.py (nuevas preguntas)
4. Agrega tus datos en: data/
5. Ejecuta de nuevo
```

### 👥 Quiero Trabajar en Equipo
```
1. Lee: GIT_FLOW.md (flujo de trabajo)
2. Sigue: Crea rama feature/
3. Haz cambios, commit, push
4. Crea Pull Request en GitHub
5. Merge después de review
```

### 🎓 Quiero Aprender Pandas
```
1. Revisa: data_processing.py (funciones)
2. Lee comentarios en: analisis.py
3. Experimenta en: python (modo interactivo)
4. Busca: "pandas groupby examples"
5. Practica con tus datos
```

---

## 📂 ESTRUCTURA DEL PROYECTO

```
Proyecto en 3 partes:

1️⃣ DOCUMENTACIÓN (Lee primero)
   ├── README.md              ← Descripción + conceptos
   ├── SETUP.md               ← Guía de instalación
   ├── EXECUTION_GUIDE.md     ← Cómo ejecutar y ver resultados
   ├── GIT_FLOW.md            ← Control de versiones
   ├── CHEATSHEET.md          ← Comandos rápidos
   ├── INDEX.md               ← Navegación completa
   └── SETUP_HERE.md          ← Este archivo

2️⃣ CÓDIGO (Ejecutar y personalizar)
   ├── analisis.py            ← Script principal
   ├── data_processing.py     ← Módulo de limpieza
   ├── requirements.txt       ← Dependencias
   └── .gitignore             ← Archivos ignorados

3️⃣ DATOS (Tu información)
   ├── usuarios.csv           ← 500 registros de usuarios
   ├── actividades.csv        ← 250+ actividades
   └── actividades_ejemplo.json ← Ejemplo en JSON
```

---

## ❓ PREGUNTAS FRECUENTES

### ¿Cuál es el propósito?
Enseñar análisis de datos con Python, Pandas y Git Flow de forma práctica.

### ¿Necesito experiencia previa?
No. El proyecto es para principiantes. Incluye documentación detallada.

### ¿Qué aprenderé?
- Cargar datos desde CSV
- Limpiar y procesar datos (Python)
- Análisis con Pandas (groupby, merge, filtrado)
- Git y flujo de desarrollo profesional
- Documentación de proyectos

### ¿Cuánto tarda la ejecución?
- Setup (instalación): 5 minutos
- Análisis (ejecución): 30 segundos
- Total: ~6 minutos para ver resultados

### ¿Puedo ejecutarlo offline?
Sí. Una vez instalado, todo funciona sin internet.

### ¿Puedo modificar los datos?
Sí. Edita `data/usuarios.csv` o `data/actividades.csv` y vuelve a ejecutar.

### ¿Necesito GitHub?
No para ejecutar. Sí si quieres usar Git Flow profesionalmente.

### ¿Qué Python necesito?
Python 3.8 o superior. Verifica con: `python --version`

---

## 🆘 PROBLEMAS COMUNES Y SOLUCIONES

### "Python no encontrado"
```bash
# Reinstala Python desde python.org
# Asegúrate de marcar: "Add Python to PATH"
# Reinicia terminal después
```

### "ModuleNotFoundError: pandas"
```bash
# Asegúrate que venv está activo (debe haber (venv) en prompt)
pip install -r requirements.txt
```

### "File not found: data/usuarios.csv"
```bash
# Verifica que estás en la carpeta correcta
# Deberías ver estos archivos:
# - analisis.py
# - data_processing.py
# - carpeta data/

ls -la              # macOS/Linux
dir                 # Windows
```

### "venv no se activa"
```bash
# Windows PowerShell: Los scripts pueden estar deshabilitados
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1

# Luego vuelve a intentar
```

### Más problemas
→ Ve a [README.md](README.md) sección "Troubleshooting"

---

## 🎓 RESULTADOS QUE VERÁS

Cuando ejecutes `python analisis.py`, verás:

**Pregunta 1: ¿Usuario más activo?**
```
Usuario 67: Juan Pérez
Actividades: 5
Email: juan.perez@example.com
```

**Pregunta 2: ¿Montos por tipo?**
```
Pagos:  $1,234,567.89 (promedio: $5,000)
Compras: $987,654.32   (promedio: $4,000)
Logins:  $0.00         (transacciones sin monto)
```

**Pregunta 3: ¿Completadas vs Pendientes?**
```
Completadas: 200 (81.6%)
Pendientes:  45  (18.4%)
```

---

## ✅ CHECKLIST RÁPIDO

Antes de comenzar, verifica:

- [ ] Python 3.8+ instalado: `python --version`
- [ ] Terminal abierta en carpeta correcta: debes ver `analisis.py`
- [ ] 5 minutos disponibles
- [ ] Conexión a internet (para instalar pandas/numpy)

**¿Todavía no? Vuelve a [PASO 1](#paso-1-abrir-terminal)**

---

## 📞 PRÓXIMOS PASOS DESPUÉS DE EJECUTAR

```
1. ✓ Ejecutaste python analisis.py
            ↓
2. ¿Quieres entender qué viste?
            ↓
3. Lee: EXECUTION_GUIDE.md
            ↓
4. ¿Quieres aprender los conceptos?
            ↓
5. Lee: README.md
            ↓
6. ¿Quieres personalizar el código?
            ↓
7. Edita: data_processing.py
            ↓
8. ¿Quieres trabajar en equipo?
            ↓
9. Aprende: GIT_FLOW.md
            ↓
10. ¡Eres un data scientist! 🎉
```

---

## 📊 MAPA VISUAL DEL PROYECTO

```
                    ENTRADA (CSV)
                         ↓
            [usuarios.csv] + [actividades.csv]
                         ↓
                   DATA_PROCESSING.PY
                         ↓
        Limpieza: nulos, espacios, mayúsculas
        Moneda: $ → números
        Validación: emails, tipos
                         ↓
                    MERGE (unir tablas)
                         ↓
                       ANÁLISIS
        ┌─────────────┬─────────────┬─────────────┐
        ↓             ↓             ↓
   Pregunta 1    Pregunta 2    Pregunta 3
   Frecuencia    Agregación    Filtrado
   
Usuario más    Montos por    Completadas
   activo        tipo        vs Pendientes
        │             │             │
        └─────────────┴─────────────┘
                  ↓
            SALIDA (consola)
            
✓ 3 Preguntas respondidas
✓ Gráficos de datos (consola)
✓ Estadísticas finales
```

---

## 💡 DATOS IMPORTANTES

**Archivo: data/usuarios.csv**
- 500 registros de usuarios
- Columnas: id, name, avatar, correo
- Problemas: 1 nombre nulo, espacios extra, mayúsculas inconsistentes

**Archivo: data/actividades.csv**
- 250+ registros de actividades
- Columnas: id, usuario_id, tipo_actividad, fecha, estado, monto
- Problemas: nulos, espacios, símbolos $, inconsistencias de estado

**Después de limpieza:**
- 499 usuarios (1 eliminado por null)
- 245 actividades (5 eliminadas por null)
- 201 usuarios únicos con actividades

---

## 🎯 OBJETIVOS FINALES

Al completar este proyecto habrás logrado:

```
✓ Teoría: Entiendes DataFrames y venvs
✓ Práctica: Instalaste librerías y ejecutaste código
✓ Análisis: Respondiste 3 preguntas con datos reales
✓ Profesionalismo: Estructuraste proyecto con Git Flow
✓ Documentación: Creaste README y guías de uso
✓ Código: Escribiste módulos reutilizables
```

**Competencias demostradas:**
- Conocimiento de Python/Pandas
- Manejo de dependencias
- Análisis exploratorio de datos
- Buenas prácticas en Git
- Documentación profesional

---

## 🚀 ¡LISTO PARA EMPEZAR?

### Opción A: Inmediata (5 minutos)
```bash
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate
pip install -r requirements.txt
python analisis.py
```

### Opción B: Con guía (15 minutos)
1. Lee [SETUP.md](SETUP.md) (5 min)
2. Sigue los 5 pasos
3. Lee [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md)

### Opción C: Completa (40 minutos)
1. Lee [README.md](README.md) (15 min)
2. Lee [SETUP.md](SETUP.md) (5 min)
3. Ejecuta el proyecto (5 min)
4. Lee [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md) (10 min)
5. Explora [INDEX.md](INDEX.md) para más

---

## 📍 LOCALIZACIÓN DE ARCHIVOS IMPORTANTES

| Necesito... | Archivo |
|-----------|---------|
| Ejecutar el proyecto | `python analisis.py` |
| Ver conceptos clave | [README.md](README.md) |
| Entender los resultados | [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md) |
| Aprender Git | [GIT_FLOW.md](GIT_FLOW.md) |
| Comandos rápidos | [CHEATSHEET.md](CHEATSHEET.md) |
| Navegación completa | [INDEX.md](INDEX.md) |
| Mis datos | [data/usuarios.csv](data/usuarios.csv) |
| Modulo limpieza | [data_processing.py](data_processing.py) |
| Script principal | [analisis.py](analisis.py) |
| Dependencias | [requirements.txt](requirements.txt) |

---

## 📝 ÚLTIMA VERIFICACIÓN ANTES DE EMPEZAR

```bash
# Copiar y pegar cada línea en terminal:

# 1. Ver versión Python
python --version

# 2. Ver si pip funciona
pip --version

# 3. Ver carpeta actual (debe mostrar archivos del proyecto)
ls -la          # macOS/Linux
dir             # Windows

# 4. Ver contenido carpeta data/
ls -la data/    # macOS/Linux
dir data\       # Windows

# ¿Todo OK? → Listo para los 5 pasos de arriba
```

---

**🎉 ¡Bienvenido! Tu viaje de datos comienza ahora**

**Siguiente paso → [SETUP.md](SETUP.md) o directamente `python analisis.py`**

---

_Última actualización: Abril 2026 | Versión: 1.0_
