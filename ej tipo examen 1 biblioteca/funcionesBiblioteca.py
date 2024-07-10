import json
import csv

#Defino nombres de los archivos
LIBROS_ARCHIVO = 'libros.json'
USUARIOS_ARCHIVO = 'usuarios.json'
PRESTAMOS_ARCHIVO = 'prestamos.csv'
EVENTOS_ARCHIVO = 'eventos.txt'

FECHA = '2024-08-07'
HORA = '17:38'

#Funciones para leer/cargar archivos (read del metodo crud)
def leer_json(nombreArchivo):
    try:
        with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print('Error al leer el archivo')
        return[] #retorna lista por ser archivo json
    
def leer_csv(nombreArchivo):
    try:
        with open(nombreArchivo, 'r', encoding='utf-8', newline='') as archivo:
            return list(csv.DictReader(archivo))
    except FileNotFoundError:
        print('Error al cargar archivo.')
        return[] #retorna lista vacía porque lo convertí en lista
    
def leer_txt(nombreArchivo):
    try:
        with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print('Error al leer el archivo.')
        return ''

#funciones para libros

def crearLibro():
    libros = leer_json(LIBROS_ARCHIVO)
    idLibro = f'B{len(libros) + 101}'
    titulo = input('Ingrese titulo libro: ')
    autor = input('Ingrese autor libro: ')

    libros.append({'idLibro': idLibro,
                   'titulo': titulo,
                   'autor': autor
                   })
    print('Libro agregado.')
    
    with open(LIBROS_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(libros, archivo, indent=4)

def actualizarLibro():
    libros = leer_json(LIBROS_ARCHIVO)
    idLibro = input('Ingrese el ID del libro a actualizar: ')
    flag = False
    for libro in libros:
        if libro['idLibro'] == idLibro:
            print('Título encontrado: ', {libro['titulo']})
            titulo = input('Ingrese nuevo título: ')
            autor = input('Ingrese nuevo autor: ')
            libro['titulo'] = titulo
            libro['autor'] = autor
            print('Libro actualizado.')
            flag = True
            break
    if flag == False:
        print('Libro no encontrado.')
        return
    with open(LIBROS_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(libros, archivo, indent=4)

def borrarLibro():
    libros = leer_json(LIBROS_ARCHIVO)
    idLibro = input('Ingrese el ID del libro a eliminar: ')
    flag = False
    for libro in libros:
        if libro['idLibro'] == idLibro:
            print('Libro encontrado: ', {libro['titulo']})
            libros.remove(libro)
            print('Libro eliminado con éxito')
            flag = True
            break
    if flag == False:
        print('Libro no encontrado.')
        return
    with open(LIBROS_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(libros, archivo, indent=4)

#Funciones para los usuarios

def crearUsuario():
    usuarios = leer_json(USUARIOS_ARCHIVO)
    idUsuario = f'U{len(usuarios) + 101}'
    nombre = input('Ingrese nombre de usuario: ')
    contraseña = input('Ingrese contraseña: ')

    usuarios.append({'idUsuario': idUsuario,
                     'nombre': nombre,
                     'contraseña': contraseña
                     })
    print('Usuario creado con éxito.')

    with open(USUARIOS_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(usuarios, archivo, indent=4)

def actualizarUsuario():
    usuarios = leer_json(USUARIOS_ARCHIVO)
    idUsuario = input('Ingrese el ID del usuario que desea actualizar: ')
    flag = False
    for usuario in usuarios:
        if usuario['idUsuario'] == idUsuario:
            print('Usuario encontrado: ', {usuario['nombre']})
            nombre = input('Ingrese nuevo nombre: ')
            contraseña = input('Ingrese nueva contraseña: ')
            usuario['nombre'] = nombre
            usuario['contraseña'] = contraseña
            print('Usuario actualizado.')
            flag = True
            break
    if flag == False:
        print('Usuario no encontrado.')
        return
    with open(USUARIOS_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(usuarios, archivo, indent=4)

def borrarUsuario():
    usuarios = leer_json(USUARIOS_ARCHIVO)
    idUsuario = input('Ingrese el ID del usuario que desea eliminar: ')
    flag = False
    for usuario in usuarios:
        if usuario['idUsuario'] == idUsuario:
            print('Usuario encontrado: ', {usuario['nombre']})
            usuarios.remove(usuario)
            print('Usuario eliminado con éxito.')
            flag = True
    if flag == False:
        print('Usuario no encontrado.')
        return
    with open(USUARIOS_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(usuarios, archivo, indent=4)

#funciones para los préstamos

def registrarPrestamo():
    prestamos = leer_csv(PRESTAMOS_ARCHIVO)
    libros = leer_json(LIBROS_ARCHIVO)
    usuarios = leer_json(USUARIOS_ARCHIVO)

    if not usuarios:
        print('No hay usuarios registrados.')
        return
    if not libros:
        print('No hay libros registrados.')
        return
    
    idLibro = input('Ingrese ID del libro a prestar: ')
    idUsuario = input('Ingrese ID del usuario: ')

    if not prestamos:
        with open(PRESTAMOS_ARCHIVO, 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow('idPrestamo', 'fechaPrestamo', 'horaPrestamo', 'idLibro', 'titulo', 'idUsuario', 'nombre')

    for prestamo in prestamos[1:]: #se hace el slice [1:] para evitar que el ciclo itere sobre la primera línea que sería la cabecera
        if prestamo[3] == idLibro:
            print('El libro ya está prestado.')
            return
        
    idPRestamo = f'P{len(prestamos) + 101}'
    
    titulo = None
    for libro in libros:
        if libro['idLibro'] == idLibro:
            titulo = libro['titulo']
            break
    
    if titulo == None:
        print('No se encontró el libro.')
        return
    
    nombre = None
    for usuario in usuarios:
        if usuario['idUsuario'] == idUsuario:
            nombre = usuario['nombre']
            break

    if nombre == None:
        print('No se encontró el usuario.')
        return
    
    nuevoPrestamo = [idPRestamo, FECHA, HORA, idLibro, titulo, idUsuario, nombre]

    with open(PRESTAMOS_ARCHIVO, 'a', encoding='utf-8', newline='') as archivo: #uso el permiso append para agregar el prestamo al final de la lista
        escritor = csv.writer(archivo)
        escritor.writerow(nuevoPrestamo)

    print(f'Libro prestado: {titulo} a usuario: {nombre}')

def borrarPrestamo():
    prestamos = leer_csv(PRESTAMOS_ARCHIVO)
    idPrestamo = input('Ingrese el ID del prestamo a borrar: ')

    for prestamo in prestamos[1:]:
        flag = False
        if prestamo['idPRestamo'] == idPrestamo:
            print(f'Prestamo encontrado: {prestamo}')
            prestamos.remove(prestamo)
            print('Prestamo eliminado.')
            flag = True
            break
        if flag == False:
            print('Préstamo no encontrado')
            return
        with open(PRESTAMOS_ARCHIVO, 'w', encoding='utf-8') as archivo:
            escritor = csv.writer(file)
            escritor.csvwriterow(prestamos)

'''def estadisticasPrestamos():
    prestamos = leer_csv(PRESTAMOS_ARCHIVO)

    if not prestamos:
        print('No hay prestamos registrados.')
        return
    
    contadorLibros = {}

    for prestamo in prestamos[1:]:
        idLibro = prestamo[3]
        if idLibro not in contadorLibros:
            contadorLibros[idLibro] = 1
        else:
            contadorLibros[idLibro] += 1

    librosOrdenados = sorted(contadorLibros.items())'''