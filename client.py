# client.py
# Proyecto Integrador - Fase 3: Marcador de arquitectura cliente-servidor (Jugador 2 - Cliente)
#
# Qué hará este archivo en la Fase 4:
# - Actuará como nodo cliente remoto conectado al servidor por socket TCP (puerto 5000).
# - Controlará al Jugador 2 (gato de agua, inicio (5, 5) -> salida (1, 5)).
# - Enviará la solicitud de conexión (CONECTAR|J2), validará localmente el formato de entrada
#   (1: Arriba, 2: Abajo, 3: Izquierda, 4: Derecha) cuando sea su turno, enviará la petición
#   de movimiento (JUGADA|2|<direccion>) y mostrará en pantalla el tablero y mensajes recibidos.
