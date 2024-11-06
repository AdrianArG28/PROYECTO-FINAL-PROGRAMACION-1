#aqui mportamos los menus de cada cosa desde los archivos menus creados
from menueqp import menu_equipos
from menujug import menu_jugadores
from menupart import menu_partidos
from menuesta import menu_estadisticas
from menuarbi import menu_arbitros
from menusanc import menu_sanciones


def menu_principal():
    while True:
        print("\n=== SISTEMA DE GESTION DE TORNEO DE FUTBOL ===")
        print("1. Gestion de equipos")
        print("2. Gestion de jugadores")
        print("3. Gestion de partidos")
        print("4. Ver estadisticas")
        print("5. Gestor de arbitros")
        print("6. Sistema de sanciones")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opcion (1-7): ")
        
        if opcion == "1":
            menu_equipos() 
        elif opcion == "2":
            menu_jugadores() 
        elif opcion == "3":
            menu_partidos() 
        elif opcion == "4":
            menu_estadisticas() 
        elif opcion =="5":
            menu_arbitros()
        elif opcion == "6":
            menu_sanciones()
        elif opcion == "7":
            print("\nChao bb.")
            break
        else:
            print("\nError: SOLO elige una de las opciones(1-7).")


if __name__ == "__main__":
    menu_principal()