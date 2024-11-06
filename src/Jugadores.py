#aqui vamos a traernos las funciones cargar_datos y guardar_datos que creamos en el archivo almacenador.py
from almacenador import cargar_datos, guardar_datos

#ahora vamos a crear un set constante de posiciones validades digitables en consola
POSICIONES_VALIDAS = {"Delantero", "Mediocampista", "Defensa", "Portero"}

#ahora vamos a crear una funcion que va a verificar el registro de un jugador en el JSON 
def Verificador_de_registro_jugador(numero_camisa, id_equipo, posicion):
    datos_del_json = cargar_datos()

    #aqui miraremos que el id del equipo coincida con el que digito el usuario
    for equipo in datos_del_json["Equipos"]:
        if equipo["ID"] == id_equipo: #aqui hace la verificacion y si lo logra
            for jugador in equipo.get("Jugadores", []):
                #aqui mira si el numero de camisa en la lista de jugadores es igual al que digito el usuario
                #si es correcto retornaara false o error 
                #ya que no puede existir el mismo numero de camisa en el mismo equipo para dos jugadores
                if jugador["numero de camisa"] == numero_camisa:
                    print(f"Error: El numero de camisa: {numero_camisa} ya esta en uso en el equipo: {id_equipo}")
                    return False
                if posicion not in POSICIONES_VALIDAS:
                    print(f"Eso no se puede, solo valido: {POSICIONES_VALIDAS}")
                    return False
            break  
    return True

#ahora vamos a crear una funcion que va a registrar a un jugador en el JSON 
def registro_jugador(nombre: str, numero_camisa: int, posicion: str, id_equipo: str):
    datos_del_json = cargar_datos()
        
    # aqui vamos a gurdar el ID del nuevo jugador
    id_list_jugador = []
    #mas de lo mismo
    for equipo in datos_del_json["Equipos"]:
        #solo que se usa. get() para acceder a las llaves de un diccionario o a los datos de los Jugadores del equipo en este caso
        #y se guarda como jugadores
        Jugadores = equipo.get("Jugadores", [])
        #usamos el metodo de asignacion de ids usado para equipos
        for jugador in Jugadores:
            id_num_jugador = int(jugador["ID"][3:])
            id_list_jugador.append(id_num_jugador)
        
    ultimo_id_jug = max(id_list_jugador, default=0)
    nuevo_id_jugador = f"jug{str(ultimo_id_jug + 1).zfill(3)}"

    #formato que se añadira al Acces.json en lista de jugadores del equipo correspondiente:
    nuevo_jugador = {
        "ID": nuevo_id_jugador,
        "nombre": nombre,
        "numero de camisa": numero_camisa,
        "posicion": posicion,
        "id_equipo": id_equipo,
        "estadisticas": {
            "partidos_jugados": 0,
            "goles": 0,
            "asistencias": 0,
            "tarjetas_amarillas": 0,
            "tarjetas_rojas": 0,
            "minutos_jugados": 0
        }
    }
    #aqui usamos el setdefault() que es una funcion que sirve para buscar si la llave Jugadores esta dentro del equipo en especifico
    #si no esta, entonces la crea y añade el valor adentro de jugadores
    #si esta simplemente añade al jugador alla adentro
    for equipo in datos_del_json["Equipos"]:
        if equipo["ID"] == id_equipo:
            equipo.setdefault("Jugadores", []).append(nuevo_jugador)
            print("Listo ya registre a:", nuevo_jugador["nombre"], "en el equipo:", id_equipo)
            break
    else:
        print(f"Perdon pero el ID:{id_equipo} no lo encontre por ninguna parte")
    
    guardar_datos(datos_del_json)

#ahora vamos a crear una funcion que va a buscar a un jugador existente en el JSON 
def buscar_jugador(criterio: str, valor):
    datos_del_json = cargar_datos()
    jugadores_encontrados = []  # aquí se van a guardar los jugadores encontrados

    # Recorremos cada equipo en la lista de equipos
    for equipo in datos_del_json.get("Equipos", []): 
        for jugador in equipo.get("Jugadores", []):
            # Imprimir el jugador y el criterio para depuración
            if jugador.get(criterio) == valor:
                jugadores_encontrados.append(jugador)

    # Si la lista jugadores_encontrados no tiene nada, se hará el else
    if jugadores_encontrados:  
        for jugador in jugadores_encontrados:
            print("Jugador encontrado:", jugador)  # devuelve toda la información de ese jugador
    else:  # si la lista está vacía es porque no encontró ningún valor
        print(f"No se encontró ningún jugador con {criterio} = {valor}.")

    
