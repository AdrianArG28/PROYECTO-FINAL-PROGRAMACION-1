from Sanciones import registrar_sancion, actualizar_estado_sancion, generar_reporte_sanciones, es_fecha_valida, buscar_por_id

TIPO_SANCION_VALIDO = {"jugador", "equipo"}
def menu_sanciones():
    while True:
        print("\n=== SISTEMA DE SANCIONES ===")
        print("1. Registrar una sancion")
        print("2. Actualizar estado de sancion")
        print("3. Generar reporte de sanciones")
        print("4. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion (1-4): ")
        
        if opcion == "1":
            tipo = input("La sancion va para un jugador o para un equipo?: ")
            while tipo not in TIPO_SANCION_VALIDO:
                print(f"Error: El tipo '{tipo}' no es valido. Debe ser uno de: {TIPO_SANCION_VALIDO}")
                tipo = input("La sancion va para un jugador o para un equipo?: ")

            id_sancionado = input(f"Digite el ID del {tipo}: ")
            while buscar_por_id(id_sancionado) == False:
                print(f"Disculpe, puede digitar a otro {tipo} ya que {id_sancionado} no esta")
                id_sancionado = input(f"Digite el ID del {tipo}: ")

            motivo = input("Cual fue el motivo?: ")
            while motivo != "Amarillas acumuladas":
                print(f"Error: el motivo '{motivo}' no es un motivo valido")
                motivo = input("Intenta con 'Amarillas acumuladas': ")

            fecha_de_inicio = input("Dame la fecha del inicio de esta sancion (AAAA-MM-DD a las HH-MM): ")
            while not es_fecha_valida(fecha_de_inicio):
                fecha_de_inicio = input("Dame la fecha del inicio de esta sancion (AAAA-MM-DD a las HH-MM): ")

            duracion = int(input("De cuantos partidos sera la sancion?: "))
            while duracion <= 0 or duracion > 10:
                if duracion <= 0:
                    print("Error: la duracion de la sancion debe ser un numero positivo mayor a 1")
                else:
                    print("Error: la sancion no puede superar la cantidad de 10 partidos")
                duracion = int(input("De cuantos partidos sera la sancion?: "))

            estado = input("Digite el estado de la sancion (activa/cumplida): ")
            while estado not in ["activa", "cumplida"]:
                print("Error: la sancion solo puede ser (activa) o (cumplida)")
                estado = input("Digite el estado de la sancion (activa/cumplida): ")

            registrar_sancion(tipo, id_sancionado, motivo, fecha_de_inicio, duracion, estado)

        elif opcion == "2":
            id_sancion = input("Dame el ID del sancionado para marcarlo como cumplido: ")
            actualizar_estado_sancion(id_sancion)

        elif opcion == "3":
            tipo = input("La sancion que busca es de jugador o equipo?: ")
            while tipo not in TIPO_SANCION_VALIDO:
                print(f"Error: El tipo '{tipo}' no es valido. Debe ser uno de: {TIPO_SANCION_VALIDO}")
                tipo = input("La sancion que busca es de jugador o equipo?: ")
            generar_reporte_sanciones(tipo)

        elif opcion == "4":
            break

        else:
            print("Opcion no valida. Por favor, seleccione una opcion entre 1 y 4")