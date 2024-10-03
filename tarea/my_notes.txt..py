# Escritura de Archivo de Texto

# Crea un nuevo archivo llamado my_notes.txt en modo escritura ('w')
my_notes = open('my_notes.txt', 'w')

# Metodo write(): escribir línea por línea
my_notes.write("Línea 1: Esta es una de mis notas personales.\n")
my_notes.write("Línea 2: Aprender Python cada día me acerca a ser mejor programador.\n")

# Metodo writelines(): escribir múltiples líneas desde una lista
lineas = ["Línea 3: Nunca es tarde para seguir aprendiendo.\n",
          "Línea 4: La constancia es clave para el éxito.\n"]
my_notes.writelines(lineas)

# Cerrar el archivo tras la escritura
my_notes.close()

# Lectura de Archivo de Texto

# Abre el archivo my_notes.txt en modo lectura ('r')
my_notes = open('my_notes.txt', 'r')

# Metodo 1: read() lee el archivo como una sola cadena
print('Método 1: read()')
print('--------------------')
print(my_notes.read())  # Mostramos el contenido del archivo completo
my_notes.close()  # Cerramos el archivo después de la lectura

# Metodo 2: readlines() lee todas las líneas en una lista
my_notes = open('my_notes.txt', 'r')  # Reabrimos el archivo
print('Método 2: readlines()')
print('--------------------')

# Leer y mostrar cada línea del archivo una por una utilizando un bucle for
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))  # Mostrar la línea sin salto de línea adicional

# Cerrar el archivo después de la lectura
my_notes.close()
