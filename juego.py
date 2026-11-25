# juego.py
# Proyecto Integrador - Fase 3: Código inicial (Menú principal - DF1)
# Juego: Los Gatos Mágicos: Aventura de Fuego y Agua

# Inicialización de menú [RF-04]
opcion_menu = 0

# Bucle principal del menú: se repite hasta elegir Salir (2) [RF-04]
while opcion_menu != 2:
    entrada = input("Menú: 1. Iniciar partida | 2. Salir: ")
    if entrada.isdigit():
        opcion_menu = int(entrada)
    else:
        opcion_menu = 0

    # Validación de entrada del menú [RF-04]
    if opcion_menu != 1 and opcion_menu != 2:
        print("Opción inválida. Intente nuevamente")
    elif opcion_menu == 1:
        # En la Fase 3, la opción Jugar muestra un mensaje de inicio
        print("Iniciando partida de Los Gatos Mágicos: Aventura de Fuego y Agua...")

print("Gracias por jugar. ¡Hasta pronto!")
