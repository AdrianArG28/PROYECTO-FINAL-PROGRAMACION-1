from Arbitros import registrar_arbitro, asignar_arbitro, generar_reporte_arbitros, nombre_valido_arb
CATEGORIA_VALIDA = {"FIFA", "Nacional", "Regional"}
def menu_arbitros():
    
    while True:
        print("\n=== GESTOR DE ARBITROS ===")
        print("1. Registrar un nuevo arbitro")
        print("2. Asignar arbitro a partido")
        print("3. Ver el reporte de arbitros")
        print("4. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion (1-4): ")
        
        if opcion == "1":
            nombre = input("Digite el nombre del arbitro(gringo, opcional): ")

            while nombre_valido_arb(nombre) == False:
                print(f"Error: no pueden existir 2 arbitros con el mismo nombre y {nombre} ya esta registrado")
                print("Ese nombre ya lo tiene un arbitro, por favor cambielo")
                nombre = input("Digite el nombre del arbitro(gringo, opcional): ")

            experiencia = int(input("Digite los años de experiencia del arbitro: "))

            while experiencia > 30:
                print("Error: La experiencia maxima de los años de arbitraje son 30")
                experiencia = int(input("Digite los años de experiencia del arbitro: "))

            while experiencia < 0:
                print("Error: La experiencia no puede ser menor a 0")
                experiencia = int(input("Digite los años de experiencia del arbitro: "))

            categoria = input("Digite la categoria a la que pertenece el arbitro(ej: FIFA, Nacional o Regional): ")

            while categoria not in CATEGORIA_VALIDA:
                print(f"{categoria} no es una categoria valida. Intenta con uno de estos: {CATEGORIA_VALIDA}")
                categoria = input("Digite la categoria a la que pertenece el arbitro(ej: FIFA, Nacional o Regional): ")

            registrar_arbitro(nombre, experiencia, categoria)

        elif opcion == "2":
            while True:
                id_partido = input("Digite el ID del partido (ej: part002) o 'salir' para cancelar: ")
                if id_partido.lower() == 'salir':
                    break
                
                id_arbitro = input("Digite el ID del arbitro (ej: arb003): ")
                
                resultado = asignar_arbitro(id_partido, id_arbitro)
                #aqui se usa la condiciones explicadas en Arbitros se que aqui no estan especificadas directamente
                if resultado['partido_encontrado'] and resultado['arbitro_encontrado']:
                    print("Arbitro asignado exitosamente")
                    break 
                else:
                    #pero en la funcion de asignar_arbitro, retorna partido encontrado y arbitro encontrado como diccionarios
                    #por eso estan aqui y funcionan despues de mencionar a resultado = asignar_arbitro(id_partido, id_arbitro)
                    if not resultado['partido_encontrado']:
                        print("Error: El ID del partido no fue encontrado, intente de nuevo")
                    elif not resultado['arbitro_encontrado']:
                        print("Error: El ID del arbitro no fue encontrado, intente de nuevo")

        elif opcion == "3":
            #esto solo genera la tabla o lista de tops de arbitros con mas partidos dirigidos
            generar_reporte_arbitros()

        elif opcion == "4":
            break