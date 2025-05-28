import tablas 

import funciones

def cargar_datos(nombres:list, generos:list, legajos:list, notas:list, tamano:int) -> None:
    '''
    Opcion de Carga de datos de los estudiantes en las listas correspondientes.
    Args:
        nombres: lista de nombres de los estudiantes
        generos: lista de generos de los estudiantes
        legajos: lista de legajos de los estudiantes
        notas: lista de notas de los estudiantes
        tamano: cantidad de estudiantes a cargar
    '''
    funciones.cargar_datos_secuencial(nombres, generos, legajos, notas, tamano)
        
def imprimir_datos(nombres:list, generos:list, legajo:list, nota:list, promedios:list, mostras:bool, tamano:int)-> None:
    '''
    Opcion de Imprimir los datos de los estudiantes.
    Args:
        nombres: lista de nombres de los estudiantes
        generos: lista de generos de los estudiantes
        legajo: lista de legajos de los estudiantes
        materias: lista de materias
        nota: lista de notas de los estudiantes
        promedios: lista de promedios de los estudiantes
        mostras: booleano que indica si se debe mostrar el promedio o no
        tamano: tamaño de la lista
    '''
    tablas.header_datos()
    tablas.imprimir_datos(nombres, generos, legajo, nota, promedios, mostras, tamano)

def calcular_promedios(promedio_estudiantes:list, notas:list, tamano:int)-> None:
    '''
    Opcion de Calcular los promedios de los estudiantes.
    Args:
        promedio_estudiantes: lista de promedios de los estudiantes
        notas: lista de notas de los estudiantes
        tamano: cantidad de estudiantes a cargar
    '''
    funciones.promedio_estudiante(promedio_estudiantes, notas, tamano)

def ordenar_promedios(nombres:list, generos:list, legajo:list, promedio:list,nota:list, como_ordenar:str, mostras:bool, tamano:int)-> None:
    '''
    Opcion de Ordenar los estudiantes por promedio y por nombre.
    Args:
        nombres: lista de nombres de los estudiantes
        generos: lista de generos de los estudiantes
        legajo: lista de legajos de los estudiantes
        materias: lista de materias
        promedio: lista de promedios de los estudiantes
        nota: lista de notas de los estudiantes
        como_ordenar: 'a' para ordenar de menor a mayor, 'd' para ordenar de mayor a menor
        mostras: booleano que indica si se debe mostrar el promedio o no
        tamano: tamaño de la lista
    '''
    funciones.ordenar_estudiantes(nombres, legajo, promedio, generos, nota, como_ordenar)
    tablas.header_datos()
    tablas.imprimir_datos(nombres, generos, legajo, nota, promedio, mostras, tamano)

def materia_mayor_promedio(notas:list)-> None:
    '''
    Opcion de Mostrar las materias con mejor promedio.
    Args:
        notas: lista de notas de los estudiantes
        materias: lista de materias
    '''
    promedio_materias = funciones.promedio_materia(notas)
    mayor_prom = funciones.mayor_promedio(promedio_materias)
    tablas.header_materias()
    tablas.show_promedio_materia(promedio_materias, mayor_prom)
        
def buscador(nombres:list, generos:list, legajo:list, nota:list, promedios:list, mostras:bool)-> None:
    '''
    Opcion de Buscar un estudiante por legajo.
    Args:
        nombres: lista de nombres de los estudiantes
        generos: lista de generos de los estudiantes
        legajo: lista de legajos de los estudiantes
        materias: lista de materias
        nota: lista de notas de los estudiantes
        promedios: lista de promedios de los estudiantes
        mostras: booleano que indica si se debe mostrar el promedio o no
    '''
    indice = funciones.buscador(legajo)
    if indice != None:
        tablas.header_datos()
        tablas.imprimir_dato(nombres, generos, legajo, nota, promedios, mostras, indice)
 
def cant_notas_x_mat(notas:list):
        '''
        Opcion de Mostrar la cantidad de notas ingresadas por materia.
        Args:
            notas: lista de notas de los estudiantes
        '''
        materia = funciones.get_indice()
        cant_notas = funciones.notas_en_materias(notas, materia)
        tablas.cant_notas_materias(cant_notas, materia)