'''
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
'''

def resultado_tenis(seq):
    zero = 'Love'
    empate = 'Deuce'
    player_1 = 0
    player_2 = 0
    ganador = ""

    for i in seq:
        if i == 'P1':
           player_1 += 15
        else:
            player_2 += 15
        # variables marcadores
        marcador_1 = zero if player_1 == 0 else player_1
        marcador_2 = zero if player_2 == 0 else player_2
        if marcador_1 == marcador_2:
           print(empate)
        else:    
            print(f"{marcador_1} - {marcador_2}")
    if player_1 > player_2:
        ganador = "P1"
    else:
        ganador = "P2"  
      
    return f"Ha ganado el {ganador}"

# probes

secuencia1 = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
proba1 = resultado_tenis(secuencia1)
print(proba1)
