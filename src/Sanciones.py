from almacenador import cargar_datos, guardar_datos

def es_fecha_valida(fecha_de_inicio: str):
    #Aca comenzamos diciendo que si la palabra "a las" no esta en fecha_de_inicio se printea el texto especifico
    if " a las " not in fecha_de_inicio:
        print("Error: La fecha debe incluir ( a las ) en el formato: 'AAAA-MM-DD [a las] HH:MM'.")
        return False   
    
    #En esta parte usamos otro if para decir que si la longitud de "AAAA-MM-DD a las HH:MM" es superada entonces saldra ese print
    #para que sepan el orden seria el numero 1 (AAAA-MM-DD), un separador (a las) y el numero 2 (HH:MM)
    fecha_partes = fecha_de_inicio.split(" a las ")    
    if len(fecha_partes) != 2:
        print("Error: La fecha debe ser escrita: '(AAAA-MM-DD a las HH:MM)'.")
        return False 

    #definimos tanto los parametro de las fechas y las separaciones que las componen
    la_fecha = fecha_partes[0]
    la_hora = fecha_partes[1]
    partes = la_fecha.split('-')

    #el condicional if para definir que si la longitud de la lista es deferente de "anio", "mes" y "dia", osea 3, sale el print correspondiente
    if len(partes) != 3:
        print("Error: La fecha debe tener el formato AAAA-MM-DD.")
        return False
    anio = partes[0]
    mes = partes[1]
    dia = partes[2]

    #Eeste es el if de anio que ya fue usado
    if not anio.isdigit() or len(anio) != 4:
        print("Error: El año debe exactamente 4 digitos.")
        return False
    #El if de mes que tambien ya fue usado
    if not mes.isdigit():
        print("Error: El mes debe contener solo numeros.")
        return False
    
    if int(anio) < 2025:
        print("Error: La fecha debe estar despues del 16 de octubre de 2025.")
        return False

    if int(anio) == 2025:
        if int(mes) < 10:
            print("Error: La fecha debe estar despues del 16 de octubre de 2025.")
            return False
        elif int(mes) == 10:
            if int(dia) <= 16:
                print("Error: La fecha debe estar despues del 16 de octubre de 2025.")
                return False

    if not 1 <= int(mes) <= 12:
        print("Error: El mes debe estar entre 01 y 12.")
        return False

    #los dias posibles en los cuales se puede digitar la sancion
    dias_por_mes = {
        1: 31,
        2: 28, 
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

    if int(dia) < 1 or int(dia) > dias_por_mes[int(mes)]:
        print(f"Error: El dia debe estar entre 1 y {dias_por_mes[int(mes)]} para el mes {mes}.")
        return False
    #El if que determina si el usiario digito o no de la forma coprrecta
    if not dia.isdigit():
        print("Error: El dia solo puede ser un numero.")
        return False

    dia_enterito = int(dia)
    
    maxi_dias_del_mesesito = dias_por_mes[int(mes)]

    if dia_enterito < 1 or dia_enterito > maxi_dias_del_mesesito:
        print(f"Error: El dia debe estar entre 01 y {maxi_dias_del_mesesito} para el mes de {mes}.")
        return False
    
    #Las espesificaciones que se necesitan para la parte de la fecha que define la hora es:
    #La forma correcta de de que se digite es "HH:MM" en ese misma forma 
    las_partes_de_la_hora = la_hora.split(':')
    if len(las_partes_de_la_hora) != 2:
        print("Error: La hora debe tener este formato: HH:MM.")
        return False 
    hora = las_partes_de_la_hora[0]
    minuto = las_partes_de_la_hora[1]
    # esta es la parte de "hora" donde se define la hora espesifica
    if not hora.isdigit() or int(hora) < 0 or int(hora) > 23:
        print("Error: La hora debe estar en formato militar entre las 00:00 y las 23:00")
        return False
    # y esta otra espara los minutos que van en la hora digitada
    if not minuto.isdigit() or int(minuto) < 0 or int(minuto) > 59:
        print("Error: Los minutos deben estar entre 00 y 59")
        return False
    return True
    
def verificar_fecha(fecha_de_inicio):
        datos_del_json = cargar_datos()
        
        if not es_fecha_valida(fecha_de_inicio):
            return False
        
        #este ciclo for quiere conseguir que cuando alla un partido registrado en el mismo dia, directamente no lo genre
        #Por ello mismo el "_" nos quiere decir que vaya y busque especificamente le parametro dia em datos_del_json (partidos)<
        fecha_dia, _ = fecha_de_inicio.split(" a las ")
        for partido in datos_del_json.get("Partidos", []):
            ya_hay_fecha, _ = partido["fecha"].split(" a las ")
            if fecha_dia == ya_hay_fecha:
                print(f"Error: Ya existe un partido registrado el {fecha_dia} y no se puede registrar mas de 1 partido el mismo dia, lo siento.")
                print("Intenta cambiar la fecha del partido")
                return False
        return True
     
def buscar_por_id(id_sancionado):
    datos_del_json = cargar_datos() 

    #Busca en los equipos
    for equipo in datos_del_json.get("Equipos", []):
        for jugador in equipo.get("Jugadores", []):  #Busca en los jugadores de cada equipo
            if jugador.get("ID") == id_sancionado:  #compara el ID del jugador con el ID sancionado
                print(f"Jugador encontrado: {jugador['nombre']}, con ID: {jugador['ID']}")
                for sancion in datos_del_json.get("Sanciones", []):  #busca en las sanciones
                    if sancion.get("id_sancionado") == id_sancionado:  #compara el ID sancionado
                        print(f"Error: El jugador {jugador['nombre']} ya tiene sanciones registradas")
                        return False  # Retorna False si ya tiene sanciones
                return True  # Retorna True si no tiene sanciones

    # busca en los equipos por ID de equipo
    for equipo in datos_del_json.get("Equipos", []):
        if equipo.get("ID") == id_sancionado:  # Compara el ID del equipo con el ID sancionado
            print(f"Equipo encontrado: {equipo['nombre']}, con ID: {equipo['ID']}")
            for sancion in datos_del_json.get("Sanciones", []): 
                if sancion.get("id_sancionado") == id_sancionado:  
                    print(f"Error: El equipo {equipo['nombre']} ya tiene sanciones registradas")
                    return False  
            return True  

   
    print(f"Que es {id_sancionado}?")
    return False  # Retorna False si no se encuentra

def registrar_sancion(tipo: str, id_sancionado: str, motivo: str, fecha_de_inicio: str, duracion: int, estado: str):
    datos_del_json = cargar_datos()  

    id_list = []
    for sancion in datos_del_json["Sanciones"]:
        id_num = int(sancion["id"][3:])  # Extrae el numero del ID
        id_list.append(id_num)

    ultimo_id = max(id_list, default=0)  # Obtiene el ultimo ID
    nuevo_id = f"san{str(ultimo_id + 1).zfill(3)}"  # Genera el nuevo ID

    nueva_sancion = {
        "id": nuevo_id,
        "tipo": tipo,
        "id_sancionado": id_sancionado,
        "motivo": motivo,
        "fecha_de_inicio": fecha_de_inicio,
        "duracion": duracion,
        "estado": estado
    }

    datos_del_json["Sanciones"].append(nueva_sancion)  #añade la nueva sancion a la lista

    guardar_datos(datos_del_json) 

    print(f"La sancion: {nueva_sancion['id']} fue correctamente registrada en el sistema.")

def actualizar_estado_sancion(id_sancion: str):
    datos_del_json = cargar_datos()  

    for sancion in datos_del_json["Sanciones"]:
        if sancion["id"] == id_sancion:  # Compara el ID de la sancion
            if sancion["estado"] == "activa":  # Verifica si la sancion esta activa
                sancion["estado"] = "cumplida"  # Cambia el estado a cumplida
                print("Listo, la sancion ya fue cumplida")

                guardar_datos(datos_del_json)  
                    
                return {}
            else:
                print("La sancion ya esta cumplida, no la puedo cambiar")
                return {}

    print("La sancion no existe.") 
    return {}

def generar_reporte_sanciones(tipo: str):
    if tipo not in {"jugador", "equipo"}:
        print(f"Error: El tipo {tipo} no es valido. intenta con: jugador o equipo")
        return []

    datos_del_json = cargar_datos()  

    sanciones_filtradas = []

    for sancion in datos_del_json["Sanciones"]:
        if sancion["tipo"] == tipo:  #filtra por tipo de sancion
            sanciones_filtradas.append(sancion)
        else:
            print("No se encontro la sancion")

    #esto ordena las sanciones filtradas por fecha de inicio
    n = len(sanciones_filtradas)
    for i in range(n):
        for j in range(0, n-i-1):
            if sanciones_filtradas[j]["fecha_de_inicio"] < sanciones_filtradas[j+1]["fecha_de_inicio"]:
                temp = sanciones_filtradas[j]
                sanciones_filtradas[j] = sanciones_filtradas[j+1]
                sanciones_filtradas[j+1] = temp

    #esto imprimira las sanciones filtradas
    for sancion in sanciones_filtradas:
        print(f"ID: {sancion['id']}, Tipo: {sancion['tipo']}, Estado: {sancion['estado']}, Fecha de Inicio: {sancion['fecha_de_inicio']}")

    return sanciones_filtradas  #retorna la lista de sanciones filtradas

