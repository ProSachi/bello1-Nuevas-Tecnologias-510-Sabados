# 📚 GUÍA DE GIT FLOW PARA EL PROYECTO

## Resumen Ejecutivo

Git Flow es un modelo de desarrollo estructurado que utiliza múltiples ramas:

```
main (producción)
 ↑
develop (desarrollo)
 ↑
feature/* (funcionalidades)
release/* (versiones)
```

---

## Estructura de Ramas

### 1. **Branch: `main`** (Producción)
- Código estable y probado
- Solo recibe merges desde `release/`
- **Protegida** en GitHub: sin pushes directos
- Tags con versiones (v1.0, v1.1, etc.)

```bash
main
├── v1.0 (tag: release/analisis-v1)
└── v1.1 (tag: release/analisis-v1.1)
```

### 2. **Branch: `develop`** (Desarrollo)
- Rama principal de desarrollo
- Integra features completadas
- Base para crear nuevas features
- **Casi protegida**: solo PRs con review

```bash
develop
├── Feature A completada
├── Feature B completada
└── Feature C en progress
```

### 3. **Branches: `feature/*`** (Funcionalidades)
- Una rama por funcionalidad
- Nomenclatura: `feature/descripcion-corta`
- Se crean desde `develop`
- Se mergean de vuelta a `develop` via PR

**Ejemplos:**
```
feature/limpieza-datos
feature/analisis-usuarios
feature/validacion-emails
feature/metricas-avanzadas
```

### 4. **Branch: `release/*`** (Releases)
- Preparación de versión para producción
- Solo bugfixes menores
- Nomenclatura: `release/version-numero`
- Se mergea a `main` y `develop`

**Ejemplo:**
```
release/analisis-v1  → main (v1.0)
release/analisis-v1.1 → main (v1.1)
```

### 5. **Branches: `hotfix/*`** (Emergencias) - Opcional
- Para bugs críticos en producción
- Se crean desde `main`
- Se mergean a `main` y `develop`

```
hotfix/corregir-crash-principal
```

---

## Flujo de Trabajo Típico

### Escenario 1: Crear Nueva Feature

```bash
# 1. Asegurar que develop está actualizada
git checkout develop
git pull origin develop

# 2. Crear rama feature desde develop
git checkout -b feature/mi-funcionalidad

# 3. Hacer cambios y commits
echo "# Nueva función" > mi_funcionalidad.py
git add .
git commit -m "Add: Implementar nueva función"

# 4. Push del feature
git push origin feature/mi-funcionalidad

# 5. Crear Pull Request en GitHub
# - De: feature/mi-funcionalidad
# - A: develop
#
# - Descripción:
#   "Implementa limpieza de datos usuarios
#    - Maneja valores nulos
#    - Normaliza correos"
#
# - Esperar review
# - Merge (Squash and merge)

# 6. Eliminar rama después del merge
git branch -d feature/mi-funcionalidad
git push origin --delete feature/mi-funcionalidad
```

### Escenario 2: Preparar Release

```bash
# 1. Crear rama release desde develop
git checkout develop
git pull origin develop
git checkout -b release/analisis-v1

# 2. Versión bump (si aplica)
# Actualizar versión en código/archivo de configuración
echo "__version__ = '1.0.0'" > __init__.py

# 3. Bugfixes menores
git commit -m "Bump: Version 1.0.0"
git push origin release/analisis-v1

# 4. Crear PR: release/analisis-v1 → main
# Descripción: "Release v1.0 - Análisis de usuarios"

# 5. Una vez aprobado, mergear a main
# → Merge (no squash)
# → Crea tag: git tag -a v1.0 -m "Version 1.0"

# 6. Mergear de vuelta a develop
git checkout develop
git pull origin develop
git merge release/analisis-v1

# 7. Eliminar rama release
git branch -d release/analisis-v1
git push origin --delete release/analisis-v1
```

### Escenario 3: Hotfix en Producción (Emergencia)

```bash
# 1. Crear hotfix desde main
git checkout main
git pull origin main
git checkout -b hotfix/corregir-bug-critico

# 2. Hacer fix
git commit -m "Fix: Corrección bug crítico en limpieza"

# 3. Mergear a main
git checkout main
git merge hotfix/corregir-bug-critico
git tag -a v1.0.1 -m "Hotfix 1.0.1"
git push origin main --tags

# 4. Mergear a develop
git checkout develop
git merge hotfix/corregir-bug-critico
git push origin develop

# 5. Limpiar
git branch -d hotfix/corregir-bug-critico
```

---

## Comandos Git Esenciales

### Configuración Inicial
```bash
# Configurar usuario
git config user.name "Tu Nombre"
git config user.email "tu@email.com"

# O globalmente
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Ramas
```bash
# Ver ramas locales
git branch

# Ver todas las ramas (local + remoto)
git branch -a

# Crear rama
git branch feature/nueva-funcion

# Cambiar a rama
git checkout feature/nueva-funcion

# Crear y cambiar en uno
git checkout -b feature/nueva-funcion

# Eliminar rama local
git branch -d feature/nueva-funcion

# Eliminar rama remota
git push origin --delete feature/nueva-funcion

# Renombrar rama
git branch -m nombre-viejo nombre-nuevo
```

### Commits
```bash
# Ver cambios
git status
git diff

# Agregar cambios
git add archivo.py
git add .           # Todos los cambios

# Hacer commit
git commit -m "Descripción del cambio"
git commit -m "Descripción

Detalles adicionales del cambio"

# Ver historial
git log --oneline
git log --graph --decorate --all

# Enmendar último commit
git commit --amend
```

### Push/Pull
```bash
# Traer cambios remotos
git pull origin develop

# Enviar cambios
git push origin feature/mi-rama

