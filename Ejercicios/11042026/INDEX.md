# 📚 ÍNDICE DEL PROYECTO

## Contenido Completo

### 📖 Documentación Principal

1. **[README.md](README.md)** ← EMPEZAR AQUÍ
   - Descripción completa del proyecto
   - Requisitos y instalación detallada
   - Explicación de conceptos clave (DataFrame, venv)
   - Troubleshooting
   - Estructura Git Flow
   - Duración: 15-20 minutos de lectura

2. **[SETUP.md](SETUP.md)** ← Guía Rápida
   - Setup en 5 pasos (5 minutos)
   - Comandos esenciales
   - Problemas comunes y soluciones
   - Estructura de carpetas
   - Checklist de verificación
   - Duración: 5-10 minutos

3. **[EXECUTION_GUIDE.md](EXECUTION_GUIDE.md)** ← Manual de Ejecución
   - Paso a paso de ejecución
   - Salida esperada con interpretación
   - Validación de resultados
   - Análisis de cada pregunta
   - Pruebas adicionales
   - Duración: 10-15 minutos de ejecución

4. **[GIT_FLOW.md](GIT_FLOW.md)** ← Git Flow Completo
   - Estructura de ramas (main, develop, feature, release)
   - Flujos de trabajo típicos
   - Comandos Git esenciales
   - Convenciones de commits
   - Pull Requests
   - Protección de ramas
   - Duración: 20-30 minutos de lectura

### 💾 Código Fuente

5. **[data_processing.py](data_processing.py)** - Módulo de Limpieza
   ```
   Funciones principales:
   ├── cargar_datos()              → Carga CSV en DataFrame
   ├── manejar_valores_nulos()     → Elimina o rellena NaN
   ├── estandarizar_texto()        → Minúsculas + trim
   ├── limpiar_campos_monetarios() → Elimina $ y convierte
   ├── convertir_tipos_datos()     → Convierte tipos
   ├── limpiar_correos()           → Valida emails
   ├── eliminar_duplicados()       → Remueve duplicates
   ├── obtener_estadisticas_limpieza() → Retorna stats
   └── resumen_limpieza()          → Imprime resumen
   ```

6. **[analisis.py](analisis.py)** - Script Principal
   ```
   Flujo:
   ├── PASO 1: Cargar datos (usuarios + actividades)
   ├── PASO 2: Limpiar usuarios
   ├── PASO 3: Limpiar actividades
   ├── PASO 4: Merge de datos
   ├── PREGUNTA 1: Usuario más activo
   ├── PREGUNTA 2: Montos por tipo de actividad
   ├── PREGUNTA 3: Actividades completadas vs pendientes
   ├── ANÁLISIS ADICIONAL 1: Distribución de tipos
   ├── ANÁLISIS ADICIONAL 2: Montos por estado
   └── RESUMEN FINAL: Estadísticas generales
   ```

### 📊 Datos

7. **[data/usuarios.csv](data/usuarios.csv)** - 500+ registros
   ```
   Columnas: id, name, avatar, correo
   Problemas deliberados:
   ├── 1 valor nulo en 'name'
   ├── Espacios extra en URLs y correos
   ├── Inconsistencias en mayúsculas
   └── Emails con formateo inconsistente
   ```

8. **[data/actividades.csv](data/actividades.csv)** - 250+ registros
   ```
   Columnas: id, usuario_id, tipo_actividad, fecha, estado, monto
   Problemas deliberados:
   ├── Valores nulos en 'usuario_id'
   ├── Espacios extra en campos
   ├── Símbolos $ en montos
   ├── Inconsistencias: "COMPLETADO" vs "completado"
   └── Fechas en formato mixto
   ```

9. **[data/actividades_ejemplo.json](data/actividades_ejemplo.json)** - Ejemplo alterno
   ```
   Formato JSON con 5 registros de ejemplo
   (Demuestra extensibilidad del proyecto a múltiples formatos)
   ```

### ⚙️ Configuración

10. **[requirements.txt](requirements.txt)** - Dependencias
    ```
    pandas==2.0.3
    numpy==1.24.3
    ```

11. **[.gitignore](.gitignore)** - Archivos ignorados
    ```
    venv/              ← No subir entorno virtual
    __pycache__/       ← No subir caché de Python
    *.pyc              ← No subir compilados
    *.log              ← No subir logs
    .DS_Store          ← No subir archivos macOS
    ```

### 🚀 Automation

12. **[init_gitflow.bat](init_gitflow.bat)** - Script de inicialización Git
    ```
    Automatiza:
    ├── git init
    ├── Crear rama develop
    ├── Crear ramas feature/
    ├── Crear rama release/
    └── Listar ramas
    ```

