from almacenador import cargar_datos, guardar_datos

def es_fecha_valida(fecha: str):
    #def es_fecha_valida esta hecha con el proposito de retornar verdaderos y falsos
    #esto es para que en las opciones del menu_partidos() pueda funcionar el bucle while, mientras no funcione correctamente
    #mas que todo para no tener siempre que volver a ejecutar la opcion en caso tal de que contenga errores del usuario

    #esto es para que verifique que separe la fecha y la hora con " a las " en el formato de fecha
    if " a las " not in fecha:
    #Si no encuentra el " a las " en la fecha escrita por el usuario, la retornara como falsa
        print("Error: La fecha debe incluir ( a las ) en el formato: 'AAAA-MM-DD [a las] HH:MM'")
        return False
      
    fecha_partes = fecha.split(" a las ")    
    #Aqui miramos si se cumple que la parte de la fecha este dividida entre 2 osea el (AAAA-MM-DD a las HH:MM)
    if len(fecha_partes) != 2:
        print("Error: La fecha debe ser escrita: '(AAAA-MM-DD a las HH:MM)'")
        return False 
    #Aqui se establecen nombres para las partes de la fecha 
    #como la fecha se divide en 2: (AAAA-MM-DD a las HH:MM)
    #AAAA-MM-DD va a ser la_fecha
    #HH:MM va a ser la_hora
    la_fecha = fecha_partes[0]
    la_hora = fecha_partes[1]
    #Esto revisa que la fecha este dividida con los guiones del medio ('-')
    partes = la_fecha.split('-')
    if len(partes) != 3:
        print("Error: La fecha debe tener el formato AAAA-MM-DD.")
        return False
    anio = partes[0] #La ñ no la podemos poner asi que por eso se llama anio
    mes = partes[1]
    dia = partes[2]

    #Esto verifica que el año NO contega algo mas que solo numeros, nada de strings o floats 
    #o que el año contenga hasta exactamente 4 numeros 
    if not anio.isdigit() or len(anio) != 4:
        print("Error: El año debe exactamente 4 digitos")
        return False
    
    #Aqui volvemos el año un entero para jugar con los datos ya que anteriormente era un string o una parte de la cadena: la_fecha
    anio_entero = int(anio)

    #si el año digitado es menor a 2024 error
    if anio_entero < 2024:
        print("Error: El año no puede ser anterior al 2024")
        return False
    
    #si el año digitado es mayor a 2027 error
    if anio_entero > 2027:
        print("Error: El año no debe superar al 2027")
        return False
    
    # O que el mes no sea ni menor a 1 ni mayor a 12 pero pueda ser igual a ellos 
    # Convertimos la cadena mes en un numero entero
    # para que podamos comparar el mes con los valores desde enero hasta diciembre
    if not mes.isdigit():
        print("Error: El mes debe contener solo numeros.")
        return False
    
    #el mes no puede ser menor a 1 pero puede ser igual a 1
    #el mes debe ser menor o igual a 12
    if not 1 <= int(mes) <= 12:
        print("Error: El mes debe estar entre 01 y 12.")
        return False
    #Establecer los dias de cada mes
    dias_por_mes = {
    #aqui pongo del primer lado los meses que van hasta 12, y al otro lado los dias maximos de cada mes
        1: 31, 
        2: 29 if int(anio) == 2024 else 28, #para febrero como es bisciesto puede aceptar hasta 29 dias si es 2024 en caso contrario 28 para 2025 en adelante
        3: 31, 
        4: 30, 
        5: 31, 
        6: 30, 
        7: 31, 
        8: 31, 
        9: 30, 
        10: 31, 
        11: 30, 
        12: 31 
    } 
    #validamos el dia con esta estructura:
    #si en el dia no hay digitos
    #entonces .isdigt() sirve para verificar si todos los caracteres del dia son unicamente numeros y no otra cosa rara
    #entonces si hay una letra o un punto o cualquier cosa que no sea de 0-9 va retornar falso
    if not dia.isdigit():
        print("Error: El dia solo puede ser un numero")
        return False
    #aqui definimos que el dia lo conviertiera en entero ya que en partes[2] que es el dia segun la estrucutra
    #hay que tener en cuenta que el formato para escribir el dia en la fecha debe der AAAA-MM-(DD)
    #DD debe ser escrito asi: 1 = 01, o 8 = 08, entonces para trabajar con ese numero y verificarlo en el calendario de dias_por_mes
    #toca convertirlo a entero usando int() y guardandolo en alguna variable que llamaremos: dia_enterito
    dia_enterito = int(dia)
    # ahora creamos un max para especificar que maxi_dias_del_mesesito sean los dias_por_mes segun el mes volverlo entero
    # ya que MM debe ser escrito asi: 01 = 1 y 09 = 9, para poder usarlo, ya que python no usa numeros con ceros sin coma a la izquierda
    maxi_dias_del_mesesito = dias_por_mes[int(mes)]
    #si se cumple que el dia sea menor a 1 
    # o que el dia sea superior a los dias del mes
    if dia_enterito < 1 or dia_enterito > maxi_dias_del_mesesito:
        #Va a generar un print con un error en los datos digitados, ya que el dia no puede ser menor a 1 y mayor a los dias del mes correspondiente
        #y la retorna como falsa
        print(f"Error: El dia debe estar entre 01 y {maxi_dias_del_mesesito} para el mes de {mes}")
        return False
    #aqui validaremos que la hora este bien escrita
    #para eso definimos las_partes_de_la_hora como la la_hora que era fecha_partes[1] con un separador con la funcion split()
    #split() que sirve para dividir una cadena de texto en partes mas pequeñas
    #split puede tomar hasta 2 argumentos, hay que especificarle como esta dividida la cadena (seria el primer argumento) 
    #(el segundo argumento es es un el numero de ":" que queremos que use)
    #pero como en HH:MM solo hay uno pues no es necesario especificar el 1, ya que seria redundante
    #en este caso HH:MM, esta dividida por ":"
    las_partes_de_la_hora = la_hora.split(':')
    if len(las_partes_de_la_hora) != 2:
        #si la logintud de las partes de la hora osea HH y MM es diferente de 2 
        #esta retornara un falso aparte del mensaje de error
        print("Error: La hora debe tener este formato: HH:MM.")
        return False 
    #aqui establecimos la hora como la primera posicion o formato de escritura en orden
    #y el minuto como la segunda posicion
    #para que el formato quede: (hora,minuto) o expresado tambien como HH:MM
    hora = las_partes_de_la_hora[0]
    minuto = las_partes_de_la_hora[1]
    #ahora si la hora no tiene digitos generara error
    #si la hora digitada es menor a 7 entonces error 
    #si la hora digitada es mayor a 21 entonces error
    #Esto lo colocamos asi ya que los partidos no pueden ser en horas tan tarde o en la madrugada
    #digo todo es posible pero seria lo ideal en un horario mas normal
    #volvemos la hora entero en caso sea desde 09 hasta 07 osea serian 09 = 9 y 08 = 8 y 07 = 7
    #para que el programa lo pueda identificar correctamente
    if not hora.isdigit() or int(hora) < 7 or int(hora) > 21:
        print("Error: La hora debe estar en formato militar entre las 07:00 y las 21:00")
        return False
    #aqui es el mismo proceso para los minutos, aparte de que se vuelvene enteros para todos los numeros que inicien con 0 algo
    #con la diferencia de que los minutos no pueden ser menores a 0 o negativos ni mayores a 59 ya que cuando llegue a 60 cambia de hora
    if not minuto.isdigit() or int(minuto) < 0 or int(minuto) > 59:
        print("Error: Los minutos deben estar entre 00 y 59")
        return False
    return True
    
