from Partidos import registrar_partido, actualizar_resultado, registrar_evento, es_fecha_valida, verificar_fecha
TIPOS_EVENTOS_VALIDOS = {"gol", "tarjeta amarilla", "tarjeta roja", "sustitucion"}

def menu_partidos():
    while True:
        print("\n=== GESTION DE PARTIDOS ===")
        print("1. Registrar nuevo partido")
        print("2. Actualizar resultado")
        print("3. Registrar evento")
        print("4. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion (1-4): ")
        
        if opcion == "1":
            fecha = input("Ingrese la fecha del partido(ej:2024-02-23) y la hora en formato militar (ej:13:00): ")

            while es_fecha_valida(fecha) == False:
                fecha = input("Ingrese la fecha del partido(ej:2024-02-23) y la hora en formato militar (ej:13:00): ")

            while verificar_fecha(fecha) == False:
                fecha = input("Ingrese la fecha del partido(ej:2024-02-23) y la hora en formato militar (ej:13:00): ")

            equipo_local = input("Ingrese el ID del equipo local: ")
            
            equipo_visitante = input("Ingrese el ID del equipo visitante: ")

            while equipo_visitante == equipo_local:
                print("Error: El equipo visitante no puede ser igual al equipo local")
                print(f"Como se van a enfretar el {equipo_local} contra {equipo_visitante}?")
                equipo_visitante = input("Ingrese el ID del equipo visitante: ")
            registrar_partido(fecha, equipo_local, equipo_visitante)

        elif opcion == "2":
            id_partido = input("Digite el ID del partido: ")

            goles_local = int(input("Cuantos goles metio el equipo local?: "))

            while goles_local > 10:
                print("Error: la cantidad maxima de goles a ingresar en un partido son 10")
                goles_local = int(input("Cuantos goles metio el equipo local?: "))

            while goles_local < 0:
                print("Error: la cantidad minima de goles a ingresar en un partido son 0")
                goles_local = int(input("Cuantos goles metio el equipo local?: "))

            goles_visitante = int(input("Cuantos goles metio el equipo visitante?: "))

            while goles_visitante > 10:
                print("Error: la cantidad maxima de goles a ingresar en un partido son 10")
                goles_visitante = int(input("Cuantos goles metio el equipo visitante?: "))

            while goles_visitante < 0:
                print("Error: la cantidad minima de goles a ingresar en un partido son 0")
                goles_visitante = int(input("Cuantos goles metio el equipo visitante?: "))

            actualizar_resultado(id_partido, goles_local, goles_visitante)

        elif opcion == "3":
            Id_partido = input("Cual es el ID del partido?: ")

            Minuto = int(input("En que minuto del partido paso?: "))

            while Minuto > 100:
                print("No existen mas de 100 minutos en un partido normal")
                Minuto = int(input("En que minuto del partido paso?: "))

            Tipo = input("Tipo de evento (gol, tarjeta amarilla, tarjeta roja, sustitucion): ")

            while Tipo not in TIPOS_EVENTOS_VALIDOS:
                print(f"\n{Tipo} no es un evento valido. Intenta con uno de estos: {TIPOS_EVENTOS_VALIDOS}")
                Tipo = input("\nTipo de evento (gol, tarjeta amarilla, tarjeta roja, sustitucion): ")

            if Tipo == "gol":
                Jugador = input("ID del jugador que metio el gol (ej: jug122): ")
            elif Tipo == "tarjeta amarilla":
                Jugador = input("ID del jugador con tarjeta amarilla (ej: jug122): ")
            elif Tipo == "tarjeta roja":
                Jugador = input("ID del jugador con tarjeta roja (ej: jug122): ")
            elif Tipo == "sustitucion":
                Jugador = input("ID del jugador sustituido (ej: jug122): ")
                
            registrar_evento(Id_partido, Minuto, Tipo, Jugador)
            
        elif opcion == "4":
            break