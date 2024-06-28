
import random
def validar_alumnos(alumno):
    while True:
        alumno = input(alumno)
        if all(c.isalpha() or cisspace() for c in alumno):
            return alumno
        print ("Error, debe ingresar un nombre valido (letras)")

def valida_edad(recibe):
    While True:
    valor = input(recibe)
    if valor.isdigit():
        return int(valor)
    print("Error, Debe ingresar edad numérica")

def generar_notas(usar_notas):
    notas = f"{random.randint(1,10)}"
    return notas

def registrar_alumnos(alumnos, usar_notas):
    
    for i in range(1,3):
        notas = generar_notas(uso_notas)
        lista_notas[i] = notas

    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad = valida_edad("Ingrese la edad del alumno: ")
    nivel = input("Ingrese el nivel del alumno")

    alumnos[nivel] = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'nivel': nivel,
        'notas': notas
    }
    usar_notas.add(notas)

def listar_alumnos(alumnos):
    if not alumnos:
        print("no hay alumnos registrados")
    else:
        print(f"")

def buscar_alumnos(alumnos):

def calcular_promedio(alumnos):

def guardar_alumnos(alumnos):




    Nombre, Apellido, Edad, Nivel (Ejemplo: 1°, 2°,
3°, etc.), y Notas (lista de 5 notas aleatorias entre 1 y 10
generadas utilizando random).