#esta funcion nos sirve para verificar que la fecha sea valida y no este registrada en el sistema, esto es para que no registre un partido el mismo dia
def verificar_fecha(fecha):
    datos_del_json = cargar_datos()
    if not es_fecha_valida(fecha):
        return False
    #aqui solo usamos la fecha del dia, ya que la hora importa poco, y en python "_" sirve para ignorar el segundo parametro
    #ya que si encuentra la fecha registrada por el usuario en algun partido retornara False para que genere un error
    fecha_del_dia, _ = fecha.split(" a las ")
    #aqui fecha del dia va dividida por el a las (AAAA-MM-DD a las HH:MM)
    for partido in datos_del_json.get("Partidos", []):
        #aqui establecemos que ya_hay_fecha y "_", va aser igual a la fecha del partido que estan en los partidos del Acces.json 
        ya_hay_fecha, _ = partido["fecha"].split(" a las ") #que tambien esta dividido por un (a las)
        if fecha_del_dia == ya_hay_fecha:
            #ahora si la fecha del dia que seria el que esta antes de (a las) es igual a  ya_hay_fecha que tambien es el que esta antes del (a las) en los partidos del Acces.json
            #en otras palabras si la fecha digitada ya esta en el sistema, entonces generara este print indicandole al usuario el error
            print(f"Error: Ya existe un partido registrado el {fecha_del_dia}")
            #retorna false para que le notifique a registrar_partido
            return False
    #si no hay fechas registradas, entonces todo esta bien, retorna true
    return True

