""" x = 10
y = "20"
print(x) """

# 1. Python crea un objeto de tipo 'int' con el valor 10 en la memoria.
# 2. Python crea un nombre 'x'.
# 3. Python "apunta" el nombre 'x' a ese objeto 'int(10)'.
x = 10

# 1. Python busca el objeto al que apunta 'x' (el int(10)).
# 2. Python crea un nuevo nombre 'y'.
# 3. Python "apunta" el nombre 'y' AL MISMO objeto 'int(10)'.
y = x

# 1. Python crea un NUEVO objeto 'int(11)'.
# 2. Python "re-apunta" el nombre 'x' a este nuevo objeto.
# 3. 'y' NO SE VE AFECTADO. Sigue apuntando al 'int(10)' original.
x = 11

print(x) # Imprime 11
