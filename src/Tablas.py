from almacenador import cargar_datos, guardar_datos

def generar_tabla_puntos():
    datos_del_json = cargar_datos()

    #ahora vamos a crear una lista vacia donde ahorita vamos a agregarle los nombre y puntos de los equipos
    tabla = []
    # seguidamente vamos a hacer un ciclo for que recorra y encuentre todos los equpos en "Equipos"
    for equipo in datos_del_json["Equipos"]:
        #luego vamos a crear una variable donde vamos a alojar los nombres de los equipos, osea todos lo que tengan la palabra clave nombre pero como equipo, traera el valor de esta
        nombre = equipo["nombre"]
        #Y aqui se creara otra variable que va entrar a estadisticas del equipo y ademas solamente a los puntos explicificamente
        puntos = equipo["estadisticas"]["puntos"]
        #Ahora aqui agregaremos a la lista vacia esas 2 variables
        tabla.append([nombre, puntos])

    #Ahora aqui vamos a ordenar esta lista con el metodo burbuja
    #Primero creamos otro ciclo for que vaya hasta la cantidad de datos que va a haber en la lista
    for _ in range(len(tabla)):
        #Seguidamente tenemos que entrar aun mas adentro de la lista, ahora haremos otro ciclo el cual ira de j hasta
        for j in range(len(tabla) - 1):
            if tabla[j][1] < tabla[j + 1][1]:
                tabla[j], tabla[j + 1] = tabla[j + 1], tabla[j]

    #Mostramos la tabla
    print("TABLA DE POSICIONES")
    print("-------------------------")

    #Imprimimos cada equipo
    for pos, equipo in enumerate(tabla, 1):
        nombre = equipo[0]
        puntos = equipo[1]
        print(pos, nombre, ":", puntos, " puntos")


def tabla_de_goleadores(top: int = 10):
    datos_del_json = cargar_datos()

    #Aqui Creamos una lista llamad tabla para almacenar jugadores y sus goles
    tabla = []

    #Hacemos un ciclo pa empezar a extraer los jugadores y sus goles de cada equipo
    for equipo in datos_del_json["Equipos"]:
        for jugador in equipo.get("Jugadores", []):
            nombre = jugador["nombre"]
            goles = jugador["estadisticas"]["goles"]
            tabla.append([nombre, goles])

    #Vea usamos ordenador para la tabla usando bubble sort o metodo burbuja
    n = len(tabla)
    for i in range(n):
        for j in range(0, n-i-1):
            if tabla[j][1] < tabla[j+1][1]:
                tabla[j], tabla[j+1] = tabla[j+1], tabla[j]

    #La lista va a ser desde donde empiece hasta el top que es int = 10
    tabla = tabla[:top]

    #Aqui imprimimos la tabla 
    print("Tabla de Goleadores")
    print("-------------------------")

    for pos, jugador in enumerate(tabla, start=1):
        nombre = jugador[0]
        goles = jugador[1]
        print(pos, nombre, goles)

def generar_estadisticas_equipo(id_equipo: str):
        datos_del_json = cargar_datos()
    
        for equipo in datos_del_json["Equipos"]:
            if equipo["ID"] == id_equipo:

                print(f"Informacion del equipo: {equipo['nombre']}")
                print(f"Ciudad: {equipo['ciudad']}")
                print(f"Director Tcnico: {equipo['dt']}")
                

                print("Estadisticas del equipo:")
                estadisticas_equipo = equipo.get("estadisticas", {})
                #usando el bulce for vamos a acceder a los keys y los values de las estadisticas del equipo
                #esto nos sirve mejor si establecemos que estadisticas_equipo una funcion de python
                #llamaa .items() y esto nos sirve para acceder a cada valor y clave de un diccionario de forma mas facil
                #en las estadisticas del equipo imprimira los datos de la izquierda que son las claves
                #un ejemplo de claves en nuestro codigo es: "puntos", "partidos_jugados", "pganados", etc
                #y esas claves tienen valores que serian numeros
                #en otras palabras va a imprimir las estadisticas de todos los jugadores del equipo
                for key, value in estadisticas_equipo.items():
                    print(f"{key}: {value}")
                
                
                partidos_jugados = estadisticas_equipo.get("partidos_jugados", 0)
                puntos = estadisticas_equipo.get("puntos", 0)
                puntos_disponibles = partidos_jugados * 3
                print(f"\nRendimiento del equipo: {puntos} puntos de {puntos_disponibles} puntos posibles, lo que quiere decir que: {puntos}/{puntos_disponibles}")


                print("\nEstadisticas de los jugadores:")
                for jugador in equipo.get("Jugadores", []):
                    print(f"\nJugador: {jugador['nombre']}")
                    for key, value in jugador.get("estadisticas", {}).items():
                        print(f"{key}: {value}")
                
                return  
        print("Equipo no encontrado")

