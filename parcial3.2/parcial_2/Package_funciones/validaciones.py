from Package_clases.clase_inicio import validar_nickname

def validar_caracteres(caracter):
    es_valido = True
    try:
        if not caracter:
            es_valido = False
        elif len(caracter) > 1:
            es_valido = False
        else:
            caracter = caracter.lower()
    except Exception as e:
        print(f"Error al validar el caracter: {e}")
        es_valido = False
    return es_valido

def validar_entrada_jugador(caracter):
    try:
        caracter_valido = validar_caracteres(caracter)
        return caracter_valido
    except Exception as e:
        print(f"Error al validar la entrada de letras: {e}")

def validar_datos_jugador(nickname):
    try:
        nickname_valido = validar_nickname(nickname)
        return nickname_valido
    except Exception as e:
        print(f"Error al validar los datos del jugador: {e}")