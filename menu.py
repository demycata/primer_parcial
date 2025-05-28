def llamar_menu()-> str:
    '''
    Muestra el menu de opciones y devuelve la opcion elegida por el usuario.
    returns:
        str: Opcion elegida por el usuario.
    '''
    while True:
        print('❅────────────────✧❅✦❅✧──────────────────❅•')
        op = input( '[1] - Ingresar Datos de los Estudiantes\n'
                    '[2] - Mostrar Datos\n'
                    '[3] - Calcular Promedios\n'
                    '[4] - Estudiantes con mejor Promedio\n'
                    '[5] - Materias con mejor Promedio general\n'
                    '[6] - Buscar por Legajo\n'
                    '[7] - Notas totales de una Materia\n' \
                    '[8] - SALIR\n' \
                    '➢  ')
        print('❅────────────────✧❅✦❅✧──────────────────❅•')
        if op == '1' or op == '2' or op == '3' or op == '4' or op == '5' or op == '6' or op == '7' or op == '8':
            print('')
            break
        else:
            print('ERROR --> INGRESE UN VALOR VALIDO')

    return op
