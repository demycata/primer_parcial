

def imprimir_dato(nombres:list, generos:list, legajo:list, nota:list, promedio_estudiante:list, mostras:bool, indice:int) -> None:
    '''
    Imprime los datos de un estudiante en la posicion indicada por el indice.
    Si mostras es True, imprime el promedio al final de la linea.
    Si mostras es False, no imprime el promedio.
    Argumentos:
        nombres: lista de nombres de los estudiantes
        generos: lista de generos de los estudiantes
        legajo: lista de legajos de los estudiantes
        materias: lista de materias
        nota: lista de notas de los estudiantes
        promedios: lista de promedios de los estudiantes
        mostras: booleano que indica si se debe mostrar el promedio o no
        indice: indice del estudiante a imprimir
    '''
    if mostras == False:
        print('┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐')
        print(f"│{nombres[indice]}\t  {generos[indice]}\t{legajo[indice]}\tMateria 1: {nota[indice][0]}\tMateria 2: {nota[indice][1]}\tMateria 3: {nota[indice][2]}\tMateria 4: {nota[indice][3]}\tMateria 5: {nota[indice][4]}\t│")
        print('└───────────────────────────────────────────────────────────────────────────────────────────────────────┘')
    else:
        print('┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐')
        print(f"│{nombres[indice]}\t  {generos[indice]}\t{legajo[indice]}\tMateria 1: {nota[indice][0]}\tMateria 2: {nota[indice][1]}\tMateria 3: {nota[indice][2]}\tMateria 4: {nota[indice][3]}\tMateria 5: {nota[indice][4]}\t{promedio_estudiante[indice]}│")
        print('└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘')
        
def imprimir_datos(nombres:list, generos:list, legajo:list, nota:list, promedios:list, mostras:bool, tamano:int) -> None: 
    '''
    Imprime los datos de todos los estudiantes.
    Si mostras es True, imprime el promedio al final de la linea.
    Si mostras es False, no imprime el promedio.
    Argumentos:
        nombres: lista de nombres de los estudiantes
        generos: lista de generos de los estudiantes
        legajo: lista de legajos de los estudiantes
        materias: lista de materias
        nota: lista de notas de los estudiantes
        promedios: lista de promedios de los estudiantes
        mostras: booleano que indica si se debe mostrar el promedio o no
        tamano: tamaño de la lista
    '''
    for i in range(tamano):
            imprimir_dato(nombres, generos, legajo, nota, promedios, mostras, i)

def header_materias() -> None:
    '''
    Imprime el encabezado de la tabla de materias.
    '''
    print('\tMAYOR PROMEDIOS DE LAS MATERIAS')
    print('')

def show_promedio_materia(promedios_materias:list, mayor:int) -> None:
    '''
    Muestra el promedio de las materias.
    Argumentos:
        materias: lista de materias
        promedios_materias: lista de promedios de las materias
        mayor: promedio mayor
    '''
    for i in range(len(promedios_materias)):
        if promedios_materias[i] == mayor:
            print(f"Materia {i+1}: {promedios_materias[i]}")
    
def show_promedios_materias(promedio_materias:list, tamano: int) -> None:
    '''
    Muestra los promedios de las materias.
    Argumentos:
        materias: lista de materias
        promedio_materias: lista de promedios de las materias
        tamano: tamaño de la lista
    '''
    for i in range(tamano):
        show_promedio_materia(promedio_materias, i)

def header_datos()-> None:
    '''
    Imprime el encabezado de la tabla de datos.
    '''
    header = 'NOMBRES\tGENERO\tLEGAJO\tNOTAS:'
    print(header)

def cant_notas_materias(cant_notas:list, indice:int)-> None:
    '''
    Imprime la cantidad de notas ingresadas por materia.
    Args:
        cant_notas: lista con las veces que salio cada nota en una materia
        indice: Materia
    '''
    print(f'Materia {indice} | REGISTRO DE NOTAS')
    print('┌─────┬─────────────────────────────────────────────────────────────────────────────────┐')
    print("│NOTA │\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t│")
    print('├─────┼─────────────────────────────────────────────────────────────────────────────────┤')
    print(f"│VECES│\t{cant_notas[0]}\t{cant_notas[1]}\t{cant_notas[2]}\t{cant_notas[3]}\t{cant_notas[4]}\t{cant_notas[5]}\t{cant_notas[6]}\t{cant_notas[7]}\t{cant_notas[8]}\t{cant_notas[9]}\t│")
    print('└─────┴─────────────────────────────────────────────────────────────────────────────────┘')
        
