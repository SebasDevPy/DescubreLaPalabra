from Package_clases.clase_juego import *
from Package_clases.clase_inicio import *
from Package_clases.clase_continuar import *
from Package_clases.clase_final import *
from constantes_pantalla import *

# Lista de palabras
#
palabras_y_validas = [
    {
        "palabra_base": "CADENA",
        "palabras_validas": ["CANA", "CADENA","DECANA" "CENA", "DACA", "NADA", "CADA", "DANA"]
    },
    {
        "palabra_base": "ROPERO",
        "palabras_validas": ["PERO", "PERRO", "OREO", "POR", "PRO", "REO", "ROPERO","RORO"]
    },
    {
        "palabra_base": "CIUDAD",
        "palabras_validas": ["CUIDA", "CIUDAD", "DICUA","DUDA", "CID", "IDA", "DIA","DAD"]
    },
    {
        "palabra_base": "FRESCA",
        "palabras_validas": ["FRESCA", "FRESA", "CAFRE", "CERA", "SER", "CESAR", "ARCE","CAFE"]
    },
    {
        "palabra_base": "RASTRO",
        "palabras_validas": ["RASTRO", "TRASO", "TORA", "ROTA", "RATO", "TARO", "ASTRO", "RAS"]
    },
    {
        "palabra_base": "RIESGO",
        "palabras_validas": ["SER", "REGIO", "RIES", "RIESGO", "EGO", "GIRO", "GIROS", "RIE"]
    },
    {
        "palabra_base": "CARTEL",
        "palabras_validas": ["CARTEL", "RECTA", "TELA", "TERCA", "ARTE","LATE","TELAR","ALE"]
    },
    {
        "palabra_base": "FRESAS",
        "palabras_validas": ["FRESAS", "FRASES", "ESAS", "REA", "FRESA", "FRASE", "ESA", "RES"]
    },
    {
        "palabra_base": "ANIMAL",
        "palabras_validas": ["ANIMA", "MINA", "LAMINA", "ANIMAL","ALMA", "ALA", "LIMA","MIL"]
    }
] 


def juego_palabras(lista: list)->None:
    inicio = Inicio()
    pantalla_actual = "inicio"

    while True:
        if pantalla_actual == "inicio":
            pantalla_actual = inicio.bucle_pantalla_inicio()
            if pantalla_actual == "juego":
                nickname = inicio.nickname
                juego = Juego(lista, nickname)

        elif pantalla_actual == "juego":
            juego.bucle_juego()
            if not juego.running:
                pantalla_actual = "final"

        elif pantalla_actual == "final":
            pantalla_final = PantallaFinal()
            pantalla_final.bucle_pantalla_final()
            pantalla_actual = "fin"#s
            break
juego_palabras(palabras_y_validas)