# Push de rama nueva
git push -u origin feature/mi-rama

# Push de tags
git push origin --tags
git push origin v1.0
```

### Merge
```bash
# Mergear rama en actual
git merge feature/mi-rama

# Mergear sin fast-forward
git merge --no-ff feature/mi-rama

# Rebase (reorganizar commits)
git rebase develop

# Abort merge si hay conflictos
git merge --abort
```

### Conflictos
```bash
# Ver conflictos
git status
git diff

# Resolver conflictos manualmente en el archivo

# Marcar como resuelto
git add archivo-conflictivo.py

# Completar merge
git commit -m "Merge: Resolver conflictos"
```

---

## Convenciones de Commits

### Formato Recomendado

```
<tipo>: <descripción corta>

<descripción detallada opcional>

<referencias (ej: #123)>
```

### Tipos de Commits

```
feat:  Nueva funcionalidad
fix:   Corrección de bug
docs:  Cambios en documentación
style: Cambios de formato sin tocar lógica
refactor: Reorganización de código sin cambios funcionales
perf:  Mejoras de rendimiento
test:  Cambios en tests
build: Cambios en dependencias o build
ci:    Cambios en CI/CD
chore: Cambios miscéláneos
```

### Ejemplos

```bash
# Feature
git commit -m "feat: Agregar función de validación de emails"

# Bugfix
git commit -m "fix: Corregir crash al cargar CSV vacío"

# Documentación
git commit -m "docs: Actualizar README con instrucciones"

# Con detalles
git commit -m "feat: Normalizar campos de correo

- Convertir a minúsculas
- Eliminar espacios
- Validar formato"
```

---

## Pull Requests (PRs)

### Crear un buen PR

**Título:**
```
feat: Agregar limpieza de campos monetarios
```

**Descripción:**
```markdown
## Descripción
Implementa función para limpiar campos monetarios en DataFrames,
eliminando símbolos ($, €) y convirtiendo a números.

## Cambios
- Nueva función `limpiar_campos_monetarios()` en data_processing.py
- Maneja símbolos de moneda
- Convierte a float automáticamente
- Incluye manejo de errores

## Testing
- ✓ Testeado con datos CSV reales
- ✓ Maneja valores nulos correctamente
- ✓ No rompe datos existentes

## Screenshots/Output
```
input: ['$100.50', '$200.00', 'invalid']
output: [100.5, 200.0, NaN]
```

## Checklist
- [x] Código testea sin errores
- [x] Documentado con docstrings
- [x] Sin conflictos con develop
- [x] Sigue convenciones del proyecto
```

### Revisar un PR

1. **Ver cambios**: Click en "Files changed"
2. **Revisar lógica**: ¿Tiene sentido? ¿Está bien?
3. **Comprobar tests**: ¿Pasan todos?
4. **Hacer comentarios**: Sugerir mejoras
5. **Aprobar o solicitar cambios**

---

## Protección de Ramas en GitHub

### Configurar `main` como rama protegida

1. Ir a: Configuración > Branches > Branch protection rules
2. Patrón: `main`
3. Requiere:
   - ✓ Pull request reviews antes de merge
   - ✓ Al menos 1 aprobación
   - ✓ Dismiss stale reviews
   - ✓ Require branches to be up to date
   - ✓ Require status checks (si tienes CI)

### Resultado
```
❌ No se puede hacer push directo a main
✓ Solo PRs aprobadas se pueden mergear
```

---

## Casos Comunes

### Caso 1: He hecho cambios en develop pero debo estar en feature

```bash
# 1. Crear rama feature
git checkout -b feature/mi-tarea

# 2. Los cambios ya están (git los tomará automáticamente)

# 3. Ir a develop y resetear
git checkout develop
git reset --hard origin/develop  # ⚠️ Pierde cambios locales

# 4. Los cambios están en feature
git checkout feature/mi-tarea
```

### Caso 2: Mergear una rama que tiene conflictos

```bash
# 1. Intentar merge
git merge feature/x
# → Conflictos!

# 2. Resolver conflictos manualmente
# Abrir archivo conflictivo:
# <<<<<<< HEAD
# código actual
# =======
# código que viene del merge
# >>>>>>> feature/x

# 3. Elegir qué mantener, guardar

# 4. Completar merge
git add archivo-conflictivo.py
git commit -m "Merge: Resolver conflictos"

# Si cambias de idea
git merge --abort
```

### Caso 3: He cometido un error, quiero deshacer

```bash
# Deshacer último commit (mantiene cambios)
git reset --soft HEAD~1

# Deshacer último commit (pierde cambios)
git reset --hard HEAD~1

# Deshacer cambios en archivo
git checkout -- archivo.py

# Ver qué va a desaparecer
git log --oneline -5
```

---

## Visualizar el árbol de ramas

```bash
# Comando útil
git log --graph --decorate --all --oneline

# O crear alias
git config --global alias.tree "log --graph --decorate --all --oneline"

# Luego solo:
git tree
```

Salida:
```
* a1b2c3d (HEAD -> develop) Merge pull request #2
|\
| * 5x6y7z (release/analisis-v1) Release v1.0
|/
* 8a9b0c1 (main) Initial commit v1.0
```

---

## ✅ Checklist: Antes de Mergear

- [ ] ¿Los tests pasan?
- [ ] ¿No hay conflictos con develop?
- [ ] ¿El código está documentado?
- [ ] ¿Sigue las convenciones del proyecto?
- [ ] ¿La descripción del PR es clara?
- [ ] ¿Se revisó el código?
- [ ] ¿Funciona en la máquina?

---

**Recuerda: Commits pequeños, frecuentes y bien documentados → Historial limpio y mantenible** 📝
