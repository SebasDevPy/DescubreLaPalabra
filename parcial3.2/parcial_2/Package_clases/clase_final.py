import pygame
from constantes_pantalla import *
from Package_funciones.archivo_json import leer_puntuaciones_json

class PantallaFinal:
    def __init__(self):
        pygame.init()

        # Crear pantalla y cargar imagen para el fondo e icono
        self.pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption("DESCUBRE PALABRAS")
        self.fondo_p_diseño = pygame.image.load("parcial_2\\imagenes\\fondo_pantalla_continuar.png").convert()
        self.fondo_p_diseño = pygame.transform.scale(self.fondo_p_diseño, (ANCHO_VENTANA, ALTO_VENTANA))
        self.icono = pygame.image.load('parcial_2\\imagenes\\logo_pantalla_continuar.png')
        pygame.display.set_icon(self.icono)

        self.logo = pygame.image.load('parcial_2/imagenes/logo.png')
        self.logo = pygame.transform.scale(self.logo, (50, 50))
        self.logo_rect = self.logo.get_rect(topleft=(10, 10))

        # Cargar imágenes para figura ovalo
        self.ovalo = pygame.image.load('parcial_2\\imagenes\\ovalo.png')
        self.ovalo = pygame.transform.scale(self.ovalo, (450, 160))
        self.letras_ovalo_rect = self.ovalo.get_rect(topleft=(360, 40))

        # Cargar imagen palabra score
        self.palabra_score = pygame.image.load('parcial_2\\imagenes\\palabra_score.png')
        self.palabra_score = pygame.transform.scale(self.palabra_score, (300, 85))
        self.palabra_score_rect = self.palabra_score.get_rect(topleft=(440, 80))

        # Cargar imagen para el boton close
        self.boton_close = pygame.image.load('parcial_2\\imagenes\\boton_close.png')
        self.boton_close = pygame.transform.scale(self.boton_close, (180, 50))
        self.boton_close_rect = self.boton_close.get_rect(topleft=(500, 510))

        # Cargar imagen para el texto de puntuaciones
        self.texto_puntuaciones = pygame.image.load('parcial_2\\imagenes\\texto_pantalla_continuar.png')
        self.texto_puntuaciones = pygame.transform.scale(self.texto_puntuaciones, (330, 12))
        self.texto_puntuaciones_rect = self.texto_puntuaciones.get_rect(topleft=(430, 485))

        # Cargar fuente para el texto
        self.fuente = pygame.font.Font(None, 48)

        # Lista para almacenar las puntuaciones
        self.lista_puntuaciones = []

        self.running = True

    def obtener_top_puntuaciones(self):
        puntuaciones = leer_puntuaciones_json()
        # Ordenar puntuaciones de mayor a menor
        puntuaciones_ordenadas = sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)
        # Tomar las primeras 5 puntuaciones (o menos si hay menos de 5 jugadores)
        self.lista_puntuaciones = puntuaciones_ordenadas[:5]

    def bucle_pantalla_final(self):
        self.obtener_top_puntuaciones()

        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    posicion_click = evento.pos
                    if self.boton_close_rect.collidepoint(posicion_click):
                        self.running = False

            self.pantalla.fill(COLOR_NEGRO)
            self.pantalla.blit(self.fondo_p_diseño, (0, 0))
            self.pantalla.blit(self.ovalo, self.letras_ovalo_rect)
            self.pantalla.blit(self.boton_close, self.boton_close_rect)
            self.pantalla.blit(self.palabra_score, self.palabra_score_rect)
            self.pantalla.blit(self.texto_puntuaciones, self.texto_puntuaciones_rect)
            self.pantalla.blit(self.logo, self.logo_rect)
            # Mostrar las puntuaciones
            y_pos = 250
            for jugador, puntuacion in self.lista_puntuaciones:
                texto = self.fuente.render(f"{jugador}: {puntuacion}", True, COLOR_NARANJA)
                texto_rect = texto.get_rect(center=(ANCHO_VENTANA // 2, y_pos))
                self.pantalla.blit(texto, texto_rect)
                y_pos += 50  # Espaciado entre cada línea de puntuación

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    pantalla_final = PantallaFinal()
    pantalla_final.bucle_pantalla_final()
