# 🚀 CHEAT SHEET - Comandos Rápidos

## 1️⃣ ENTORNO VIRTUAL (venv)

### Crear venv
```bash
# Windows, macOS, Linux
python -m venv venv
```

### Activar venv
```bash
# Windows - CMD
venv\Scripts\activate

# Windows - PowerShell
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

### Desactivar venv
```bash
deactivate
```

### Verificar venv activo
```bash
# Debe aparecer (venv) al inicio del prompt
# Windows: (venv) C:\ruta\proyecto>
# Linux:   (venv) usuario@pc:~/proyecto$
```

---

## 2️⃣ PIP - Gestor de Paquetes

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Listar paquetes instalados
```bash
pip list
```

### Ver detalles de un paquete
```bash
pip show pandas
```

### Instalar versión específica
```bash
pip install pandas==2.0.3
pip install numpy>=1.20,<2.0
```

### Actualizar paquete
```bash
pip install --upgrade pandas
pip install -U pandas
```

### Desinstalar paquete
```bash
pip uninstall pandas -y
```

### Generar requirements.txt
```bash
pip freeze > requirements.txt
```

### Instalar desde requirements.txt
```bash
pip install -r requirements.txt
```

---

## 3️⃣ PYTHON

### Ejecutar script
```bash
python analisis.py
python -m data_processing    # Como módulo
```

### Ejecutar comando rápido
```bash
python -c "import pandas; print(pd.__version__)"
```

### Verificar versión
```bash
python --version
python -V
```

### Entrar al interactivo
```bash
python
>>> import pandas as pd
>>> pd.read_csv('data.csv')
>>> exit()
```

---

## 4️⃣ GIT - Control de Versiones

### Configuración inicial
```bash
git config user.name "Tu Nombre"
git config user.email "tu@email.com"
git config --global user.name "Tu Nombre"   # Global
```

### Inicializar repositorio
```bash
git init
```

### Estado del repositorio
```bash
git status
git log --oneline
git log --graph --all --decorate
```

### Agregar cambios
```bash
git add archivo.py          # Un archivo
git add .                   # Todos los cambios
git add data/*.csv          # Patrón
```

### Hacer commit
```bash
git commit -m "Descripción corta"
git commit -m "Título

Descripción más larga"
```

### Ver diferencias
```bash
git diff                    # Cambios no staged
git diff --staged           # Cambios staged
git diff main develop       # Entre ramas
```

---

## 5️⃣ GIT - RAMAS

### Ver ramas
```bash
git branch                  # Locales
git branch -a               # Todas (local + remoto)
git branch -v               # Con commits
```

### Crear rama
```bash
git branch feature/nueva    # Crear
git branch feature/nueva    # Y cambiar
git checkout -b feature/nueva
```

### Cambiar rama
```bash
git checkout main
git checkout develop
git checkout feature/limpieza
```

### Eliminar rama
```bash
git branch -d feature/vieja         # Local (safe)
git branch -D feature/vieja         # Local (force)
git push origin --delete feature/vieja  # Remoto
```

### Renombrar rama
```bash
git branch -m nombre-viejo nombre-nuevo
```

### Mergear rama
```bash
git merge feature/lista
git merge --no-ff feature/lista     # Sin fast-forward
git merge --squash feature/lista    # Squash commits
```

---

## 6️⃣ GIT - REMOTO (GitHub)

### Conectar a GitHub
```bash
git remote add origin https://github.com/user/repo.git
git remote -v                       # Ver remotos
```

### Push (enviar código)
```bash
git push origin main                # Rama main
git push origin develop             # Rama develop
git push origin feature/nueva       # Nueva rama
git push -u origin feature/nueva    # Tracking
git push --all                      # Todas las ramas
git push --tags                     # Tags
```

### Pull (traer código)
```bash
git pull origin main        # Actualizar mainlocal
git fetch origin            # Traer sin mergear
git rebase origin/main      # Rebase
```

### Crear pull request (en GitHub)
```
1. Push rama feature
2. GitHub mostrará: "Compare & pull request"
3. Click y describir cambios
4. Esperar review y mergear
```

---

## 7️⃣ PANDAS - Operaciones Comunes

### Cargar datos
```python
import pandas as pd
df = pd.read_csv('data/usuarios.csv')
```

### Ver datos
```python
df.head(5)          # Primeras 5 filas
df.tail(5)          # Últimas 5 filas
df.info()           # Info columnas
df.describe()       # Estadísticas
df.shape            # (filas, columnas)
```

### Limpiar datos
```python
df.dropna()                 # Eliminar nulos
df.fillna(0)                # Rellenar nulos
df.drop_duplicates()        # Eliminar duplicados
```

### Transformar datos
```python
df['columna'].str.lower()   # A minúsculas
df['columna'].str.strip()   # Quitar espacios
df['columna'] = pd.to_numeric(df['columna'])  # A número
```

### Filtrar datos
```python
df[df['edad'] > 18]         # Condición simple
df[(df['edad'] > 18) & (df['ciudad'] == 'Madrid')]  # Múltiples
df.query('edad > 18')       # Query
df.loc[0:5]                 # Por posición
df.iloc[0:5]                # Por índice
```

### Agrupar datos
```python
df.groupby('ciudad').size()             # Contar
df.groupby('ciudad')['edad'].mean()     # Promedio
df.groupby('ciudad').agg({'edad': 'mean', 'salario': 'sum'})
```

### Mergear datos
```python
df_resultado = df1.merge(df2, on='id')
df_resultado = df1.merge(df2, left_on='id', right_on='user_id')
df_resultado = pd.concat([df1, df2], axis=1)  # Concatenar
```

### Exportar datos
```python
df.to_csv('resultado.csv', index=False)
df.to_json('resultado.json')
df.to_excel('resultado.xlsx')
```

---

## 8️⃣ ARCHIVOS Y CARPETAS

### Listar contenido
```bash
# Windows
dir                 # Listar carpeta actual
dir data\           # Listar carpeta data
ls -l data/         # Equivalente a Linux

# macOS / Linux
ls                  # Listar carpeta actual
ls -la data/        # Listar con detalles
tree                # Árbol de carpetas
```

### Crear carpeta
```bash
# Windows
mkdir data
mkdir data\backups

# macOS / Linux
mkdir data
mkdir -p data/backups   # Crear padres
```

### Cambiar directorio
```bash
cd datos            # Entrar a carpeta
cd ..               # Ir a padre
cd ~                # Ir a home
cd /ruta/absoluta   # Ruta absoluta
pwd                 # Ver ruta actual
```

### Copiar/Mover
```bash
# Windows
copy archivo.txt archivo_copia.txt
move archivo.txt otra_carpeta\

# macOS / Linux
cp archivo.txt archivo_copia.txt
mv archivo.txt otra_carpeta/
```

### Ver contenido archivo
```bash
# Windows
type README.md      # Ver contenido

# macOS / Linux
cat README.md       # Ver contenido
less README.md      # Ver paginado
head -5 README.md   # Primeras 5 líneas
tail -5 README.md   # Últimas 5 líneas
```

---

## 9️⃣ ATAJOS ÚTILES

### Python + venv en 1 línea
```bash
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

### Ejecutar sin activar venv (Windows)
```bash
venv\Scripts\python.exe analisis.py
```

### Crear y cambiar a rama rápido
```bash
git checkout -b feature/tarea && git push -u origin feature/tarea
```

### Ver commits recientes
```bash
git log --oneline -10 --graph
```

### Deshacer último commit (cuidado!)
```bash
git reset --soft HEAD~1     # Mantiene cambios
git reset --hard HEAD~1     # Pierde cambios
```

### Limpiar pycache
```bash
# Windows
rmdir __pycache__ /s

# macOS / Linux
rm -rf __pycache__
find . -type d -name __pycache__ -exec rm -r {} +
```

---

## 🔟 ATAJOS DE TERMINAL

### Navegación rápida
```bash
.               # Carpeta actual
..              # Carpeta padre
~               # Home del usuario
-               # Carpeta anterior
*               # Cualquier archivo (wildcard)
```

### Comandos útiles
```bash
clear           # Limpiar pantalla
history         # Ver historial comandos
which python    # Ver dónde está python
whereis python  # Búsqueda más profunda
echo $PATH      # Ver variable PATH
```

### Permisos (Linux/macOS)
```bash
chmod +x script.py      # Ejecutable
chmod 755 script.py     # rwx r-x r-x
chmod 644 archivo.txt   # rw- r-- r--
```

---

## 📊 PANDAS CHEAT SHEET COMPRIMIDO

```python
import pandas as pd
import numpy as np

# CARGAR
df = pd.read_csv('file.csv')
df = pd.read_json('file.json')
df = pd.read_excel('file.xlsx')

# EXPLORAR
df.shape, df.dtypes, df.info(), df.describe()
df.head(), df.tail(), df.sample()

# LIMPIAR
df.dropna(), df.fillna(value), df.drop_duplicates()

# TRANSFORMAR
df['col'].str.lower(), df['col'].astype('int64')
df['col'] = df['col'].apply(lambda x: x*2)

# FILTRAR
df[df['col'] > 5]
df.query('col > 5')
df.loc[0:5]

# AGRUPAR
df.groupby('col1').size()
df.groupby('col1')['col2'].agg(['sum', 'mean', 'count'])

# MERGEAR
df1.merge(df2, on='key')
pd.concat([df1, df2])

# EXPORTAR
df.to_csv('out.csv', index=False)
df.to_json('out.json')
```

---

## ⚡ ORDEN DE SIEMPRE

```bash
# 1. Crear venv
python -m venv venv

# 2. Activar venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar proyecto
python analisis.py

# 5. Si cambias código, hacer commit
git add .
git commit -m "Descripción cambio"
git push origin nombre-rama
```

---

## 🆘 SOLUCIONES RÁPIDAS

| Problema | Solución |
|----------|----------|
| "ModuleNotFoundError: pandas" | `pip install pandas` |
| "No such file: data.csv" | `ls data/` (verificar archivo existe) |
| "venv no se activa" | Verifica path, intenta: `python -m venv venv` |
| "Puerto ocupado" | Cambiar puerto o matar proceso |
| "Merge conflict" | Editar archivo, resolver, `git add`, `git commit` |
| Git no funciona | `git config user.name/email` |
| Python no encontrado | Reinstalar Python, asegurar está en PATH |

---

**Imprime este archivo o guárdalo como referencia** 📌

**Última actualización:** Abril 2026
