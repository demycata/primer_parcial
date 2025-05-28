
import menu

import opcion

import datos

promedios = False

ingreso = False

while True:

    menu_de_opciones = menu.llamar_menu()

    match menu_de_opciones:
        
        case '1':

            opcion.cargar_datos(datos.nombres_estudiantes, datos.generos_estudiantes, datos.legajos_estudiantes, datos.notas_de_cada_estudiante, datos.estudiantes)

            ingreso = True

        case '2' if ingreso == True:

            opcion.imprimir_datos(datos.nombres_estudiantes, datos.generos_estudiantes, datos.legajos_estudiantes, datos.notas_de_cada_estudiante, datos.promedio_estudiantes, False, datos.estudiantes)

        case '3' if ingreso == True:

            opcion.calcular_promedios(datos.promedio_estudiantes, datos.notas_de_cada_estudiante, datos.estudiantes)

            promedios = True

        case '4' if ingreso == True and promedios == True:

            opcion.ordenar_promedios(datos.nombres_estudiantes, datos.generos_estudiantes, datos.legajos_estudiantes, datos.promedio_estudiantes, datos.notas_de_cada_estudiante, 'd', promedios, datos.estudiantes)

        case '5' if ingreso == True:

            opcion.materia_mayor_promedio(datos.notas_de_cada_estudiante)

        case '6' if ingreso == True:

            opcion.buscador(datos.nombres_estudiantes, datos.generos_estudiantes, datos.legajos_estudiantes, datos.notas_de_cada_estudiante, datos.promedio_estudiantes, promedios)
        
        case '7' if ingreso == True:

            opcion.cant_notas_x_mat(datos.notas_de_cada_estudiante)

        case '8':
            input("Presione ENTER para salir...")
            break

        case _:
            if ingreso == False:
                print('\nERROR --> INGRESA PRIMERO LOS DATOS')
            
            if promedios == False and ingreso == True:
                print('\nSE DEBE CALCULAR LOS PROMEDIOS')