from Jugadores import registro_jugador, buscar_jugador, actualizar_estadisticas_jugador, Verificador_de_registro_jugador

def menu_jugadores():
    while True:
        print("\n=== GESTION DE JUGADORES ===")
        print("1. Registrar nuevo jugador")
        print("2. Buscar jugador")
        print("3. Actualizar estadisticas de jugador")
        print("4. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion (1-4): ")

        if opcion == "1":
            nombre = input("Como se llama el nuevo jugador?: ")

            numero_camisa = int(input("Que numero de camisa le quieres poner al nuevo jugador?: "))

            id_equipo = input("Dame el ID del equipo donde meteremos a el jugador (ej: eqp001): ")

            posicion = input("Posicion (ej: Delantero, Mediocampista, Portero o Defensa): ")

            while Verificador_de_registro_jugador(numero_camisa, id_equipo, posicion) == False:
                numero_camisa = int(input("Numero de camisa: "))
                id_equipo = input("Dame el ID del equipo donde meteremos al jugador (ej: eqp001): ")
                posicion = input("Posicion (ej: Delantero, Mediocampista, Portero o Defensa): ")

            registro_jugador(nombre, numero_camisa, posicion, id_equipo)

        elif opcion == "2":
            while True:
                criterio = input("Criterio de busqueda (ID, nombre, numero de camisa, posicion): ")        
                if criterio in ["ID", "nombre", "numero de camisa", "posicion"]:  
                    break  
                else:
                    print("Criterio invalido. Intente de nuevo.")
            
            while True:
                print("Si no conoce su valor, escriba: salir")  
                valor = input(f"Ingrese el valor para {criterio}: ")  
                if valor.lower() == 'salir':
                    break  
                

                if criterio == "numero de camisa":  
                    if valor.isdigit():  
                        valor = int(valor)  
                        buscar_jugador(criterio, valor)  
                        break  
                    else:
                        print("El valor para 'numero de camisa' debe ser un numero entero.")
                        continue  

                buscar_jugador(criterio, valor)
                break 
  

        elif opcion == "3":
            id_jugador = input("ID del jugador: ")
            actualizar_estadisticas_jugador(id_jugador)
            
        elif opcion == "4":
            break