#ahora vamos a crear una funcion que va a actualizar las estadisticas de un jugador existente en el JSON
def actualizar_estadisticas_jugador(id_jugador: str):
    datos_del_json = cargar_datos()

    #crearemos un ciclo for con .get() para los diccionarios y para que pueda acceder al jugador en especifico
    for equipo in datos_del_json["Equipos"]:
        for jugador in equipo.get("Jugadores", []):
            if jugador["ID"] == id_jugador:
                print("Actualizando estadisticas del jugador:", jugador['nombre'])
                #aqui usamos mas verificadores para las estadisticas de los jugadores:

                partidos_jugados = int(input("Cuantos partidos ha jugado?: "))
                while partidos_jugados < 0 or partidos_jugados > 10:
                    if partidos_jugados < 0:
                        print(f"Oiga que le pasa, como que {partidos_jugados}?, no se pueden numeros negativos")
                    else:
                        print(f"Oiga que le pasa como que jugo mas de {partidos_jugados}?, si el maximo son 10")
                    partidos_jugados = int(input("Cuantos partidos ha jugado?: "))

                goles = int(input("Cuantos goles ha marcado?: "))
                while goles < 0 or goles > 10:
                    if goles < 0:
                        print(f"Como que asi que metio {goles}?, nadie mete goles negativos")
                    else:
                        print(f"Como que metio {goles}?, eso es imposible")
                    goles = int(input("Cuantos goles ha marcado?: "))

                asistencias = int(input("Cuantas asistencias ha dado?: "))
                while asistencias < 0 or asistencias > 10:
                    if asistencias < 0:
                        print(f"Como asi que asistio {asistencias}?, nadie asiste en negativo")
                    else:
                        print(f"Como asi que asistio {asistencias}?, nadie asiste demasiado en un partido")
                    asistencias = int(input("Cuantas asistencias ha dado?: "))

                tarjetas_amarillas = int(input("Cuantas tarjetas amarillas ha recibido?: "))
                while tarjetas_amarillas < 0 or tarjetas_amarillas > 2:
                    if tarjetas_amarillas < 0:
                        print(f"Como asi que saco {tarjetas_amarillas}?, nadie saca tarjetas amarillas en negativo")
                    else:
                        print(f"Como asi que le sacaron {tarjetas_amarillas}?, si cuando le sacan 2 ya es roja")
                    tarjetas_amarillas = int(input("Cuantas tarjetas amarillas ha recibido?: "))

                tarjetas_rojas = int(input("Cuantas tarjetas rojas ha recibido?: "))
                while tarjetas_rojas < 0 or tarjetas_rojas > 1:
                    if tarjetas_rojas < 0:
                        print(f"Como asi que le sacaron {tarjetas_rojas}?, nadie saca tarjetas rojas en negativo")
                    else:
                        print(f"Como asi que le sacaron {tarjetas_rojas}, si el maximo es 1 sola y lo expulsan")
                    tarjetas_rojas = int(input("Cuantas tarjetas rojas ha recibido?: "))

                minutos_jugados = int(input("Cuantos minutos ha jugado?: "))
                while minutos_jugados < 0 or minutos_jugados > 100:
                    if minutos_jugados < 0:
                        print(f"Como asi que jugo {minutos_jugados}?, si el minimo es 0, nadie juega en minutos negativos")
                    else:
                        print(f"Como asi que jugo {minutos_jugados}?, si el maximo por 1 partido son 100 a lo mucho")
                    minutos_jugados = int(input("Cuantos minutos ha jugado?: "))

                if tarjetas_amarillas >= 2:
                    tarjetas_rojas = 1
                    tarjetas_amarillas = 0
                
                #profe este es el actualizador de estadisticas de los jugadores con "+=" 
                #para que en caso de que el jugador ya tuviera unos goles de (ej:4) si lo vuelvo a actuallizar, se sume al valor anterior
                #sino estaria sobre escribiendo los valores anteriores, para no llevar un contador, sino un sumador
                jugador["estadisticas"]["partidos_jugados"] = partidos_jugados
                jugador["estadisticas"]["goles"] += goles
                jugador["estadisticas"]["asistencias"] += asistencias
                jugador["estadisticas"]["tarjetas_amarillas"] += tarjetas_amarillas
                jugador["estadisticas"]["tarjetas_rojas"] += tarjetas_rojas
                jugador["estadisticas"]["minutos_jugados"] += minutos_jugados
                
                #aqui imprime en la consola, el nombre del jugador, y que sus estadisticas fueron actualizadas 
                print("Wepa las estadisticas las pude actualizar. :D")
                print("Bueno las estadisticas:", jugador['nombre'], "quedaron asi: ")
                print(f"Partidos jugados: {jugador['estadisticas']['partidos_jugados']}")
                print(f"Goles: {jugador['estadisticas']['goles']}")
                print(f"Asistencias: {jugador['estadisticas']['asistencias']}")
                print(f"Tarjetas amarillas: {jugador['estadisticas']['tarjetas_amarillas']}")
                print(f"Tarjetas rojas: {jugador['estadisticas']['tarjetas_rojas']}")
                print(f"Minutos jugados: {jugador['estadisticas']['minutos_jugados']}")

                guardar_datos(datos_del_json)
                return #este return vacio es porque necesito que la funcion def termine en cuanto actualice las estadisticas del jugador en el Acces.json
    #si lo de atras no funciono es porque el id del jugador no se encontro por ningun lado
    print("Intente hasta el cansancio buscar al jugador, pero es que: ", id_jugador, " no existe")
    