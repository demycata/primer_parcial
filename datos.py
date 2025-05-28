import random

from BibliotecaDemy import *

estudiantes = 30

promedio_estudiantes = [0] * estudiantes

#notas_de_cada_estudiante = inicializar_matriz(estudiantes, 5, 4)

notas_de_cada_estudiante = [
    [random.randint(1, 10) for _ in range(5)] for _ in range(estudiantes)
]

#nombres_estudiantes = crear_lista(estudiantes, 'Name')

nombres_estudiantes = [
    "Juan", "Ana", "Pedro", "Lucia", "Carlos", "Sofia", "Diego", "Pablo", "Mateo", "Camila",
     "Kiara", "Martin", "Tomas", "Julian", "Messi", "Mia", "Nahuel", "Teo", "Lucas", "Paula",
     "Bruno", "Emilia", "Nicole", "Renata", "Demian", "Isabel", "Franco", "Victor", "Luis", "Lara"
]

generos_estudiantes = crear_lista(estudiantes, 'X')

legajos_estudiantes = generar_lista_legajos()

#materias = ['Matematica', 'Algebra', 'Historia', 'Ingles', 'Fisica']