import pygame, sys
from pygame.mouse import get_pos
import random


pygame.init()

#tamaño de mi ventana (size)
size = (900,600)

#creo la ventana (screen)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


#----------------------------------------------------------------------------------------LAS CARTAS
# Cartas:
mas_2_amarillo = pygame.image.load('img/+2-amarillo.png').convert()
saltomarillo = pygame.image.load('img/salto-amarillo.png').convert()
sentido_contrariomarillo = pygame.image.load('img/sentido-contrario-amarillo.png').convert()
amarillo_0 = pygame.image.load('img/0-amarillo.png').convert()
amarillo_1 = pygame.image.load('img/1-amarillo.png').convert()
amarillo_2 = pygame.image.load('img/2-amarillo.png').convert()
amarillo_3 = pygame.image.load('img/3-amarillo.png').convert()
amarillo_4 = pygame.image.load('img/4-amarillo.png').convert()
amarillo_5 = pygame.image.load('img/5-amarillo.png').convert()
amarillo_6 = pygame.image.load('img/6-amarillo.png').convert()
amarillo_7 = pygame.image.load('img/7-amarillo.png').convert()
amarillo_8 = pygame.image.load('img/8-amarillo.png').convert()
amarillo_9 = pygame.image.load('img/9-amarillo.png').convert()


mas_2_azul = pygame.image.load('img/+2-azul.png').convert()
saltozul = pygame.image.load('img/salto-azul.png').convert()
sentido_contrario_azul = pygame.image.load('img/sentido-contrario-azul.png').convert()
azul_0 = pygame.image.load('img/0-azul.png').convert()
azul_1 = pygame.image.load('img/1-azul.png').convert()
azul_2 = pygame.image.load('img/2-azul.png').convert()
azul_3 = pygame.image.load('img/3-azul.png').convert()
azul_4 = pygame.image.load('img/4-azul.png').convert()
azul_5 = pygame.image.load('img/5-azul.png').convert()
azul_6 = pygame.image.load('img/6-azul.png').convert()
azul_7 = pygame.image.load('img/7-azul.png').convert()
azul_8 = pygame.image.load('img/8-azul.png').convert()
azul_9 = pygame.image.load('img/9-azul.png').convert()


mas_2_verde = pygame.image.load('img/+2-verde.png').convert()
salto_verde = pygame.image.load('img/salto-verde.png').convert()
sentido_contrario_verde = pygame.image.load('img/sentido-contrario-verde.png').convert()
verde_0 = pygame.image.load('img/0-verde.png').convert()
verde_1 = pygame.image.load('img/1-verde.png').convert()
verde_2 = pygame.image.load('img/2-verde.png').convert()
verde_3 = pygame.image.load('img/3-verde.png').convert()
verde_4 = pygame.image.load('img/4-verde.png').convert()
verde_5 = pygame.image.load('img/5-verde.png').convert()
verde_6 = pygame.image.load('img/6-verde.png').convert()
verde_7 = pygame.image.load('img/7-verde.png').convert()
verde_8 = pygame.image.load('img/8-verde.png').convert()
verde_9 = pygame.image.load('img/9-verde.png').convert()


mas_2_rojo = pygame.image.load('img/+2-rojo.png').convert()
salto_rojo = pygame.image.load('img/salto-rojo.png').convert()
sentido_contrario_rojo = pygame.image.load('img/sentido-contrario-rojo.png').convert()
rojo_0 = pygame.image.load('img/0-rojo.png').convert()
rojo_1 = pygame.image.load('img/1-rojo.png').convert()
rojo_2 = pygame.image.load('img/2-rojo.png').convert()
rojo_3 = pygame.image.load('img/3-rojo.png').convert()
rojo_4 = pygame.image.load('img/4-rojo.png').convert()
rojo_5 = pygame.image.load('img/5-rojo.png').convert()
rojo_6 = pygame.image.load('img/6-rojo.png').convert()
rojo_7 = pygame.image.load('img/7-rojo.png').convert()
rojo_8 = pygame.image.load('img/8-rojo.png').convert()
rojo_9 = pygame.image.load('img/9-rojo.png').convert()

