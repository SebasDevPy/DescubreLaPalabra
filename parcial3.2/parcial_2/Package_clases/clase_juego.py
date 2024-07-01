import pygame
import time
import random
from constantes_pantalla import *
from Package_funciones.archivo_json import guardar_puntuaciones_json, leer_puntuaciones_json
from Package_funciones.archivo_csv import leer_nickname_desde_csv, guardar_jugadores_en_csv
from Package_funciones.carga_de_jugadores import *
from Package_clases.clase_continuar import Continuar


def generar_palabras_validas(palabra_base, lista_palabras):
    letras_base = sorted(palabra_base)
    palabras_validas = []

    for palabra in lista_palabras:
        if len(palabra) == len(palabra_base) and sorted(palabra) == letras_base:
            palabras_validas.append(palabra)

    return palabras_validas

class Juego:
    def __init__(self, palabras_y_validas, nickname, puntuacion_inicial = 0):
    
        pygame.init()
        self.nickname = nickname
        self.indice_palabra_actual = 0
        self.cambiar_palabra_actual(palabras_y_validas)
        self.entrada_jugador = ""
        self.puntos_jugador = 0
        self.tiempo_inicio = time.time()
        self.tiempo_limite = 25
        self.puntuacion = puntuacion_inicial
        self.en_juego = True
        self.palabras_acertadas = []
        self.dict_jugador = {}
        self.contador_nuevo = 0
        pygame.display.set_caption("DESCUBRE PALABRAS")
        self.fondo_p_diseño = pygame.image.load("parcial_2/imagenes/fondo.png")
        self.fondo_p_diseño = pygame.transform.scale(self.fondo_p_diseño, (ANCHO_VENTANA, ALTO_VENTANA))
        self.icono = pygame.image.load('parcial_2/imagenes/logo.png')
        pygame.display.set_icon(self.icono)
        
        self.tiempo_restante = self.tiempo_limite - (time.time() - self.tiempo_inicio)

        # Crear pantalla y cargar imagen para el fondo e icono
        self.pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption("DESCUBRE PALABRAS")
        self.fondo_p_diseño = pygame.image.load("parcial_2\\imagenes\\fondo.png")
        self.fondo_p_diseño = pygame.transform.scale(self.fondo_p_diseño, (ANCHO_VENTANA, ALTO_VENTANA))
        self.icono = pygame.image.load('parcial_2/imagenes/logo.png')
        pygame.display.set_icon(self.icono)

        # Cargar imagen para botones (burbujas)
        self.boton = pygame.image.load('parcial_2/imagenes/burbuja_fucsia.png')
        self.boton = pygame.transform.scale(self.boton, (151, 151))

        # Cargar imagen para simular huellas de los botones de las burbujas
        self.boton_huella = pygame.image.load('parcial_2/imagenes/Huella.png')
        self.boton_huella = pygame.transform.scale(self.boton_huella, (149, 149))

        # Cargar imagen para el botón borrar
        self.boton_borrar = pygame.image.load('parcial_2/imagenes/boton_clear.png')
        self.boton_borrar = pygame.transform.scale(self.boton_borrar, (150, 50))
        self.boton_borrar_rect = self.boton_borrar.get_rect(topleft=(900, 436))

        # Cargar imagen para el botón submit
        self.boton_submit = pygame.image.load('parcial_2/imagenes/boton_submit.png')
        self.boton_submit = pygame.transform.scale(self.boton_submit, (150, 50))
        self.boton_submit_rect = self.boton_submit.get_rect(topleft=(700, 436))

        # Cargar imagen para el botón shuffle
        self.boton_shuffle = pygame.image.load('parcial_2/imagenes/boton_shuffle.png')
        self.boton_shuffle = pygame.transform.scale(self.boton_shuffle, (150, 50))
        self.boton_shuffle_rect = self.boton_shuffle.get_rect(topleft=(350, 436))

        # Cargar imagen para la barra
        self.barra = pygame.image.load('parcial_2/imagenes/barra.png')
        self.barra = pygame.transform.scale(self.barra, (1190, 120))
        self.barra_rect = self.barra.get_rect(topleft=(5, 400))

        # Cargar imagen para el logo
        self.logo = pygame.image.load('parcial_2/imagenes/logo.png')
        self.logo = pygame.transform.scale(self.logo, (50, 50))
        self.logo_rect = self.logo.get_rect(topleft=(10, 10))

        # Cargar imagen para el puntaje
        self.score = pygame.image.load('parcial_2/imagenes/score.png')
        self.score = pygame.transform.scale(self.score, (90, 20))
        self.score_rect = self.score.get_rect(topleft=(80, 450))

        # Tamaño y tipo de fuente
        self.font_score = 50
        self.font_score = pygame.font.SysFont(None, self.font_score)  # type: ignore
        self.font_size = 110
        self.font = pygame.font.SysFont(None, self.font_size) # type: ignore

        # Posiciones iniciales y posiciones de destinos de letras y botones (burbujas)
        self.posicion_inicial_letras = [(162, 100), (325, 100), (488, 100), (660, 100), (815, 100), (980, 100)]
        self.posicion_destino_letras = [(162, 265), (325, 265), (488, 265), (660, 265), (815, 265), (980, 265)]
        self.posicion_inicial_botones = [(115, 60), (280, 60), (445, 60), (610, 60), (775, 60), (935, 60)]
        self.posicion_destino_botones = [(115, 225), (280, 225), (445, 225), (610, 225), (775, 225), (935, 225)]

        # Estados de los botones
        self.estado_botones = [False] * len(self.posicion_inicial_botones)
        self.posiciones_ocupadas = [None] * len(self.posicion_inicial_botones)

        self.bandera = True
        self.running = True

        # Variable para almacenar el texto desordenado y las palabras asociadas
        self.texto_desordenado = None

        # Lista para guardar las letras en las posiciones de destino
        self.letras_destino = [None] * len(self.posicion_destino_botones)
        self.palabras_y_validas = palabras_y_validas

        # Variables para el temporizador
        self.fuente_tiempo = pygame.font.SysFont("consolas", 50)
        self.palabra_x_=20
        self.palabra_y_=560
        self.set_palabras = set()        #
        self.continuar = Continuar(self,self.pantalla)

    def cambiar_palabra_actual(self, palabras_y_validas):
        palabras_y_validas_aleatoria = random.choice(palabras_y_validas)
        self.palabra_base = palabras_y_validas_aleatoria["palabra_base"]
        self.palabras_validas = palabras_y_validas_aleatoria["palabras_validas"]
        self.letras_desordenadas = list(self.palabra_base)
        random.shuffle(self.letras_desordenadas)#DESORDENAR
    
    def ingresar_palabra(self):
        palabra_formada = "".join([letra for letra in self.letras_destino if letra is not None])
        
        # Verificar si la palabra ya ha sido acertada antes
        if palabra_formada in self.palabras_acertadas:
            # Si ya ha sido acertada, no hacer nada
            return
        
        if palabra_formada in self.palabras_validas:
            self.incrementar_puntuacion(palabra_formada)
            self.palabras_acertadas.append(palabra_formada)
        
        
    
    def incrementar_puntuacion(self, palabra):
        self.puntos_jugador += len(palabra)
        self.palabras_acertadas.append(palabra)


    def mostrar_puntuacion(self):
        texto_puntuacion = self.font_score.render(f"{self.puntos_jugador}", True, COLOR_NARANJA) # type: ignore
        #self.pantalla.blit(self.score,(50,443)) 
        self.pantalla.blit(texto_puntuacion, (180,445))
    
    def mostrar_resultado_final(self):
        self.pantalla.fill(COLOR_NEGRO)
        self.fondo_p_diseño = pygame.image.load("parcial_2\\imagenes\\fondo_pantalla_continuar.png").convert()
        self.fondo_p_diseño = pygame.transform.scale(self.fondo_p_diseño, (ANCHO_VENTANA, ALTO_VENTANA))
        self.icono = pygame.image.load('parcial_2\\imagenes\\logo_pantalla_continuar.png')
        pygame.display.set_icon(self.icono)
        self.logo = pygame.image.load('parcial_2/imagenes/logo.png')
        self.logo = pygame.transform.scale(self.logo, (50, 50))
        self.logo_rect = self.logo.get_rect(topleft=(10, 10))
        fuente = pygame.font.SysFont("consolas", 50)
        texto_resultado = f"Juego terminado. Puntuación final: {self.puntos_jugador}"
        superficie_texto = fuente.render(texto_resultado, True, (255, 255, 255))
        rect_texto = superficie_texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
        self.pantalla.blit(self.fondo_p_diseño, (0, 0))
        self.pantalla.blit(superficie_texto, rect_texto)
        self.pantalla.blit(self.logo, self.logo_rect)
        pygame.display.flip()
        time.sleep(5)  # Mantener la pantalla final por 5 segundos antes de cerrar el juego
        self.running = False
    
    def tiempo_agotado(self):
        return self.tiempo_restante <= 0
    
    def actualizar_tiempo(self):
        # Calcular el tiempo transcurrido desde el inicio del juego
        tiempo_transcurrido = time.time() - self.tiempo_inicio

        # Calcular el tiempo restante
        self.tiempo_restante = self.tiempo_limite - tiempo_transcurrido

        # Asegurarse de que el tiempo restante no sea negativo
        if self.tiempo_restante < 0:
            self.tiempo_restante = 0

    
        # Verificar si el tiempo se ha agotado completamente
        if self.tiempo_restante == 0 and self.contador_nuevo < 3:
            self.contador_nuevo +=1 
            self.continuar.mostrar_popup_continuar()

    
    def nueva_partida(self):
        # No reiniciar la puntuación aquí, solo reiniciar otras variables
        self.tiempo_inicio = time.time()
        self.tiempo_limite = 25
        self.en_juego = True
        self.entrada_jugador = ""
        self.cambiar_palabra_actual(self.palabras_y_validas)
        self.palabras_acertadas = []
        self.estado_botones = [False] * len(self.posicion_inicial_botones)
        self.posiciones_ocupadas = [None] * len(self.posicion_inicial_botones)
        self.letras_destino = [None] * len(self.posicion_destino_botones)
        self.tiempo_restante = self.tiempo_limite - (time.time() - self.tiempo_inicio)
        
    def bucle_juego(self):
        palabras=""

     
        contador_partidas_jugadas = 0
        while self.running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    posicion_click = evento.pos
                    print(posicion_click)
                    if self.boton_borrar_rect.collidepoint(posicion_click):
                        # Reiniciar todos los estados y posiciones
                        self.estado_botones = [False] * len(self.posicion_inicial_botones)
                        self.posiciones_ocupadas = [None] * len(self.posicion_inicial_botones)
                        self.letras_destino = [None] * len(self.posicion_destino_botones)
                        self.entrada_jugador = ""

                    elif self.boton_submit_rect.collidepoint(posicion_click):
                        # Evalua la palabra formada y reinicia todos los estados y posiciones
                        self.ingresar_palabra()
                        self.estado_botones = [False] * len(self.posicion_inicial_botones)
                        self.posiciones_ocupadas = [None] * len(self.posicion_inicial_botones)
                        self.letras_destino = [None] * len(self.posicion_destino_botones)

                    elif self.boton_shuffle_rect.collidepoint(posicion_click):
                        # Genera una nueva palabra desordenada y reinicia todos los estados y posiciones
                        self.bandera = True
                        self.cambiar_palabra_actual(self.palabras_y_validas)
                        self.estado_botones = [False] * len(self.posicion_inicial_botones)
                        self.posiciones_ocupadas = [None] * len(self.posicion_inicial_botones)
                        self.letras_destino = [None] * len(self.posicion_destino_botones)
                    else:
                        for i, (pos_x, pos_y) in enumerate(self.posicion_inicial_botones):
                            boton_rect = pygame.Rect(pos_x, pos_y, 150, 150)
                            if boton_rect.collidepoint(posicion_click):
                                if self.estado_botones[i]:
                                    # Volver a la posición inicial
                                    self.estado_botones[i] = False
                                    indice = self.posiciones_ocupadas.index(i) # type: ignore
                                    self.posiciones_ocupadas[indice] = None
                                    self.letras_destino[indice] = None
                                else:
                                    # Mover a la primera posición destino disponible
                                    for j in range(len(self.posiciones_ocupadas)):
                                        if self.posiciones_ocupadas[j] is None:
                                            self.posiciones_ocupadas[j] = i # type: ignore
                                            self.estado_botones[i] = True
                                            self.letras_destino[j] = self.letras_desordenadas[i]
                                            break
                                break
            #Modificar para que ingrese a la pregunta si desea seguir jugando 
            self.actualizar_tiempo()

            if self.tiempo_agotado():
                self.tiempo_restante = 0
                self.texto_tiempo = self.fuente_tiempo.render(f"{int(self.tiempo_restante)}", False, COLOR_ROJO)

                if contador_partidas_jugadas < 3:
                    continuar = self.continuar.mostrar_popup_continuar()
                    if continuar:
                        self.nueva_partida()
                        contador_partidas_jugadas += 1
                    else:
                        self.running = False
                        self.mostrar_resultado_final()
                else:
                    self.mostrar_resultado_final()
                    self.running = False
                                

            if len(self.palabras_validas) == 0:
                # Cambiar a la siguiente palabra
                self.cambiar_palabra_actual(self.palabras_y_validas)
                # Resetear estados y posiciones para la nueva palabra
                self.estado_botones = [False] * len(self.posicion_inicial_botones)
                self.posiciones_ocupadas = [None] * len(self.posicion_inicial_botones)
                self.letras_destino = [None] * len(self.posicion_destino_botones)
            
            self.pantalla.fill((0, 0, 0))
            self.pantalla.blit(self.fondo_p_diseño, (0, 0))

            for i in range(len(self.posicion_inicial_botones)):
                if self.estado_botones[i]:
                    indice = self.posiciones_ocupadas.index(i) # type: ignore
                    nueva_pos = self.posicion_destino_botones[indice]
                else:
                    nueva_pos = self.posicion_inicial_botones[i]

                self.pantalla.blit(self.boton_huella, self.posicion_inicial_botones[i])
                self.pantalla.blit(self.boton_huella, self.posicion_destino_botones[i])
                self.pantalla.blit(self.boton, nueva_pos)

            for i, letra in enumerate(self.letras_desordenadas):
                if i < len(self.posicion_destino_letras):
                    superficie_letra = self.font.render(letra, True, (255, 0, 0))
                    if self.estado_botones[i]:
                        posicion = self.posiciones_ocupadas.index(i) # type: ignore
                        nueva_pos_letras = self.posicion_destino_letras[posicion]
                    else:
                        nueva_pos_letras = self.posicion_inicial_letras[i]
                    self.pantalla.blit(superficie_letra, nueva_pos_letras)

            
            self.tiempo_restante = self.tiempo_limite - (time.time() - self.tiempo_inicio)
            self.texto_tiempo = self.fuente_tiempo.render(f"{int(self.tiempo_restante)}", False, COLOR_ROJO)

            self.palabra_x_ = 30
            self.palabra_y_=500
            fuente_palabra =  pygame.font.SysFont("arial", 30)


            for palabra in self.palabras_acertadas:
            
                self.set_palabras.add(palabra)  # type: ignore
            for palabra in self.set_palabras:
            
                palabras = fuente_palabra.render(f"{palabra}", False, COLOR_NARANJA)

                self.pantalla.blit(palabras, (self.palabra_x_,self.palabra_y_))

                self.palabra_x_+= 110
                if self.palabra_x_ + palabras.get_width() > self.pantalla.get_width():
                    self.palabra_x_ = 30
                    self.palabra_y_ += 60
            
            
            
                
                


            self.pantalla.blit(self.barra, self.barra_rect)
            self.pantalla.blit(self.logo, self.logo_rect)
            self.pantalla.blit(self.boton_borrar, self.boton_borrar_rect)
            self.pantalla.blit(self.boton_submit, self.boton_submit_rect)
            self.pantalla.blit(self.boton_shuffle, self.boton_shuffle_rect)
            self.pantalla.blit(self.score, self.score_rect)
            self.pantalla.blit(self.texto_tiempo, (575, 425))
            self.mostrar_puntuacion()
            pygame.display.flip()

        puntuaciones = leer_puntuaciones_json()
        puntuaciones[self.nickname] = self.puntos_jugador
        guardar_puntuaciones_json(puntuaciones)

        lista_jugadores, contador_jugadores_id = leer_nickname_desde_csv()
        if self.nickname not in lista_jugadores:
            lista_jugadores, contador_jugadores_id = cargar_jugadores(
                lista_jugadores, contador_jugadores_id, self.nickname, self.puntos_jugador)
            guardar_jugadores_en_csv(lista_jugadores)
        
        
    

  

            
