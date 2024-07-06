# 1)
# 1. Procesar lista de estudiantes.
# 2. Registrar estudiante.
# 3. Modificar nota.
# 4. Eliminar estudiante.
# 5. Generar promedio de notas.
# 6. Generar acta de cierre de curso.
# 7. Salir.
# 2)
# Registrar estudiante.
# Deberá solicitar al usuario los siguientes campos:
# a. Rut
# b. Nombre
# c. Nota 1
# d. Nota 2

estudiante = []

def procesar_lista_estudantes():
    with open("ListaCurso5b.csv", "r") as lista_5b:
        print(lista_5b)


def registrar_estudiante():
    while True:
        try:
            rut = input("Ingresa el rut del estudiante\n")
            break
        except:
            print("Opcion no valida")

    nombre = input("Ingresa el nombre del estudiante\n")
    apellido1 = input("Ingrese el primero apellido\n")
    apellido2 = input("Ingrese el segundo apellido\n")

    while  True:
        try:
            nota1 = float(input("Ingrese la primera nota:\n"))
            if nota1 > 1.0 and nota1 < 7.0:
                break
            else:
                print("Ingrese una nota dentro del rango")
        except:
            print("Opcion no valida")
    while  True:
        try:
            nota2 = float(input("Ingrese la segunda nota:\n"))
            if nota2 > 1.0 and nota2 < 7.0:
                break
            else:
                print("Ingrese una nota dentro del rango")
        except:
            print("Opcion no valida")


    dicc_estudiantes = {
        "rut": rut,
        "nombre": nombre,
        "apellido1": apellido1,
        "apellido2": apellido2,
        "nota1": nota1,
        "nota2": nota2
    }
    estudiante.append(dicc_estudiantes)

def modificar_nota():
    modificar_nota = input("Ingrese el rut del estudiante:\n")
    if not estudiante:
        print("No tienes trabajadores ingresados")
    else:
        for modificar_nota in estudiante:
            if modificar_nota in estudiante:
                print(f"Desea modificar el estudiante {modificar_nota}?\n1. Si\n2. No\n")
                op_eliminar = int(input())
                if op_eliminar == 1:
                    estudiante.insert(modificar_nota)
                else:
                    pass


def eliminar_estudiante():
    eliminar_estudiante = input("Ingrese el rut del estudiante:\n")
    if not estudiante:
        print("No tienes trabajadores ingresados")
    else:
        for eliminar_estudiante in estudiante:
            if eliminar_estudiante in estudiante:
                print(f"Desea elminar el estudiante {eliminar_estudiante}?\n1. Si\n2. No\n")
                op_eliminar = int(input())
                if op_eliminar == 1:
                    estudiante.remove(eliminar_estudiante)
                else:
                    pass
                


def generar_promedio_notas():
    pass
    
def generar_acta_cierre():
    pass

def salir():
    exit()

def menu():
    # Función que muestra el menú y gestiona las opciones
    opcion = 0
    while opcion != 7:
        try:
            print(
                "¿Que opcion desea realizar?\n"
                "1. Procesar lista de estudiantes\n"
                "2. Registrar estudiante\n"
                "3. Modificar nota\n"
                "4. Eliminar estudiante\n"
                "5. Generar promedio de notas\n"
                "6. Generar acta de cierre de curso\n"
                "7. Salir"
                )
            opcion = int(input("\n"))
            if opcion == 1:
                procesar_lista_estudantes()          
            elif opcion == 2:
                registrar_estudiante()
            elif opcion == 3:
                modificar_nota()
            elif opcion == 4:
                eliminar_estudiante()
            elif opcion == 5:
                generar_promedio_notas()
            elif opcion == 6:
                generar_acta_cierre()
            elif opcion == 7:
                salir()
            else:
                print("Opción no válida.")
        except ValueError:
            print("Opción no válida")

menu()  # Iniciar el programa llamando a la función del menú