mas_4_colores = pygame.image.load('img/+4-colores.png').convert()

cambio_color = pygame.image.load('img/cambio.png').convert()

base = pygame.image.load('img/base.png').convert()

fondo = pygame.image.load('img/fondo.jpg').convert()

#---------------------------------------------------------------------------------------------------

mazo = [
    mas_2_amarillo, saltomarillo, sentido_contrariomarillo, amarillo_0, amarillo_1, amarillo_2, amarillo_3, amarillo_4, amarillo_5, amarillo_6, amarillo_7, amarillo_8, amarillo_9,
    mas_2_amarillo, saltomarillo, sentido_contrariomarillo, amarillo_1, amarillo_2, amarillo_3, amarillo_4, amarillo_5, amarillo_6, amarillo_7, amarillo_8, amarillo_9,
    mas_2_azul, saltozul, sentido_contrario_azul, azul_0, azul_1, azul_2, azul_3, azul_4, azul_5, azul_6, azul_7, azul_8, azul_9,
    mas_2_azul, saltozul, sentido_contrario_azul, azul_1, azul_2, azul_3, azul_4, azul_5, azul_6, azul_7, azul_8, azul_9,
    mas_2_verde, salto_verde, sentido_contrario_verde, verde_0, verde_1, verde_2, verde_3, verde_4, verde_5, verde_6, verde_7, verde_8, verde_9,
    mas_2_verde, salto_verde, sentido_contrario_verde, verde_1, verde_2, verde_3, verde_4, verde_5, verde_6, verde_7, verde_8, verde_9,
    mas_2_rojo, salto_rojo, sentido_contrario_rojo, rojo_0, rojo_1, rojo_2, rojo_3, rojo_4, rojo_5, rojo_6, rojo_7, rojo_8, rojo_9,
    mas_2_rojo, salto_rojo, sentido_contrario_rojo, rojo_1, rojo_2, rojo_3, rojo_4, rojo_5, rojo_6, rojo_7, rojo_8, rojo_9,
    mas_4_colores, mas_4_colores, mas_4_colores, mas_4_colores,
    cambio_color, cambio_color, cambio_color, cambio_color
]




#listas de posibilidades de juego por color:
conbinaciones_posibles = [[mas_2_amarillo, saltomarillo, sentido_contrariomarillo, amarillo_0, amarillo_1, amarillo_2, amarillo_3, amarillo_4, amarillo_5, amarillo_6, amarillo_7, amarillo_8, amarillo_9, mas_4_colores,
    cambio_color],[mas_2_azul, saltozul, sentido_contrario_azul, azul_0, azul_1, azul_2, azul_3, azul_4, azul_5, azul_6, azul_7, azul_8, azul_9, mas_4_colores,
    cambio_color],[mas_2_verde, salto_verde, sentido_contrario_verde, verde_0, verde_1, verde_2, verde_3, verde_4, verde_5, verde_6, verde_7, verde_8, verde_9,  mas_4_colores,
    cambio_color],[mas_2_rojo, salto_rojo, sentido_contrario_rojo, rojo_0, rojo_1, rojo_2, rojo_3, rojo_4, rojo_5, rojo_6, rojo_7, rojo_8, rojo_9,  mas_4_colores,
    cambio_color],[amarillo_1, azul_1, verde_1, rojo_1],[amarillo_2, azul_2, verde_2, rojo_2],[amarillo_3, azul_3, verde_3, rojo_3],[amarillo_3, azul_3, verde_3, rojo_3],[amarillo_4, azul_4, verde_4, rojo_4],[amarillo_5, 
    azul_5, verde_5, rojo_5],[amarillo_6, azul_6, verde_6, rojo_6],[amarillo_7, azul_7, verde_7, rojo_7],[amarillo_8, azul_8, verde_8, rojo_8],[amarillo_9, azul_9, verde_9, rojo_9],[saltomarillo,saltozul,salto_verde,salto_rojo],
    [cambio_color],[mas_4_colores]]


