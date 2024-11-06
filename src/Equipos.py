#aqui vamos a traernos las funciones cargar_datos y guardar_datos que creamos en el archivo almacenador.py
from almacenador import cargar_datos, guardar_datos



#aqui vamos a crear in diccionario con ciudades de colombia validas para asignar a los equipos
CIUDADES_COLOMBIA = {
    "Amazonas": ["Leticia", "Puerto Narino"],
    "Antioquia": ["Medellin", "Bello", "Itagui", "Envigado", "Apartado", "Turbo"],
    "Arauca": ["Arauca", "Tame", "Saravena"],
    "Atlantico": ["Barranquilla", "Soledad", "Malambo", "Sabanalarga"],
    "Bolivar": ["Cartagena", "Magangue", "Turbaco", "Mompox"],
    "Boyaca": ["Tunja", "Sogamoso", "Duitama", "Chiquinquira"],
    "Caldas": ["Manizales", "La Dorada", "Chinchina"],
    "Caqueta": ["Florencia", "San Vicente del Caguan", "Cartagena del Chaira"],
    "Casanare": ["Yopal", "Aguazul", "Villanueva"],
    "Cauca": ["Popayan", "Santander de Quilichao", "Puerto Tejada"],
    "Cesar": ["Valledupar", "Aguachica", "Agustin Codazzi"],
    "Choco": ["Quibdo", "Istmina", "Riosucio"],
    "Cordoba": ["Monteria", "Lorica", "Sahagun", "Cerete"],
    "Cundinamarca": ["Bogota", "Soacha", "Facatativa", "Girardot", "Zipaquira"],
    "Guainia": ["Inirida"],
    "Guaviare": ["San Jose del Guaviare"],
    "Huila": ["Neiva", "Pitalito", "Garzon"],
    "La Guajira": ["Riohacha", "Maicao", "Fonseca", "Uribia"],
    "Magdalena": ["Santa Marta", "Cienaga", "Fundacion"],
    "Meta": ["Villavicencio", "Granada", "Acacias"],
    "Narino": ["Pasto", "Tumaco", "Ipiales"],
    "Norte de Santander": ["Cucuta", "Ocana", "Pamplona"],
    "Putumayo": ["Mocoa", "Puerto Asis", "Orito"],
    "Quindio": ["Armenia", "Calarca", "Montenegro"],
    "Risaralda": ["Pereira", "Dosquebradas", "Santa Rosa de Cabal"],
    "San Andres y Providencia": ["San Andres"],
    "Santander": ["Bucaramanga", "Floridablanca", "Piedecuesta", "Barrancabermeja"],
    "Sucre": ["Sincelejo", "Corozal", "Sampues"],
    "Tolima": ["Ibague", "Espinal", "Honda"],
    "Valle del Cauca": ["Cali", "Palmira", "Buenaventura", "Tulua"],
    "Vaupes": ["Mitu"],
    "Vichada": ["Puerto Carreno"]
}
#ahora haremos una funcion que verificara que la ciudad sea valida para el diccionario CIUDADES_COLOMBIA con 2 respuestas a retornar para su verificacion True or False
def es_ciudad_valida(ciudad):
        #para las ciudades que son los valores del diccionario que estan dentro de las claves de CIUDADES_COLOMBIA
        for ciudades in CIUDADES_COLOMBIA.values():
            #si la ciudad escrita por el usuario esta en las ciudades retorara verdadero
            if ciudad in ciudades:
                return True
        #de lo contrario imprimira una lista de recomendaciones con las ciudades que puede escribir el usuario
        print(f"Intenta con una de estas: {CIUDADES_COLOMBIA.values()} ")
        return False

#ahora haremos otra funcion que verifica que no se pueda registrar a un equipo con el mismo nombre
def nombre_valido(nombre):
    datos_del_json = cargar_datos() 
    #para los equipos que estan dentro de la lista de Equipos en Acces.json 
    for equipo in datos_del_json["Equipos"]:
        #si el nombre coincide con el equipo retornara falso esto es para que no pueda digitar el nombre de un equipo existente
        if nombre == equipo["nombre"]:
            return False  
        #si no retorna false es porque retornara true y si hace eso verifica que el nombre del equipo que puso el usuario es nuevo y no existe aun y por ende es valido
    return True

