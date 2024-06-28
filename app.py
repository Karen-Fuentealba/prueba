"""Evaluación Parcial 3: Desarrollo de una Aplicación de Gestión de
Alumnos
Descripción del problema:
Desarrolle una aplicación en Python utilizando Visual Studio que permita
gestionar la información de los alumnos en una escuela. La aplicación
debe incluir las siguientes funcionalidades:
Menú de usuario:
1. Registrar alumno
2. Listar todos los alumnos
3. Buscar alumnos por nivel
4. Calcular la nota promedio de los alumnos
5. Salir del programa y guardar
-----Objetivos y restricciones del script:
---- Debe incluir el uso de funciones (con y sin retorno, con o sin
-----parámetros)
---- Debe validar los datos ingresados y controlar las excepciones
---- Debe incluir control de versiones git/github
------ El desarrollo de la evaluación es INDIVIDUAL y debe ser subido a
GITHUB a la cuenta del estudiante
 Cualquier código idéntico será penalizado con nota 1.0
 El script debe ser comentado (explicando cada bloque de
código)
 De no existir el script o el repositorio en GITHUB será descontado
el 50% de la nota calificada
 En la plataforma AVA debe ser subido el enlace apuntando al
repositorio de GITHUB
 El programa debe guardar los alumnos ingresados en un archivo
de texto al salir del menú
Detalles de la funcionalidad:



1. Registrar alumno:
 El sistema debe permitir registrar un alumno ingresando los
siguientes datos: Nombre, Apellido, Edad, Nivel (Ejemplo: 1°, 2°,
3°, etc.), y Notas (lista de 5 notas aleatorias entre 1 y 10
generadas utilizando random).
 Validar que todos los datos sean ingresados correctamente
(validaciones numéricas y excepciones).

2. Listar todos los alumnos:
 Debe mostrar en la pantalla la lista de todos los alumnos
registrados en el sistema, con el formato similar al siguiente:

*****Nombre, Apellido, Edad, Nivel (Ejemplo: 1°, 2°,
3°, etc.), y Notas (lista de 5 notas aleatorias entre 1 y 10
generadas utilizando random).******

3. Buscar alumnos POR NIVEL:
 Permitir al usuario buscar y mostrar todos los alumnos de un nivel
específico.
4. Calcular la nota promedio de los alumnos:
 Calcular y mostrar la nota promedio de todos los alumnos
registrados utilizando la librería math para los cálculos necesarios.
5. Salir del programa:
 El programa debe funcionar hasta que el usuario decida salir,
guardando los alumnos ingresados en el programa en un archivo
de texto."""
from utilidades import registrar_alumnos, listar_alumnos, buscar_alumnos, calcular_promedio, guardar_alumnos
import os

def programa_principal():
    alumnos = {}
    lista_notas = []
    os.system('cls')
    print ("Menú de Usuario")
    print ("[1] - Registrar todos los alumnos")
    print ("[2] - Listar todos los alumnos")
    print ("[3] - Buscar alumnos por nivel")
    print ("[4] - Calcular la nota promedio de los alumnos")
    print ("[5] - Salir del programa y guardar")

    opcion = input("Seleccione una opción")
    if opcion == '1':
        os.cyctem('cls')
        registrar_alumnos(alumnos)
    elif opcion == '2':
        os.cyctem('cls')
        listar_alumnos(alumnos)
    elif opcion =='3':
        Buscar_alumnos(alumnos)
    elif opcion =='4':
        calcular_promedio(alumnos)
    elif opcion == '5':
        print("Saliendo del programa...")
        guardar_alumnos(alumnos)
        break
    else:
        print("Opción no valida. Intente de nuevo")
    
    if __name__ == "__main__":
        programa_principal()


        


