
import pygame
import re
from constantes_pantalla import *

def validar_nickname(nickname_completo):
    es_valido = True
    try:
        if not nickname_completo:
            es_valido = False
        elif len(nickname_completo) > 10:
            es_valido = False   
        elif not re.match("^[\\w\\W]*$", nickname_completo):
            es_valido = False
    except Exception as e:
        print(f"Error al validar el nickname_completo: {e}")
        es_valido = False
    return es_valido

def validar_espacioes(palabra:str)-> bool:
    valido_espacio = palabra.count(" ") # ceunto la veces que encuento espacios
    espacio = False
    if valido_espacio > 0:
        espacio = True
    return espacio

class Inicio:
    def __init__(self):
        pygame.init()

        # Crear pantalla y cargar imagen para el fondo e icono
        self.pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption("DESCUBRE PALABRAS")
        self.pos_fondo_x = 0
        self.fondo_p_diseño = pygame.image.load("parcial_2\\imagenes\\fondo_inicio.png").convert()
        self.fondo_p_diseño = pygame.transform.scale(self.fondo_p_diseño, (ANCHO_VENTANA, ALTO_VENTANA))
        self.icono = pygame.image.load('parcial_2\\imagenes\\logo.png')
        pygame.display.set_icon(self.icono)

        # Cargar imágenes para el título 
        self.letras_inicios = pygame.image.load('parcial_2\\imagenes\\titulo_inicio.png')
        self.letras_inicios = pygame.transform.scale(self.letras_inicios, (470, 200))
        self.letras_inicios_rect = self.letras_inicios.get_rect(topleft=(360, 130))

        # Cargar imágenes para el fondo del input y botón 
        self.rectangulo = pygame.image.load('parcial_2\\imagenes\\tarjeta_fondo_input .png')
        self.rectangulo = pygame.transform.scale(self.rectangulo, (470, 200))
        self.rectangulo_rect = self.rectangulo.get_rect(topleft=(360, 330))

        # Cargar imagen para botón (STAR)
        self.boton_star = pygame.image.load('parcial_2\\imagenes\\boton_star.png')
        self.boton_star = pygame.transform.scale(self.boton_star, (135, 35))
        self.boton_star_rect = self.boton_star.get_rect(topleft=(640, 374))

        # Cargar imagen para el input 
        self.input = pygame.image.load('parcial_2\\imagenes\\input.png')
        self.input = pygame.transform.scale(self.input, (220, 40))
        self.input_rect = self.input.get_rect(topleft=(420, 365))

        self.nickname = ""
        self.input_activo = True
        self.mensaje_error = ""
        self.mensaje_error = "Nickname no válido. Verifica las reglas."

        self.running = True

        # Cargar fuentes para el texto
        self.fuente = pygame.font.Font(None, 28)
        self.fuente_pequeña = pygame.font.Font(None, 30)

    def bucle_pantalla_inicio(self):
        valido_espacios=""
        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False
                if evento.type == pygame.KEYDOWN :
                    if self.input_activo:
                        if evento.key == pygame.K_RETURN:
                            if validar_nickname(self.nickname):
                                self.input_activo = False
                            
                        elif evento.key == pygame.K_BACKSPACE:
                            self.nickname = self.nickname[:-1]
                        else:
                            self.nickname += evento.unicode
                            valido_espacios =  validar_espacioes(self.nickname)
                        if texto_ingreso.get_width() > self.input_rect.width-20:
                            self.nickname = self.nickname[:-1]
                            texto_ingreso = self.fuente.render(self.nickname, True, COLOR_BLANCO)

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    posicion_click = evento.pos
                    print(posicion_click)
                    #se verifica la colicion del click del mouse con la ubicacion del boton star
                    if self.boton_star_rect.collidepoint(posicion_click) and len(self.nickname) > 3 :
                        # Acciona el boton star
                        pantalla = "juego"
                        self.running = False
                        return pantalla


            self.pantalla.fill(COLOR_NEGRO)
            posicion_relativa_x = self.pos_fondo_x % self.fondo_p_diseño.get_rect().width
            print(posicion_relativa_x)
            self.pantalla.blit(self.fondo_p_diseño, (posicion_relativa_x - self.fondo_p_diseño.get_rect().width, 0))
            if posicion_relativa_x < ANCHO_VENTANA:
                self.pantalla.blit(self.fondo_p_diseño, (posicion_relativa_x, 0))

            self.pos_fondo_x -= 1

            self.pantalla.blit(self.rectangulo, self.rectangulo_rect)
            self.pantalla.blit(self.letras_inicios, self.letras_inicios_rect)
            self.pantalla.blit(self.boton_star, self.boton_star_rect)
            self.pantalla.blit(self.input, self.input_rect)
            
            #referencia
        
            if valido_espacios  :
                texto_error = self.fuente_pequeña.render(self.mensaje_error, True, COLOR_BLANCO)
                self.pantalla.blit(texto_error, (373, 470))
                self.nickname =""
            if self.input_activo :
                texto_ingreso = self.fuente.render(self.nickname, True, COLOR_BLANCO)
                self.pantalla.blit(texto_ingreso, (430, 382))
                

            pygame.display.flip()

        pygame.quit()