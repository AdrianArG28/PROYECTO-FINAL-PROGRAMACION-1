from Equipos import registro_equipo, buscar_equipo, actualizar_estadisticas, es_ciudad_valida, nombre_valido

def menu_equipos():
    while True:
        print("\n=== GESTION DE EQUIPOS ===")
        print("1. Registrar nuevo equipo")
        print("2. Buscar equipo")
        print("3. Actualizar estadisticas de equipo")
        print("4. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion (1-4): ")
        
        if opcion == "1":
            nombre = input("Nombre del equipo: ")
            while nombre_valido(nombre) == False:
                print(f"Error: no pueden existir equipos con el mismo nombre y {nombre} ya esta registrado")
                nombre = input("Nombre del equipo: ")
            ciudad = input("Ciudad del equipo: ")
            while es_ciudad_valida(ciudad) == False:
                print(f"Lo siento pero {ciudad} no pertenece a ninguna ciudad de colombia. Por favor escriba una ciudad valida de Colombia")
                ciudad = input("Ciudad del equipo: ")
            dt = input("Director tecnico: ")
            registro_equipo(nombre, ciudad, dt)

        elif opcion == "2":
            while True:
                #esto se va a ejecutar asta que criterio sea escrito correctamente
                criterio = input("Que busca? (ID, nombre, ciudad o dt): ")
                if criterio in ["ID", "nombre", "ciudad", "dt"]:
                    #si lo escribe bien break rompera el while True
                    break  
                else:
                    #si no lo escribe bien else ejecutara este mensaje. Pero mira que no rompe el while true
                    #lo que quiere decir que lo seguira ejecutando
                    print(f"Perdon pero {criterio}, no es valido, intente nuevamente")
            while True:
                print("Si no conoce su valor, escriba: salir")  
                valor = input(f"Ingrese {criterio} del equipo: ") 
                if valor.lower() == 'salir':
                    break        
                if buscar_equipo(criterio, valor):
                    
                    break  
                else:
                    print("No encontre al equipo, intente de nuevo")

        elif opcion == "3":
            while True:
                id_equipo = input("ID del equipo: ")
                if actualizar_estadisticas(id_equipo):
                    break
                else:
                    print("Intenta otra vez")
                

        elif opcion == "4":
            break