#esta funcion ahora verificara que haya sanciones activas
def hay_sanciones_activas(id_sancionado):
    datos_del_json = cargar_datos()
    #aqui obtiene todas las sanciones activas de Sanciones
    for sancion in datos_del_json.get("Sanciones", []):
        #y si el id del sancionado esta en sanciones y aparte esta activo entonces retorna true
        #para que active que hay sanciones activas
        if sancion["id_sancionado"] == id_sancionado and sancion["estado"] == "activa":
            #retorna true si encontro sanciones y aparte estan activas
            return True
    #retorna falso si no encontro sanciones
    return False

def equipo_tiene_sanciones(equipo_id):
    datos_del_json = cargar_datos()
    for sancion in datos_del_json.get("Sanciones", []):
        #entonces si el jugador esta en el equipo y la sancion esta activa
        if sancion["id_sancionado"] == equipo_id and sancion["estado"] == "activa":
            #retorna que el equipo tiene a un jugador sancionado
            return True
    #y para el jugador en el equipo mira si tiene el jugador tiene sanciones
    for equipo in datos_del_json.get("Equipos", []):
        if equipo["ID"] == equipo_id:
            for jugador in equipo.get("Jugadores", []):
                if hay_sanciones_activas(jugador["ID"]):
                    return True
    return False

