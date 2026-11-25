# server.py
# Proyecto Integrador - Fase 3: Marcador de arquitectura cliente-servidor (Jugador 1 - Servidor)
#
# Qué hará este archivo en la Fase 4:
# - Actuará como nodo servidor autoritativo en red LAN mediante sockets TCP (puerto 5000).
# - Controlará al Jugador 1 (gato de fuego, inicio (1, 1) -> salida (5, 1)).
# - Aceptará la conexión del cliente (Jugador 2), inicializará el tablero oficial 5x5,
#   recibirá las jugadas locales y remotas (trama JUGADA|2|<direccion>), ejecutará toda
#   la validación de reglas (DF2), actualizará coordenadas, alternará turnos, evaluará
#   la victoria cooperativa (DF3) y difundirá el estado actualizado (ESTADO|... / FIN|...).
