#Centralizacion de Texto
def centrar_texto(texto,ancho_tabla,opcion): 
    """
    ¿Que hace la Funcion?
    Esta funcion se encarga de recibir un texto con un ancho total para ajustarlo a un espacio fijo y se alinea segun la opcion.
    - Opcion 1: Se centrara para la Izquierda
    - Opcion 2: Se centrara para la Derecha
    - Opcion 3: El Texto se centrara al medio

    Creacion de Variables (Dentro de la Funcion):
    - Texto (str): recibera el texto pasado como parametro. Se usa un String para asi tambien valores enteros o flotantes puedan funcionar.
    - Espacios (int): Cantidad de espacios para asignarle a texto. Recibe los parametros ancho_tabla y texto. Va a restar el ancho de tabla -
    el largo del texto
    - Espacios_Izq (int): Cantidad de espacios hacia la izquierda asignados para el texto. Hace la cantidad de espacios y lo divide por 2,
    dando un valor entero (Esto es por -> //).
    - Espacios_Der (int): Cantidad de espacios hacia la derecha asignados para el texto. Resta los espacios menos los espacios a la izquierda
   
    Parametros:
    Texto (str): El que se desea fijar a una medida.
    Ancho_tabla (int): El ancho total de la tabla, que se buscara fijar a una medida.
    Opcion (int): es la opcion que se seleccionara para fijar a una medida.

    Retorna:
    Texto (str): el texto con los espacios asignados segun la opcion indicada.
    """
    
    #Convertimos el contenido de 'texto' a tipo string por si viene con otro tipo de dato
    texto = str(texto)

    #Calculamos cuantos espacios hay que agregar para que el texto se alinee dentro del ancho total de la tabla
    espacios = ancho_tabla - len(texto)   

    #Calculamos cuantos espacios van a la izquierda para centrar el texto 
    espacios_izq = espacios // 2

    #Lo que sobra va a la derecha (por si el numero es impar)
    espacios_der = espacios - espacios_izq

    #Opcion 1: Alinear el texto a la izquierda, rellenando espacios a la derecha
    if (opcion == 1):
        texto = texto + " " * espacios
    #Opcion 2: Alinear el texto a la derecha, agregando espacios a la izquierda
    elif (opcion == 2):
        texto = " " * espacios + texto
    #Opcion 3: Centrar el texto, agregando espacios tanto a la izquierda como a la derecha
    elif (opcion == 3): 
        texto = " " * espacios_izq + texto + " " * espacios_der
    
    return texto


#Esperar Tecla
def esperarTecla():
    """
    ¿Que hace la Funcion?
    Sirve como pausa interactiva en el juego

    Creacion de Variables (Dentro de la Funcion):
    - Tecla (str): Una variable que guarda lo que el usuario escribe cuando el programa le muestra este mensaje
    """

    #Solicita al usuario que presione solo Enter
    tecla = input("Toque solo Enter para continuar... ")

    #Mientras el usuario ingrese algo (> 0), se repite el mensaje de error
    while len(tecla) != 0:
        tecla = input("Toque solo Enter para continuar... ")


#Indice
def tiposIndice(indice):

    if indice == 1:
        print("----------------------------------------------\n")
    elif indice == 2:
        print("\n----------------------------------------------")
    