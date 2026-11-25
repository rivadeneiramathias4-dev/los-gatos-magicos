# game_logic.py
# Proyecto Integrador - Fase 3: Traducción de DF2 (Validación) y DF3 (Fin de la partida)
# Juego: Los Gatos Mágicos: Aventura de Fuego y Agua

print("=== PRUEBA DF2: VALIDACIÓN DE LA JUGADA ===")

# Estado de ejemplo para prueba unitaria de validación [RF-05]
turno = 1
fila_fuego = 2
columna_fuego = 1
fila_agua = 5
columna_agua = 5
fila_destino = 0
columna_destino = 0
casilla_destino = ""
movimiento_valido = 0

# Bucle de validación hasta ingresar una jugada válida [RF-05..RF-10]
while movimiento_valido != 1:
    entrada_dir = input(
        "Ingrese dirección (1: Arriba, 2: Abajo, 3: Izquierda, 4: Derecha): "
    )
    if entrada_dir.isdigit():
        direccion = int(entrada_dir)
    else:
        direccion = 0

    # Validación de formato (1..4) [RF-10]
    if direccion < 1 or direccion > 4:
        print("Dirección inválida. Intente nuevamente")
    else:
        # Calcular coordenada candidata según turno [RF-05]
        if turno == 1:
            fila_destino = fila_fuego
            columna_destino = columna_fuego
        else:
            fila_destino = fila_agua
            columna_destino = columna_agua

        if direccion == 1:
            fila_destino = fila_destino - 1
        elif direccion == 2:
            fila_destino = fila_destino + 1
        elif direccion == 3:
            columna_destino = columna_destino - 1
        elif direccion == 4:
            columna_destino = columna_destino + 1

        # Verificar límites del tablero 5x5 [RF-07]
        if (
            fila_destino < 1
            or fila_destino > 5
            or columna_destino < 1
            or columna_destino > 5
        ):
            print("Movimiento no permitido. Intente nuevamente")
        else:
            # Verificar colisión con el otro personaje [RF-09]
            if (
                turno == 1
                and fila_destino == fila_agua
                and columna_destino == columna_agua
            ) or (
                turno == 2
                and fila_destino == fila_fuego
                and columna_destino == columna_fuego
            ):
                print("Movimiento no permitido. Intente nuevamente")
            else:
                # Determinar tipo de terreno sin arreglos (variables escalares) [RF-08]
                if fila_destino == 3 and columna_destino == 3:
                    casilla_destino = "pared"
                elif fila_destino == 2 and columna_destino == 2:
                    casilla_destino = "agua"
                elif fila_destino == 4 and columna_destino == 4:
                    casilla_destino = "lava"
                elif fila_destino == 5 and columna_destino == 1:
                    casilla_destino = "salida_fuego"
                elif fila_destino == 1 and columna_destino == 5:
                    casilla_destino = "salida_agua"
                else:
                    casilla_destino = "libre"

                # Verificar pared y compatibilidad elemental [RF-08]
                if (
                    casilla_destino == "pared"
                    or (turno == 1 and casilla_destino == "agua")
                    or (turno == 2 and casilla_destino == "lava")
                ):
                    print("Movimiento no permitido. Intente nuevamente")
                else:
                    movimiento_valido = 1
                    print("Movimiento realizado correctamente")

print("\n=== PRUEBA DF3: FIN DE LA PARTIDA ===")

# Estado de ejemplo para prueba unitaria de finalización [RF-12, RF-13]
fila_fuego = 5
columna_fuego = 1
activo_fuego = 1
llego_fuego = 0
fila_agua = 1
columna_agua = 5
activo_agua = 1
llego_agua = 0

# Evaluar llegada del gato de fuego a su salida (5, 1) [RF-12, RF-13]
if fila_fuego == 5 and columna_fuego == 1 and llego_fuego == 0:
    llego_fuego = 1
    activo_fuego = 0
    if llego_agua == 0:
        print("¡El personaje ha llegado a su salida! La partida continúa")

# Evaluar llegada del gato de agua a su salida (1, 5) [RF-12, RF-13]
if fila_agua == 1 and columna_agua == 5 and llego_agua == 0:
    llego_agua = 1
    activo_agua = 0
    if llego_fuego == 0:
        print("¡El personaje ha llegado a su salida! La partida continúa")

# Evaluar victoria cooperativa [RF-12, RF-13]
if llego_fuego == 1 and llego_agua == 1:
    print("¡FELICIDADES! Ambos gatos han completado la aventura")
else:
    print("La partida continúa con el personaje activo restante")
