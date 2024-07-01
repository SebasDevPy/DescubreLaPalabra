from Package_funciones.validaciones import *
from Package_clases import *
from Package_clases.clase_inicio import *
from Package_funciones.archivo_csv import *
from Package_funciones.archivo_json import *

def crear_jugador(id: int, nickname):

    diccionario_jugador = {
        "id" : id,
        "nickname" : nickname
    }
    return diccionario_jugador

def cargar_jugadores(lista_jugadores, contador_jugadores_id, nickname, puntuacion):
    try:
        
        contador_jugadores_id += 1
        
        
        jugador = {
            "id": contador_jugadores_id,
            "nickname": nickname,
            "puntuacion": puntuacion
        }
        
        
        lista_jugadores.append(jugador)
        return lista_jugadores, contador_jugadores_id
    
    except Exception as e:
        print(f"Error al cargar jugador: {e}")
        return lista_jugadores, contador_jugadores_id
    
def ingreso_datos_jugador(lista_jugadores, nickname):

    try:
        nickname_valido = validar_datos_jugador(nickname)

        if nickname_valido:
            nuevo_id = (len(lista_jugadores)+1)
            jugador = crear_jugador(nuevo_id, nickname)
            return jugador, True
        else:
            return None, False
    except Exception as e:
        print(f"Se ha producido un error: {e}")
        return None, False