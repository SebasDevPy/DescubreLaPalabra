import pygame
from Package_clases.clase_juego import *
from Package_clases.clase_inicio import *
from Package_clases.clase_continuar import *
from Package_clases.clase_final import *
from constantes_pantalla import *

pygame.init()
# Lista de palabras
#
palabras_y_validas = [
    {
        "palabra_base": "cadena",
        "palabras_validas": ["cana", "cadena", "cena", "daca", "nada"]
    },
    {
        "palabra_base": "ropero",
        "palabras_validas": ["pero", "perro", "oreo", "por", "pro", "reo", "ropero"]
    },
    {
        "palabra_base": "ciudad",
        "palabras_validas": ["cuida", "ciudad", "dicua", "cid", "ida", "dia"]
    },
    {
        "palabra_base": "fresca",
        "palabras_validas": ["fresca", "fresa", "cafre", "cera", "ser", "cesar", "arce","res"]
    },
    {
        "palabra_base": "rastro",
        "palabras_validas": ["rastro", "traso", "tora", "rota", "rato", "astro", "ras"]
    },
    {
        "palabra_base": "riesgo",
        "palabras_validas": ["ser", "regio", "ries", "riesgo", "rgo", "giro", "giros", "rie","sergio"]
    },
    {
        "palabra_base": "cartel",
        "palabras_validas": ["cartel", "recta", "tela", "calte"]
    },
    {
        "palabra_base": "fresas",
        "palabras_validas": ["fresas", "seraf", "safer", "sear", "fresa","ser","res"]
    },
    {
        "palabra_base": "animal",
        "palabras_validas": ["anima", "mina", "lamina", "animal","mal","mil","lima"]
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
            pantalla_actual = "fin"
            pygame.quit()
            break

    pygame.quit()
    
juego_palabras(palabras_y_validas)