def registrar_partido(fecha: str, equipo_local: str, equipo_visitante: str):
    datos_del_json = cargar_datos()

    #esto toma 2 parametros 
    fecha_del_dia, _ = fecha.split(" a las ")
    anio, mes, dia = map(int, fecha_del_dia.split('-'))
    
    fecha_limite = (2025, 10, 16)
     # aqui definimos a sancionar jugadores como si la fecha digitada del usuario supera a la fecha_limite
    sancionar_jugadores = (anio, mes, dia) > fecha_limite

    #esto invoca que si la fecha no es valida entonces la llama, si lo es no invoca a es_fecha_valida
    if not es_fecha_valida(fecha):
        return  
    
    #se permite registrar el partido sin considerar sanciones
    print("El partido se puede registrar")

    lista_de_ids = []
    for partido in datos_del_json["Partidos"]:
        id_del_partido_sin_part = partido["ID"][4:]  
        id_del_partido_entero = int(id_del_partido_sin_part)         
        lista_de_ids.append(id_del_partido_entero)

    alineacion_loc = []  # aqui metemos a los primeros 11 jugadores 
    banca_loc = []  # los que sobren o esten sancionados a banca    
    alineacion_vis = []  
    banca_vis = []       

    #aqui buscamos a los jugadores del equipo local y los metemos al partido a la alineacion local los primeros 11
    for equipo in datos_del_json["Equipos"]:
        if equipo["ID"] == equipo_local:
            jugadores = equipo.get("Jugadores", [])
            for jugador in jugadores:
                #aqui verificamos si la fecha supera el limite, si lo supera, sancionara a los jugadores y si tienen sanciones lo pondra en la banca
                #y aparte mostrara un mensaje de aviso de que el jugador esta sancionado y y el motivo por el que se pondra en la banca
                if sancionar_jugadores and hay_sanciones_activas(jugador["ID"]):
                    banca_loc.append(f"{jugador['ID']}(sancionado)")
                    print(f"El jugador {jugador['ID']} esta sancionado y se coloca en la banca")
                else:
                    alineacion_loc.append(jugador["ID"])
                # aqui definimos que la alineacion tenga a 11 jugadores
                if len(alineacion_loc) == 11:
                    break

            # como esto imprime a uno por uno en orden
            #si hacen falta jugadores en la alineacion entonces escoje uno que no este sancionado y el sancionado ira a la banca 
            for jugador in jugadores:
                if len(alineacion_loc) < 11:
                    if jugador["ID"] not in alineacion_loc:
                        if sancionar_jugadores and hay_sanciones_activas(jugador["ID"]):
                            banca_loc.append(f"{jugador['ID']}(sancionado)")
                        else:
                            alineacion_loc.append(jugador["ID"])

    #lo mismo aqui para el equipo visitante
    for equipo in datos_del_json["Equipos"]:
        if equipo["ID"] == equipo_visitante:
            jugadores = equipo.get("Jugadores", [])
            for jugador in jugadores:
                if sancionar_jugadores and hay_sanciones_activas(jugador["ID"]):
                    banca_vis.append(f"{jugador['ID']}(sancionado)")
                    print(f"El jugador {jugador['ID']} esta sancionado y se coloca en la banca")
                else:
                    alineacion_vis.append(jugador["ID"])
                if len(alineacion_vis) == 11:
                    break

            for jugador in jugadores:
                if len(alineacion_vis) < 11:
                    if jugador["ID"] not in alineacion_vis:
                        if sancionar_jugadores and hay_sanciones_activas(jugador["ID"]):
                            banca_vis.append(f"{jugador['ID']}(sancionado)")
                        else:
                            alineacion_vis.append(jugador["ID"])

    #aqui nos aseguramos de que la banca tenga 3 jugadores ya que 11 juegan y 3 se sientan y mas el sancionado
    #si la longitud de la banca local es menor a 3 y si la alineacion local mas la alineacion de la banca
    #es menor a la longitud de los jugadores
    while len(banca_loc) < 3 and len(alineacion_loc) + len(banca_loc) < len(jugadores):
        for jugador in jugadores:
            if jugador["ID"] not in alineacion_loc and f"{jugador['ID']}(sancionado)" not in banca_loc:
                banca_loc.append(jugador["ID"])
                if len(banca_loc) == 3:
                    break
    #lo mismo para la banca visitante                
    while len(banca_vis) < 3 and len(alineacion_vis) + len(banca_vis) < len(jugadores):
        for jugador in jugadores:
            if jugador["ID"] not in alineacion_vis and f"{jugador['ID']}(sancionado)" not in banca_vis:
                banca_vis.append(jugador["ID"])
                if len(banca_vis) == 3:
                    break

    #esto asigna el id del partido al nuevo partido como part000 tal y verifica el ultimo partido para que el nuevo sea el id del anterior + 1
    ultimo_id_part = max(lista_de_ids, default=0)
    nuevo_id_part = f"part{str(ultimo_id_part + 1).zfill(3)}"
    #Este es el formato que se va a guardar en el Acces.json
    nuevo_partido = {
        "ID": nuevo_id_part,
        "fecha": fecha,  
        "id_arbitro": "",
        "equip_loc": equipo_local,
        "equip_vis": equipo_visitante,
        "goles_loc": 0,
        "goles_vis": 0,
        "alineacion_loc": alineacion_loc,
        "banca_loc": banca_loc,
        "alineacion_vis": alineacion_vis,
        "banca_vis": banca_vis,
        "eventos": []
    }

    datos_del_json["Partidos"].append(nuevo_partido)
    print("El partido fue registrado correctamente")

    guardar_datos(datos_del_json)


