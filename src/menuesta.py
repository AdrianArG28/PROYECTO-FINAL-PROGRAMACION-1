from Tablas import generar_tabla_puntos, tabla_de_goleadores, generar_estadisticas_equipo

def menu_estadisticas():
    while True:
        print("\n=== ESTADISTICAS ===")
        print("1. Ver tabla de posiciones")
        print("2. Ver tabla de goleadores")
        print("3. Ver rendimiento del equipo")
        print("4. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion (1-4): ")
        
        if opcion == "1":
            generar_tabla_puntos()

        elif opcion == "2":
            tabla_de_goleadores()

        elif opcion == "3":
            id_equipo = input("Digite el id del equipo: ")
            generar_estadisticas_equipo(id_equipo)
            
        elif opcion == "4":
            break