---

## 🗺️ Mapa de Aprendizaje

### Para Principiantes (Si vas a empezar)

**Recomendación de lectura:**

```
1. SETUP.md (5 min)
   ↓
2. Ejecuta: python analisis.py (5 min)
   ↓
3. EXECUTION_GUIDE.md (15 min)
   ↓
4. README.md - Secciones sobre DataFrame y venv (10 min)
   ↓
5. Explora el código: data_processing.py + analisis.py (20 min)
   ↓
6. GIT_FLOW.md (cuando necesites Git) (30 min)

Total: ~85 minutos
```

### Para Usuarios Intermedios (Quieres personalizar)

```
1. EXECUTION_GUIDE.md (10 min)
   ↓
2. Revisa data_processing.py (10 min)
   ↓
3. Edita analisis.py con nuevas preguntas
   ↓
4. Agrega tus datos CSV en data/
   ↓
5. Ejecuta python analisis.py
   ↓
6. GIT_FLOW.md para gestionar cambios (20 min)

Total: ~60 minutos
```

### Para Usuarios Avanzados (Quieres aportar)

```
1. Lee todos los comentarios en el código (15 min)
   ↓
2. GIT_FLOW.md - Todo sobre workflow (30 min)
   ↓
3. Crea nuevas funciones en data_processing.py
   ↓
4. Crea feature branch: git checkout -b feature/mi-mejora
   ↓
5. Develop, test, commit con buenos mensajes
   ↓
6. Push + Pull Request en GitHub

Total: ~60 minutos de setup + tu tiempo en código
```

---

## 🎯 Preguntas Que Responde Este Proyecto

### Pregunta 1: Análisis de Frecuencia
**¿Cuál es el usuario con más actividades registradas?**

**Técnica:** `value_counts()` + orden descendente
**Archivo:** analisis.py (líneas 115-147)

### Pregunta 2: Análisis de Agregación
**¿Cuál es el monto total de actividades por tipo?**

**Técnica:** `groupby()` + `agg()`
**Archivo:** analisis.py (líneas 150-185)

### Pregunta 3: Análisis con Filtrado y Conteo
**¿Cuántas actividades están completadas vs pendientes?**

**Técnica:** Filtrado + `value_counts()`
**Archivo:** analisis.py (líneas 188-213)

---

## 🔄 Flujo de Uso Típico

```
┌─────────────────────────────────────────────────────┐
│ USUARIO DESCARGA EL PROYECTO                        │
└─────────────────────────────────────────────────────┘
                      ↓
        Lee SETUP.md (5 minutos)
                      ↓
┌─────────────────────────────────────────────────────┐
│ python -m venv venv                                 │
│ venv\Scripts\activate (o source en Linux/macOS)     │
│ pip install -r requirements.txt                     │
└─────────────────────────────────────────────────────┘
                      ↓
        python analisis.py (1 minuto)
                      ↓
┌─────────────────────────────────────────────────────┐
│ ✓ Análisis completado exitosamente                  │
│ ✓ 3 preguntas respondidas                           │
│ ✓ Datos limpios y procesados                        │
└─────────────────────────────────────────────────────┘
                      ↓
        Lee EXECUTION_GUIDE.md
        para entender resultados
                      ↓
  ¿Quieres aprender Git Flow?
           ↙              ↘
         Sí               No
        ↓                 ↓
  Lee GIT_FLOW.md    Personaliza el
                     código
                     ↓
                Google "pandas
                 groupby" etc.
                     ↓
        Agrega tus datos
        Escribe nuevas
        funciones
                     ↓
┌─────────────────────────────────────────────────────┐
│ ¡Proyecto personalizado listo para producción!      │
└─────────────────────────────────────────────────────┘
```

---

## 📋 Validación de Entrega

Antes de presentar tu proyecto, verifica:

