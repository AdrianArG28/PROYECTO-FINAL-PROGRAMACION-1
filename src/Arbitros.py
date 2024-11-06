#aqui vamos a traernos las funciones cargar_datos y guardar_datos que creamos en el archivo almacenador.py
from almacenador import cargar_datos, guardar_datos


#ahora crearemos otra funcion que va a ser una especie de validador que mirara que el nombre no se repita en el registro de arbitros
def nombre_valido_arb(nombre):
    #aqui mediante la funcion de cargar_datos vamos a cargar los datos del JSON
    datos_del_json = cargar_datos()
    #aqui mira arbitro por arbitro en las lista de arbitros del JSON
    for arbitro in datos_del_json["Arbitros"]:
        #y haremos una condicion que si el nombre lo encuentra entonces retorne un error
        #con el objetivo de que no permita registrar ese nombre otra vez
        if nombre == arbitro["nombre"]:
            return False  
    #si no lo encuentra entonces es valido para usarse
    return True

#ahora crearemos otra funcion que va a ser la que se encargue de registrar el arbitro en el JSON
def registrar_arbitro(nombre: str, experiencia: int, categoria: str):
    datos_del_json = cargar_datos()

    #esta va a ser la lsita que va a guardar todos los numeros que llevan todos los ids de todos los arbitros actuales
    id_list = [] 
    
    #usamos la misma estructura para los ids usados anteriormente
    for arbitros in datos_del_json["Arbitros"]:
        id_num = int(arbitros["id"][3:]) 
        id_list.append(id_num)

    ultimo_id = max(id_list, default=0)
    nuevo_id = (f"arb{str(ultimo_id + 1).zfill(3)}")
    #este va a ser el esquema que se va a añadir al Acces.json
    nuevo_arbitro = {
            "id": nuevo_id,
            "nombre": nombre,
            "experiencia": experiencia,
            "categoria": categoria,
            "partidos_dirigidos": 0
        }
    #aqui va a meter en arbitros el nuevo arbitro con el esquema anterior
    datos_del_json["Arbitros"].append(nuevo_arbitro)

    guardar_datos(datos_del_json)
    #aqui imprimira un mensaje de que funciono
    print(f"El arbitro: {nuevo_arbitro} acaba de ser registrado correctamente.")

#ahora crearemos otra funcion que va a ser la que se encargue de asignar los arbitros en los partidos en el JSON
def asignar_arbitro(id_partido: str, id_arbitro: str):
        datos_del_json = cargar_datos()
        
        #marcamos como falsas estas variables para que si funcionan las volvamos verdaderas
        partido_encontrado = False
        arbitro_encontrado = False
        
        #esto encuentra al partido, y luego la fecha de asignacion del arbitro sera la misma de la fecha del partido
        for partido in datos_del_json["Partidos"]:
            if partido["ID"] == id_partido:
                fecha = partido["fecha"]
                #si si lo encuentra partido_encontrado la volvemos verdadera
                partido_encontrado = True
                #y esto mira que el arbitro exista 
                #para que si lo llega ha encontrar 
                #en la seccion de id arbitro del partido especifico se registe o se llene con el id del arbitro que vamos a asignar
                for arbitro in datos_del_json["Arbitros"]:
                    arbitro_id = arbitro.get("id", [])
                    if arbitro_id == id_arbitro:
                        #si lo encuentra pues la volvemos en true
                        arbitro_encontrado = True
                        #y esto va al id del arbitro en el partido y le asignamos el arbitro 
                        partido["id_arbitro"] = id_arbitro
        #este es el manejo de errores
        #si el partido existe pero el arbitro no entonces error
        if partido_encontrado and not arbitro_encontrado:
            print("Error: Encontre el partido pero no encontre al arbitro")
        #si el arbitro existe y el partido no entonces otro error
        elif arbitro_encontrado and not partido_encontrado:
            print("Error: Encontre al arbitro, pero no pude encontrar al partido")
        #si el partido existe y el arbitro tambien le enviamos un mensaje de confirmacion de la asignacion correctamente
        elif partido_encontrado and arbitro_encontrado:
            print(f"\nListo, añadi al arbitro al partido: {id_partido}")
            print(f"El arbitro: {id_arbitro}, fue asignado para la fecha: {fecha}")
        #si ni el arbitro ni el partido existen entonces generar este mensaje de error
        else:
            print("Error: No se encontro ni al partido ni al arbitro")  

        #y ahora aqui mediante la funcion de guardar_datos vamos a guardar los datos en el JSON
        guardar_datos(datos_del_json)
        #se que no es comun retornar esto pero es un diccionario que nos sirve que si el partido y el arbitro fuero encontrados
        #el menu podria interpretar esto como correcto ya que alla le pedimos condiciones al partido y al arbitro
        #y esto es necesario para que el menu de arbitros lo pueda interpretar
        #es que son variables que retornamos de la funcion para que el menu pueda hacer las validaciones
        return {
            'partido_encontrado': partido_encontrado,
            'arbitro_encontrado': arbitro_encontrado
        }

#y ahora aqui finalmente crearemos otra funcion que va a ser la que se encargue de generar reportes de todos los arbitros en el JSON
def generar_reporte_arbitros():
    datos_del_json = cargar_datos()
    #definimos para no tener que escribir la lista de arbitros como viene de fabrica
    #asi que le asignamos un nombre
    arbitros = datos_del_json["Arbitros"]

    #ahora aqui usaremos el metodo burbuja para ordenar los reportes de primero a ultimo
    n = len(arbitros)
    for i in range(n):
        for j in range(0, n-i-1):
            partidos_j = arbitros[j].get("partidos_dirigidos", 0)
            partidos_j1 = arbitros[j+1].get("partidos_dirigidos", 0)
            if partidos_j < partidos_j1:  
                arbitros[j], arbitros[j+1] = arbitros[j+1], arbitros[j]
    #aqui fue usado la abreviacion de arbitros de la linea de arriba
    for arbitro in arbitros:
        id_arbitro = arbitro["id"]
        nombre_arbitro = arbitro.get("nombre", [])  
        partidos_dirigidos = arbitro.get("partidos_dirigidos", 0)  
        print(f"Para el arbitro con ID: {id_arbitro} y con nombre {nombre_arbitro}, ha dirigido en total: {partidos_dirigidos} partidos en el campeonato")




   