#ahora haremos otra funcion que registrara a un equipo en el JSON
def registro_equipo(nombre: str, ciudad: str, dt: str):
    datos_del_json = cargar_datos() 

    #creamos la lista para guardar los numeros 
    id_list = [] #aqui fue a parar el numero_id

    #aqui ira por cada equipo en la lista de equipos
    for equipo in datos_del_json["Equipos"]:
        # esto extrae el numero del ID del equipo
        # y el [3:] ignora los 3 primeros carateres que estan en comillas dobles: "eqp"-000 y toma el 000 y lo vuelve un entero osea 0
        # en palabras simples:
        # vuelve el eqp000 en esto: 000 y luego lo convierte a 0
        # y trabaja con ese 0
        numero_id = int(equipo["ID"][3:]) #000 = 0
        # añadimos el numero del ID a la lista
        id_list.append(numero_id)

    #esta funcion encuentra el ID maximo en la lista
    #si la lista no tiene ni un solo equipo 
    #va a crear al primer equipo con el id de eqp000 para que en el nuevo id que registre a ese 000 le sumemos 1 y quede 001
    #usamos la funcion max() para averiguar cual es el id maximo o mas grande de la lista de equipos, esto retorna el numero mas grande que haya
    #le pongo en default = 0 por si acaso no hay nada max() me retorne un 0
    #esto lo pusimos al principio de la creacion del programa debibo a que no habia equipos pero ahora es irrelevante
    #normalmente escojera a id_list que seria el numero actual y eso es lo que devolvera
    ultimo_id = max(id_list, default=0)

    #aqui generamos el ID para la nueva lista que se genere, añadiendole a eqp el ultimo id mas grande que verifico
    #luego le suma 1 para que no registre al mismo otra vez, ya que de base ya tenemos 11 equipos entonces, ultimo id (11) + 1, y lo llenamos con 000
    #pero verifica cada numero, osea (012 en vez de 12) esos 000 del .zfill(3), seran remplazados por 012
    #.zfill() funciona llenando de espacios vacios con ceros, si hay un 12 verifica que si hay numero no haga nada pero si esta vacio añada el que haga falta
    #si pongo .zfill(6) entonces queda eqp000001 para el primer equipo o si fuera el eqp000100, en caso tal que ya fuera por 100 equipos
    nuevo_id = (f"eqp{str(ultimo_id + 1).zfill(3)}") 

    # creamos el nuevo equipo con el formato del .json
    # asi es como se va a crear el nuevo equipo o como se va a añadir alla

        
    nuevo_equipo = {
        "ID": nuevo_id,
        "nombre": nombre,
        "ciudad": ciudad,
        "dt": dt,
        "Jugadores": [],
        "estadisticas": {
            "puntos": 0,
            "partidos_jugados": 0,
            "pganados": 0,
            "pempatados": 0,
            "pperdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    }

    #aqui añadiemos a equipos del json el nuevo equipo con la estrucutra anterior
    datos_del_json["Equipos"].append(nuevo_equipo)
    guardar_datos(datos_del_json)

    print(f"El equipo: {nuevo_equipo} fue registrado satisfactoriamente")
    


#ahora haremos otra funcion que buscara a un equipo en el JSON
def buscar_equipo(criterio: str, valor: str):
    datos_del_json = cargar_datos()
    #inicializamos como falso para que si lo encuentra retorne a encontrado como True
    encontrado = False

    #entonces por cada equipo en la lista de Equipos
    for equipo in datos_del_json["Equipos"]:
        #si el equipo encaja con el criterio que puede ser (ID, nombre, ciudad o dt)
        #verificara si tambien el valor que digito el usuario encaje tambien con el valor que esta en el equipo
        if equipo[criterio] == valor:
            #si todo encaja entonces encontrado se volvera True
            encontrado = True
            #e imprimira datos del encuentro
            #usamos end='' ya que nos sirve para que el print que esta despues de este print se imprima al lado del print anterior
            print(f"Nombre: {equipo['nombre']}, Ciudad: {equipo['ciudad']}, Director tecnico: {equipo['dt']},", end='')
            #aqui lo mismo para la linea siguiente
            print(" Jugadores: ", end='') 
            for jugador in equipo["Jugadores"]:
                print(f"{jugador['nombre']}, ", end='') #aca lo mismo para cada jugador que vaya encontrando lo imprimira al lado con la coma
            print() #un salto de linea xd, osea esto imprime algo vacio para que no se pegue con el menu
    #si lo encuentra retornara a encontrado como True 
    return encontrado 
    
#ahora haremos otra funcion que validara si el total de partidos jugados de un equipo es igual a la suma de los partidos ganados, perdidos y empatados 
def obtener_partidos(tipo: str, max_partidos: int):
    #inicializamos a partidos = -1 para que si el usuario digite algo negativo salgo el error
    partidos = -1
    while partidos < 0:
        partido_digitado = input(f"Cuantos {tipo}?: ")
        #esto verificara que halla unicamente numeros en la respuesta
        if partido_digitado.isdigit():
            partidos = int(partido_digitado)
            #esto verificara que el numero de partidos jugados no sea negativo
            if partidos < 0:
                print(f"Como asi que {tipo} {partidos} partidos?, nadie {tipo} en negativo")
            #esto verificara que el numero de partidos jugados no sea mayor a los partidos que tiene puede jugar un equipo
            elif partidos > max_partidos:
                print(f"Como asi que {tipo} mas de {partidos} de partidos?, si solo pueden jugar hasta {max_partidos} partidos")
        else:
            print(f"Como asi que {partido_digitado}?, eso no tiene sentido")
    return partidos

#ahora haremos otra funcion que actualizara las estadisticas o datos de un equipo en el JSON
def actualizar_estadisticas(id_equipo: str): 
    datos_del_json = cargar_datos()
    #encontramos al equipo con bucles for y si encaja con el parametro lo encuentra
    for equipo in datos_del_json["Equipos"]:
        if equipo["ID"] == id_equipo:
            print("Actualizando estadisticas del equipo:", equipo["nombre"])
            print("Recuerde que si ya hay unas estadisticas en un equipo, lo que escriba se le sumara a las anteriores estadisticas")
            
            #aqui definimos que el total de equipos sera la cantidad total de equipos que hay en los datos del Acces.json
            total_equipos = len(datos_del_json["Equipos"])
            max_partidos = total_equipos - 1  # y el -1 es porque un equipo no se puede enfrentar a si mismo
            #osea si existen 12 equipos el maximo de partidos que puede jugar el equipo es de 11 partidos

            #estas son variables que definimos aqui para que lo que retorne obtener partidos, lo podamos meter en las estadisticas
            pganados = obtener_partidos("ganaron", max_partidos)
            pempatados = obtener_partidos("empataron", max_partidos)
            pperdidos = obtener_partidos("perdieron", max_partidos)

            #si la suma no da los 11 partidos en este caso entonces le volvera a preguntar al usuario nuevamente hasta que registre bien
            while pganados + pempatados + pperdidos != max_partidos:
                print(f"La suma de partidos ganados, empatados y perdidos debe ser {max_partidos}. Actualmente es {pganados + pempatados + pperdidos}")
                print("Por favor, ajusta los valores")
                pganados = obtener_partidos("ganaron", max_partidos)
                pempatados = obtener_partidos("empataron", max_partidos)
                pperdidos = obtener_partidos("perdieron", max_partidos)
            #aqui definimos que jugados es la suma de todos los partidos
            partidos_jugados = pganados + pempatados + pperdidos
            #y los puntos que corresponder a la suma de los ganados * 3 y los empatados * 1
            puntos = (pganados * 3) + (pempatados * 1)

            #inicializamos esto como -1 para que pueda ejecutar el ciclo while
            goles_favor = -1
            #este bucle while verifica que los goles a favor no sean menores a 0 ni mayores a los maximos partidos posibles que se puedan jugar marcando un limete maximo de 10 goles por partido
            #en otras palabras 100 son los goles en este caso para poder meter
            #y otro verificador de que los goles a favor no pueden ser menores a los partidos ganados
            #esto porque si uno gana almenos los 10 partidos, se necesita almenos 1 gol por partido para ganar
            while goles_favor < 0 or goles_favor > max_partidos * 10 or goles_favor < pganados:
                goles_favor_input = input("Cuantos goles metieron?: ")
                if goles_favor_input.isdigit():
                    goles_favor = int(goles_favor_input)
                    if goles_favor < 0:
                        print("Nadie marca goles negativos")
                    elif goles_favor > max_partidos * 10:
                        print(f"El maximo es normalmente hasta {max_partidos * 10} en {max_partidos} partidos")
                    elif goles_favor < pganados:
                        print(f"Error: el numero de goles NO puede ser menor a los {pganados} partidos ganados")
                else:
                    print("Eso ni siquiera es un numero")

            #mas de lo mismo solo que la diferencia es que los goles en contra no puede ser superior a 100 goles
            #el calculo es en base a que si lo maximo de goles que normalmente se ve en la historia del futbol
            #serian 10 por partido, puede que haya excepciones y que haya mas pero eso solo aumenta su rareza
            goles_contra = -1
            while goles_contra < 0 or goles_contra > max_partidos * 10:
                goles_contra_input = input("Cuantos goles les metieron?: ")
                if goles_contra_input.isdigit():
                    goles_contra = int(goles_contra_input)
                    if goles_contra < 0:
                        print("Nadie marca goles negativos")
                    elif goles_contra > max_partidos * 10:
                        print(f"El maximo es normalmente hasta {max_partidos * 10} en {max_partidos} partidos")
                else:
                    print("Eso ni siquiera es un numero")

            #esto es lo que va a actualizar las estadisticas del equipo, reemplazando los valores por los del usuario
            #todos tiene += ya que la suma es acumulativa excepto para partidos jugados que solo actualizara el valor anterior
            equipo["estadisticas"]["partidos_jugados"] = partidos_jugados
            equipo["estadisticas"]["pganados"] += pganados
            equipo["estadisticas"]["pempatados"] += pempatados
            equipo["estadisticas"]["pperdidos"] += pperdidos
            equipo["estadisticas"]["goles_favor"] += goles_favor
            equipo["estadisticas"]["goles_contra"] += goles_contra
            equipo["estadisticas"]["puntos"] += puntos


            guardar_datos(datos_del_json)
            #si todo funciona retorna verdadero para romper el bucle while del menu
            print("Estadisticas actualizadas correctamente")
            return True
    #sino le volvera a pedir que digite nuevamente y retornara falso
    print("ID de equipo no encontrado")
    return False

    