```
✓ ESTRUCTURA
├── [x] README.md (documentación completa)
├── [x] data_processing.py (módulo limpieza)
├── [x] analisis.py (script principal)
├── [x] requirements.txt (dependencias)
├── [x] .gitignore (ignora venv)
└── [x] data/usuarios.csv + actividades.csv

✓ FUNCIONALIDAD
├── [x] Script ejecuta sin errores: python analisis.py
├── [x] Pregunta 1 respondida (usuario más activo)
├── [x] Pregunta 2 respondida (montos por tipo)
├── [x] Pregunta 3 respondida (completadas vs pendientes)
└── [x] Estadísticas finales con sentido

✓ GIT
├── [x] Repositorio inicializado: git init
├── [x] Rama main protegida
├── [x] Rama develop para desarrollo
├── [x] Ramas feature/ para funcionalidades
├── [x] Rama release/ para versiones
└── [x] .gitignore previene subir venv/

✓ DOCUMENTACIÓN
├── [x] README.md explica qué y cómo
├── [x] SETUP.md guía rápida de instalación
├── [x] EXECUTION_GUIDE.md paso a paso
├── [x] GIT_FLOW.md explica workflow
├── [x] Código comentado con docstrings
└── [x] requirements.txt actualizado

✓ DATOS
├── [x] usuarios.csv: 500+ registros
├── [x] actividades.csv: 250+ registros
├── [x] Datos relacionados (merge posible)
├── [x] Problemas deliberados (nulos, espacios, mayúsculas)
└── [x] Formato CSV limpio
```

---

## 🆘 Ayuda Rápida

| Necesito... | Archivo | Sección |
|-----------|---------|---------|
| Instalar el proyecto | SETUP.md | Paso 1-3 |
| Ejecutar análisis | SETUP.md / EXECUTION_GUIDE.md | Paso 4 |
| Entender resultados | EXECUTION_GUIDE.md | Salida esperada |
| Aprender Git | GIT_FLOW.md | Todo |
| Personalizar código | README.md → data_processing.py | Funciones |
| Agregar datos | data/ → usuarios.csv o actividades.csv | Copiar formato |
| Solucionar problemas | README.md | Troubleshooting |

---

## 🎓 Competencias Demostradas

```
☑ CONOCIMIENTO (Conceptos)
├── [x] Qué es un DataFrame
├── [x] Por qué usar venv
├── [x] Operaciones pandas: merge, groupby, filtrado
└── [x] Estructuras de proyecto profesional

☑ DESEMPEÑO (Habilidades)
├── [x] pip y requirements.txt
├── [x] Crear y activar venv
├── [x] Escribir módulos reutilizables
├── [x] Usar Git y GitHub
└── [x] Documentar proyectos

☑ PRODUCTO (Entrega)
├── [x] Script Python funcional (0 errores)
├── [x] Datos bien estructurados
├── [x] README.md profesional
├── [x] Git Flow implementado
└── [x] Respuestas a 3+ preguntas de análisis
```

---

## 📞 Próximos Pasos Sugeridos

1. **Domina el proyecto actual**
   - Ejecuta varias veces
   - Cambia datos de entrada
   - Agrega nuevas preguntas

2. **Aprende más de Pandas**
   - Lee documentación oficial
   - Experimenta con `.pivot_table()`
   - Intenta visualizaciones con `matplotlib`

3. **Domina Git Flow**
   - Crea ramas locales
   - Practica merges
   - Crea un PR real en GitHub

4. **Expande el proyecto**
   - Agrega validación de datos
   - Implementa logging
   - Crea testes unitarios
   - Exporta resultados a HTML/PDF

5. **Publica en GitHub**
   - Crea repositorio público
   - Agrega badge de estado
   - Pide pull requests
   - Documenta cómo contribuir

---

## 📊 Estadísticas del Proyecto

```
Líneas de código:
├── data_processing.py: ~300 líneas
├── analisis.py: ~400 líneas
├── Total: ~700 líneas de código

Documentación:
├── README.md: ~500 líneas
├── GIT_FLOW.md: ~400 líneas
├── SETUP.md: ~200 líneas
├── EXECUTION_GUIDE.md: ~400 líneas
├── Este archivo: ~800 líneas
└── Total: ~2,300 líneas de documentación

Datos:
├── usuarios.csv: 500 registros
├── actividades.csv: 250+ registros
└── Total: 750+ registros

Funciones de limpieza:
├── cargar_datos()
├── manejar_valores_nulos()
├── estandarizar_texto()
├── limpiar_campos_monetarios()
├── convertir_tipos_datos()
├── limpiar_correos()
├── eliminar_duplicados()
├── obtener_estadisticas_limpieza()
└── Total: 8 funciones

Preguntas de análisis:
├── Pregunta 1: Frecuencia
├── Pregunta 2: Agregación
├── Pregunta 3: Filtrado y conteo
├── Análisis adicional 1: Distribución tipos
├── Análisis adicional 2: Montos por estado
└── Total: 5 análisis
```

---

**🎉 ¿Listo para empezar? Comienza con [SETUP.md](SETUP.md)**

**¿Quieres entender qué hace? Lee [README.md](README.md)**

**¿Necesitas ejecutar y validar? Usa [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md)**

**¿Trabajarás en equipo con Git? Aprende [GIT_FLOW.md](GIT_FLOW.md)**
