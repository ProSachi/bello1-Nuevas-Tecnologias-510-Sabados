# Proyecto de Login y Registro

Sistema de autenticación con formularios de inicio de sesión y registro usando HTML, Tailwind CSS y JavaScript.

## Características

- ✨ Diseño moderno y responsivo con Tailwind CSS
- 🔄 Alternancia fluida entre formularios de login y registro
- 💾 Almacenamiento de usuarios en localStorage
- ✅ Validación de formularios en tiempo real
- 🔔 Sistema de notificaciones
- 🎨 Gradientes y animaciones suaves

## Estructura del Proyecto

```
├── index.html    # Página principal con los formularios
├── script.js     # Lógica JavaScript
└── README.md     # Este archivo
```

## Funcionalidades

### Formulario de Login
- Campo de correo electrónico
- Campo de contraseña
- Opción "Recordarme"
- Enlace para recuperar contraseña
- Validación de credenciales

### Formulario de Registro
- Campo de nombre completo
- Campo de correo electrónico
- Campo de contraseña (mínimo 6 caracteres)
- Confirmación de contraseña
- Aceptación de términos y condiciones
- Validación de datos

### Validaciones Implementadas
- Campos requeridos
- Formato de email válido
- Longitud mínima de contraseña
- Coincidencia de contraseñas
- Verificación de correo único
- Verificación de credenciales al iniciar sesión

## Cómo Usar

1. Abre `index.html` en tu navegador
2. Para registrarte: haz clic en "Regístrate aquí"
3. Completa el formulario de registro
4. Inicia sesión con tus credenciales

## Tecnologías Utilizadas

- **HTML5**: Estructura del proyecto
- **Tailwind CSS**: Framework de CSS vía CDN
- **JavaScript**: Lógica de validación y almacenamiento
- **localStorage**: Persistencia de datos del usuario

## Notas

- Los datos se almacenan localmente en el navegador (localStorage)
- Las contraseñas se guardan en texto plano (solo para demostración)
- En un proyecto real, la autenticación debería hacerse en el backend con encriptación adecuada
