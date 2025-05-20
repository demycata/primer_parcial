from BibliotecaDemy import *



mensaje_error = 'ERROR AL INGRESAR TU DATO'



def cargar_datos_secuencial(nombres: list, generos: list, legajos: list, materias:list, notas:list, tamano: int) -> None:
    '''
    Carga los datos de los estudiantes en las listas correspondientes.
    Argumentos:
        nombres: lista de nombres de los estudiantes
        generos: lista de generos de los estudiantes
        legajos: lista de legajos de los estudiantes
        notas: lista de notas de los estudiantes
        tamano: cantidad de estudiantes a cargar
    '''
    for i in range(tamano):

        nombres[i] = get_name()

        legajos[i] = get_legajo(legajos)

        generos[i] = get_genero()

        for j in range(len(notas[i])):
            print(materias[j])
            nota = get_int('Nota: ', mensaje_error, 1, 10, 100)
            notas[i][j] = nota

        print('Datos Ingresados CORRECTAMENTE')
        print('❅────────────────✧❅✦❅✧──────────────────❅•')
        seguir = input("Desea cargar otro estudiante?('s'/'n'): ")
        seguir = lower(seguir)
        if seguir == 'n':
            break

def promedio_estudiante(promedio:list, nota:list, tamano:int) -> list:
    '''
    Calcula el promedio de cada estudiante.
    Args:
        promedio: lista de promedios de los estudiantes
        nota: lista de notas de los estudiantes
        tamano: cantidad de estudiantes
    returns:
        Devuelve una lista con los promedios de cada estudiante.
    '''
    cantidad_materias = len(nota[0])
    for i in range(tamano):
        suma = 0
        for j in range(cantidad_materias):
            suma += nota[i][j]
        promedio[i] = suma / cantidad_materias
    print('Listo! Promedios calculados ✔')
    return promedio

def ordenar_estudiantes(nombres:list, legajo:list, promedio:list, genero:list, nota:list, como_ordenar:str, mostras:bool) -> None:
    '''
    Ordena los estudiantes por promedio y por nombre.
    Argumentos:
        nombres: lista de nombres de los estudiantes
        legajo: lista de legajos de los estudiantes
        promedio: lista de promedios de los estudiantes
        genero: lista de generos de los estudiantes
        nota: lista de notas de los estudiantes
        como_ordenar: 'a' para ordenar de menor a mayor, 'd' para ordenar de mayor a menor
        mostras: True si se deben mostrar los promedios, False si no
    '''
    if como_ordenar == 'a':

        for i in range(0, len(nombres)-1, 1):
            
            for j in range(i + 1, len(nombres), 1):
                    if promedio[i] > promedio[j]:
                    
                        legajo_auxiliar = legajo[i]
                        legajo[i] = legajo[j]
                        legajo[j] = legajo_auxiliar

                        nombre_auxiliar = nombres[i]
                        nombres[i] = nombres[j]
                        nombres[j] = nombre_auxiliar

                        promedio_auxiliar = promedio[i]
                        promedio[i] = promedio[j]
                        promedio[j] = promedio_auxiliar

                        genero_auxiliar = genero[i]
                        genero[i] = genero[j]
                        genero[j] = genero_auxiliar
                    
                        nota_auxiliar = nota[i]
                        nota[i] = nota[j]
                        nota[j] = nota_auxiliar                               

    if como_ordenar == 'd':

        for i in range(0, len(nombres)-1, 1):
            
            for j in range(i + 1, len(nombres), 1):

                    if promedio[i] < promedio[j]:
                    
                        legajo_auxiliar = legajo[i]
                        legajo[i] = legajo[j]
                        legajo[j] = legajo_auxiliar

                        nombre_auxiliar = nombres[i]
                        nombres[i] = nombres[j]
                        nombres[j] = nombre_auxiliar

                        promedio_auxiliar = promedio[i]
                        promedio[i] = promedio[j]
                        promedio[j] = promedio_auxiliar

                        genero_auxiliar = genero[i]
                        genero[i] = genero[j]
                        genero[j] = genero_auxiliar
                    
                        nota_auxiliar = nota[i]
                        nota[i] = nota[j]
                        nota[j] = nota_auxiliar                               

def promedio_materia(notas:list) -> list:
    '''
    Calcula el promedio de cada materia.
    Args:
        notas: lista de notas de los estudiantes
    returns:    
        Devuelve una lista con los promedios de cada materia.
    '''
    promedios_materias = [0] * len(notas[0])
    alumnos = len(notas)
    for i in range(alumnos):
        for j in (range(len(notas[0]))):
            promedios_materias[j] += notas[i][j]

    for x in range(len(promedios_materias)):
        promedios_materias[x] //= alumnos
    return promedios_materias

def mayor_promedio(promeidos:list) -> int | None:
    '''
    Busca el mayor promedio de la lista de promedios.
    Args:
        promedios: lista de promedios de cada materia
    returns:
        Devuelve el mayor promedio.
    '''
    mayor_promedio = None
    for i in promeidos:
        if mayor_promedio == None:
            mayor_promedio  = i
        if i >= mayor_promedio:
            mayor_promedio  = i
    return mayor_promedio

def buscador(legajo:list)-> int | None:
    '''
    Busca un legajo en la lista de legajos.
    Args:
        legajo: lista de legajos de los estudiantes
    returns:
        Devuelve el indice del legajo encontrado.
    '''
    indice = None
    referencia = get_int('Legajo:', mensaje_error, 10000, 99999, 100 )
    for i in range(len(legajo)):
        if legajo[i] == referencia:
            indice = i
            print(' ')
    if indice == None:
        print('\nNO EXISTE ESE LEGAJO')
    return indice
