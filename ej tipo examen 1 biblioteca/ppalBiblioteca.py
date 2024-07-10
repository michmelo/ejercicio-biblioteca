import funcionesBiblioteca as fn


while True:
        print("\n\nMenú de opciones:")
        print("1. Crear libro")
        print("2. Actualizar libro")
        print("3. Eliminar libro")
        print("4. Crear usuario")
        print("5. Actualizar usuario")
        print("6. Eliminar usuario")
        print("7. Registrar préstamo")
        print("8. Eliminar préstamo")
        print("9. Estadísticas de préstamos")
        print("10. Salir")
        opcion = input("Ingrese la opción: ")
        if opcion == '1':
            fn.crearLibro()#
        elif opcion == '2':
            fn.actualizarLibro()#
        elif opcion == '3':
            fn.borrarLibro()#
        elif opcion == '4':
            fn.crearUsuario()#
        elif opcion == '5':
            fn.actualizarUsuario()#
        elif opcion == '6':
            fn.borrarUsuario()#
        elif opcion == '7':
            fn.registrarPrestamo()#
        elif opcion == '8':
            fn.borrarPrestamo()#
        elif opcion == '9':
            fn.estadisticasPrestamos()
        elif opcion == '10':
            break
        else:
            print("Opción no válida")
