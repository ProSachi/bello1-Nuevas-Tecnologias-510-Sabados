// Función para mostrar el formulario de registro
function showRegister() {
    document.getElementById('loginForm').classList.add('hidden');
    document.getElementById('registerForm').classList.remove('hidden');
    clearNotification();
}

// Función para mostrar el formulario de login
function showLogin() {
    document.getElementById('registerForm').classList.add('hidden');
    document.getElementById('loginForm').classList.remove('hidden');
    clearNotification();
}

// Función para mostrar notificaciones
function showNotification(message, type = 'success') {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.classList.remove('hidden', 'bg-green-500', 'bg-red-500', 'bg-blue-500');
    
    if (type === 'success') {
        notification.classList.add('bg-green-500');
    } else if (type === 'error') {
        notification.classList.add('bg-red-500');
    } else {
        notification.classList.add('bg-blue-500');
    }
    
    // Ocultar notificación después de 3 segundos
    setTimeout(() => {
        notification.classList.add('hidden');
    }, 3000);
}

// Función para limpiar notificaciones
function clearNotification() {
    const notification = document.getElementById('notification');
    notification.classList.add('hidden');
}

// Manejo del formulario de login
function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    
    // Validación básica
    if (!email || !password) {
        showNotification('Por favor, completa todos los campos', 'error');
        return;
    }
    
    // Verificar si el usuario existe en localStorage
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const user = users.find(u => u.email === email && u.password === password);
    
    if (user) {
        showNotification(`¡Bienvenido de nuevo, ${user.name}!`, 'success');
        
        // Guardar sesión
        localStorage.setItem('currentUser', JSON.stringify(user));
        
        // Limpiar formulario
        event.target.reset();
        
        // Aquí podrías redirigir a otra página
        setTimeout(() => {
            console.log('Usuario logueado:', user);
        }, 1500);
    } else {
        showNotification('Correo o contraseña incorrectos', 'error');
    }
}

// Manejo del formulario de registro
function handleRegister(event) {
    event.preventDefault();
    
    const name = document.getElementById('registerName').value;
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
    const confirmPassword = document.getElementById('registerConfirmPassword').value;
    
    // Validación básica
    if (!name || !email || !password || !confirmPassword) {
        showNotification('Por favor, completa todos los campos', 'error');
        return;
    }
    
    // Validar que las contraseñas coincidan
    if (password !== confirmPassword) {
        showNotification('Las contraseñas no coinciden', 'error');
        return;
    }
    
    // Validar longitud de contraseña
    if (password.length < 6) {
        showNotification('La contraseña debe tener al menos 6 caracteres', 'error');
        return;
    }
    
    // Obtener usuarios existentes
    const users = JSON.parse(localStorage.getItem('users')) || [];
    
    // Verificar si el email ya está registrado
    if (users.some(u => u.email === email)) {
        showNotification('Este correo ya está registrado', 'error');
        return;
    }
    
    // Crear nuevo usuario
    const newUser = {
        id: Date.now(),
        name: name,
        email: email,
        password: password,
        createdAt: new Date().toISOString()
    };
    
    // Agregar usuario al array
    users.push(newUser);
    
    // Guardar en localStorage
    localStorage.setItem('users', JSON.stringify(users));
    
    showNotification('¡Cuenta creada exitosamente!', 'success');
    
    // Limpiar formulario
    event.target.reset();
    
    // Cambiar a login después de 2 segundos
    setTimeout(() => {
        showLogin();
    }, 2000);
}

// Verificar si hay un usuario logueado al cargar la página
window.addEventListener('DOMContentLoaded', () => {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (currentUser) {
        showNotification(`Sesión activa: ${currentUser.name}`, 'info');
    }
});

// Función para cerrar sesión (opcional)
function logout() {
    localStorage.removeItem('currentUser');
    showNotification('Sesión cerrada', 'info');
}
