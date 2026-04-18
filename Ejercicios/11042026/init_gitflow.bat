@echo off
REM Script para inicializar Git Flow en el proyecto
REM Ejecutar esto desde la carpeta raíz del proyecto

echo.
echo =====================================================
echo Inicializando repositorio Git con Git Flow
echo =====================================================
echo.

REM Inicializar repositorio git
echo Paso 1: Inicializando repositorio git...
git init
git config user.email "usuario@example.com"
git config user.name "Mi Nombre"

REM Agregar archivos iniciales
echo Paso 2: Agregando archivos iniciales...
git add .
git commit -m "Initial commit: Estructura base del proyecto"

REM Crear rama develop
echo Paso 3: Creando rama develop...
git branch develop

REM Crear ramas de feature
echo Paso 4: Creando ramas de desarrollo...
git checkout -b feature/limpieza-datos
git commit --allow-empty -m "Feature: Módulo de limpieza de datos"
git checkout develop
git merge feature/limpieza-datos --no-edit

git checkout -b feature/analisis-usuarios
git commit --allow-empty -m "Feature: Script de análisis de usuarios"
git checkout develop
git merge feature/analisis-usuarios --no-edit

REM Crear rama release
echo Paso 5: Creando rama de release...
git checkout -b release/analisis-v1
git commit --allow-empty -m "Release: Versión 1.0 del análisis"
git checkout develop

REM Volver a main
git checkout main

echo.
echo =====================================================
echo ✓ Git Flow inicializado correctamente
echo =====================================================
echo.
echo Ramas disponibles:
git branch -a

echo.
echo Próximos pasos:
echo 1. Crear repositorio en GitHub
echo 2. Agregar remoto: git remote add origin https://github.com/usuario/repo.git
echo 3. Push de ramas: git push -u origin main develop release/analisis-v1
echo 4. Proteger rama main en GitHub
echo.
pause