def actualizar_resultado(id_partido:str,goles_local:int, goles_visitante:int):
    datos_del_json = cargar_datos()
    #esta funcion actualiza los goles de un partido
    for partido in datos_del_json["Partidos"]:
        #aqui si encuentra al partido procede a actualizar sus los goles del partido
        if partido["ID"] == id_partido:
            print("Actualizando resultados del partido: ", partido['ID'])

            #aqui los guardamos en estas variables para que alla en la estructura del Acces.json en estadisticas se actualicen los goles
            partido["goles_loc"] = goles_local
            partido["goles_vis"] = goles_visitante

            Hecho = (f"Perfecto, las estadisticas del partido: {id_partido}, fueron actualizadas")
            print(f"Estas son las nuevas estadisticas del partido: {id_partido}")
            print(f"Goles del local: {goles_local}")
            print(f"Goles del visitante: {goles_visitante}")

            guardar_datos(datos_del_json)
            return Hecho
    #en caso tal de que en la secuencia for no encuentre nada entonces imprimira esto, como una especie de mensaje error
    print("El ID de ese partido no existe.")
    
#esta funcion busca si los jugadores estan sancionados, esto para que no lo pueda registrar en el evento del partido
def esta_sancionado(jugador_id, sanciones):
    for sancion in sanciones:
        if sancion["id_sancionado"] == jugador_id and sancion["estado"] == "activa":
            return sancion  
    return None

def registrar_evento(Id_partido: str, Minuto: int, Tipo: str, Jugador: str):
    datos_del_json = cargar_datos()
    #aqui definimos sanciones como todas las sanciones que estan dentro de Sanciones
    sanciones = datos_del_json.get("Sanciones", [])

    partido_encontrado = False 
    equipo_local_id = None
    equipo_visitante_id = None

    for partido in datos_del_json["Partidos"]:
        if partido["ID"] == Id_partido:
            partido_encontrado = True
            equipo_local_id = partido["equip_loc"]
            equipo_visitante_id = partido["equip_vis"]
            print("Actualizando eventos del partido:", partido["ID"])
            break

    if not partido_encontrado:
        print(f"El ID del partido: '{Id_partido}' no fue encontrado")
        return

    jugador_encontrado = False
    equipo_id = None

    for equipo in datos_del_json["Equipos"]:
        if equipo["ID"] in [equipo_local_id, equipo_visitante_id]:
            for jugadorcito in equipo.get("Jugadores", []):
                if jugadorcito["ID"] == Jugador:
                    jugador_encontrado = True 
                    equipo_id = equipo["ID"]
                    # esto revisa si el jugador esta sancionado
                    if esta_sancionado(Jugador, sanciones):
                        #si lo esta imprime este mensaje de error
                        print(f"Error: el jugador: {Jugador} esta sancionado y no puede registrarse un evento con su ID")
                        return  
                    break
            if jugador_encontrado:
                break
            
    if not jugador_encontrado:
        print(f"El ID del jugador: {Jugador} no pertenece a ningun equipo del partido: {Id_partido}")
        return

    if equipo_id not in [equipo_local_id, equipo_visitante_id]:
        print(f"El ID del equipo del jugador: {Jugador}, no pertenece al partido")
        return

    #si ya existe un gol registrado en el minuto tal y el usuario quiere volver a registrar otro gol en el mismo minuto no se va a poder
    for evento in partido.get("eventos", []):
        #si minuto es igual al minuto ya digita y si el evento encima es otro gol, no se podra registrar
        if evento["Minuto"] == Minuto and evento["Tipo"] == "gol":
            print(f"Lo siento pero ya existe un gol registrado en el minuto {Minuto}")
            print("No pueden existir dos goles en un mismo minuto")
            return 

    #formato del nuevo evento que se guardara en el json
    nuevo_evento = {
        "Minuto": Minuto,
        "Tipo": Tipo,
        "Jugador": Jugador,
        "Equipo": equipo_id
    }
    #si el apartado de eventos no existe en el partido, setdefault() crea eventos como una lista vacio y ahi añade con .append el nuevo evento
    partido.setdefault("eventos", []).append(nuevo_evento)
    print("El evento fue añadido")

    guardar_datos(datos_del_json)

    #el nuevo evento registrado aparecera impreso asi en la consola
    print("Este es el nuevo evento del partido:", partido["ID"])
    print(f"Minuto: {Minuto}")
    print(f"Tipo: {Tipo}")
    print(f"Jugador: {Jugador}")
    print(f"Equipo: {equipo_id}")