#------------------------------------------------------------------------------------------------



class Mazos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mazo = mazo
        self.descarte = base #va a ir cambiando y actualizandose
        self.ultimaDelMazo = self.mazo[0]

    def mezclar_mazo(self):
        random.shuffle(self.mazo)

    def iniciar_jugada(self, jugadores):
        #colocar la primera carta del juego:
        carta = self.mazo.pop(0)
        self.descarte = carta
        
        # Actualizar la carta descarte de los jugadores
        for jugador in jugadores:
            jugador.descarte = self.descarte
            
            


class JugadorUno(Mazos):
    def __init__(self):
        super().__init__()
        self.cartas = []
        

    def repartir_cartas(self):
        for i in range(7):
            carta = self.mazo.pop(0) # de 0 iniciamos a la inversa del maso
            self.cartas.append(carta)


    def sumar_carta(self):
        
        conbinable = False
        for carta in self.cartas:

            for lista in conbinaciones_posibles:
                if carta in lista and self.descarte in lista:
                    conbinable = True
                    break
        
        if conbinable == False:
            carta = self.mazo.pop(0) # de 0 iniciamos a la inversa del maso
            self.cartas.append(carta)
        
        # Actualizar la carta descarte de los jugadores
        for jugador in jugadores:
            jugador.cartas = self.cartas
    

    def jugar(self, index, jugadores):
        
        carta = self.cartas[index]

        conbinable = False

        for lista in conbinaciones_posibles:
            if carta in lista and self.descarte in lista:
                conbinable = True
                #print(conbinable)
                break
        
        if conbinable:
            carta = self.cartas.pop(index)  # Eliminar la carta seleccionada por jugador uno
            self.descarte = carta  # descarta la carta
        
            # Actualizar la carta descarte de los jugadores
            for jugador in jugadores:
                jugador.descarte = self.descarte
        

    
    
#----------------------------------------------------------------------------------
#Comiensa la partida (instancia de la clase Mazos) para barajar cartas:
mazos = Mazos()

while True:
    mazos.mezclar_mazo()

    if mazos.ultimaDelMazo == mas_4_colores: #la ultima no debe ser +4 colores
        continue
    else:
        break


#mazos.iniciar_jugada()

#(instanciamos Jugador Uno) lista de maso de cartas del jugador uno:
jugadorUno = JugadorUno()
jugadorUno.repartir_cartas()
#Cordenadas de la pocision de cada carta del J-1 en la interfaz:
x_Uno = 100
y_Uno = 50

# Crear una lista de jugadores y agregar a jugadorUno
jugadores = [jugadorUno, mazos]

# Iniciar la jugada pasando la lista de jugadores
mazos.iniciar_jugada(jugadores)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Verificar si se hizo clic con el botón izquierdo del mouse
            x, y = get_pos()  # Obtener la posición del clic del mouse
            index = (x - 100) // 100  # Calcular el índice de la carta seleccionada
            
            if 0 <= index < len(jugadorUno.cartas):
                jugadorUno.jugar(index, jugadores)
                


    

    screen.blit(fondo,[0,0]) #-------------------------ZONA DE DIBUJO:

    #pocisiono el maso de cartas principal
    for carta in mazos.mazo:     
        screen.blit(carta,(350,234))
        


    #maso de cartas descartadas:
    #for carta in mazos.descartadas:
    screen.blit(mazos.descarte,(450,234))



    #maso del jugador uno:
    for carta in jugadorUno.cartas:
        screen.blit(carta,(x_Uno,y_Uno))
        x_Uno = x_Uno + 100
        #print(x_Uno,y_Uno)

    x_Uno = 100 #inicializamos la cordenada
    
    #----------------------------------------------------------------
    

    

    pygame.display.flip()
    clock.tick(60)