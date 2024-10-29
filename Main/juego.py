#importando libreria
import pygame 
#trayendo el personaje del otro archivo
from Pygame.Main.personaje import Avioncito
#importando el enemigo
from enemigo import Enemigo
from bala import Bala
from Pygame.Main.poder import Poder
from Pygame.Main.poder2 import PoderDos


import random


pygame.init()



#creando dimensiones de la ventana
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
FPS = 60
FUENTE= pygame.font.SysFont("Comic Sans", 22)

jugando = True

#creando un reloj para la aparcición de enemigos 
reloj = pygame.time.Clock()
#reloj 2 para aparicion de poderes
duracion_poder = 5000
tiempo_poder_activo = 0
tiempo_pasado_poder = 0 
poder_activo = True

duracion_poder2 = 4000
tiempo_poder_activo2 = 0
tiempo_pasado_poder2 = 0 
poder_activo2 = False
# Añadir un nuevo factor para cámara lenta
factor_camara_lenta = 0.5  
camara_lenta_activa = False
duracion_camara_lenta = 5000  # Duración de la cámara lenta (5 segundos)
tiempo_camara_lenta_activa = 0
#definiendo las vidas 
vida = 3
puntos = 0

tiempo_pasado = 0

tiempo_entre_enemigos= 500

tiempo_entre_poder= 4000
tiempo_entre_poder2= 10000

avioncito = Avioncito(ANCHO/2,ALTO-75)
# Cambiar la imagen del personaje cuando el poder está activo
if poder_activo:
    avioncito.imagen_actual = avioncito.imagen_disfraz  # Cambia al disfraz
else:
    avioncito.imagen_actual = avioncito.imagen  # Regresa a la imagen normal

#Creando a los enemigos 
enemigos = []

enemigos.append(Enemigo(ANCHO/2,100))

# Creando poderes
poderes = []

poderes.append(Poder(ANCHO/2,100))

poderes2 = []

poderes2.append(PoderDos(ANCHO/2,100))

balas = []

ultima_bala = 0 
tiempo_entre_balas = 400 

# Haciendo funcion para crear balas

def crear_bala():
    global ultima_bala

    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        balas.append(Bala(avioncito.rect.centerx, avioncito.rect.centery))
        ultima_bala = pygame.time.get_ticks()
#definiendo las teclas para el juego 

def gestionar_teclas(teclas):
    #if teclas[pygame.K_w]:
    #   avioncito.y -= avioncito.velocidad
    #if teclas[pygame.K_s]:
    #    avioncito.y += avioncito.velocidad
    if teclas[pygame.K_a] and avioncito.x > 0:
        avioncito.x -= avioncito.velocidad
    if teclas[pygame.K_d] and avioncito.x + avioncito.ancho < ANCHO:
        avioncito.x += avioncito.velocidad
    if teclas[pygame.K_SPACE]:
        crear_bala()

#Haciendo bucle para mantener la ventana abierta 

while jugando and vida > 0 :
# Marcando el tempo de aparicion de los enemigos 
    delta_time = reloj.tick(FPS)
    tiempo_pasado += delta_time
    tiempo_pasado_poder += delta_time
    tiempo_pasado_poder2 += delta_time
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0,ANCHO),-100))
        tiempo_pasado = 0
        #poderes.append(Poder(random.randint(0,ANCHO), - 100))
        if puntos >= 100 | tiempo_pasado >= 50 :
            tiempo_entre_enemigos = 450
            enemigos.append(Enemigo(random.randint(0, ANCHO),-100))
            tiempo_pasado = 0
        if puntos >= 180 | tiempo_pasado >= 90 :
            tiempo_entre_enemigos = 415
            enemigos.append(Enemigo(random.randint(0, ANCHO),-100))
            tiempo_pasado = 0
        if puntos >= 240 | tiempo_pasado >= 130 :
            tiempo_entre_enemigos = 350
            enemigos.append(Enemigo(random.randint(0, ANCHO),-100))
            tiempo_pasado = 0
    if tiempo_pasado_poder > tiempo_entre_poder and not poder_activo:
        poderes.append(Poder(random.randint(0,ANCHO),-100))
        tiempo_pasado_poder = 0 
    if tiempo_pasado_poder2 > tiempo_entre_poder2 and not poder_activo2:
        poderes2.append(PoderDos(random.randint(0,ANCHO),-100))
        tiempo_pasado_poder2 = 0 
        

    eventos = pygame.event.get()

#dando función a las teclas
    teclas = pygame.key.get_pressed()
    
    texto_vida = FUENTE.render(f"Vida: {vida}", True, "white")
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")

    gestionar_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("lightblue")

    avioncito.dibujar(VENTANA)

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

        

# creando la colicion entre jugador y enemigo
        if pygame.Rect.colliderect(avioncito.rect, enemigo.rect):
            vida -= 1
            enemigos.remove(enemigo)

#sumando puntaje cada vez que un enemigo sobrepasa la pantalla y eliminandolo su vez
        if enemigo.y > ALTO:
            puntos += 1
            enemigos.remove(enemigo)


# Creando funcion que cada que las balas toquen el enemigo lo destruya
        for bala in balas:
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigo.vida -= 1
                balas.remove(bala)
                puntos += 1

        if enemigo.vida <= 0:
            enemigos.remove(enemigo)

        
    # creando colicion entre poder y jugador
    for poder in poderes[:]:
        poder.dibujar(VENTANA)
        poder.movimiento() 
    

        # Colisión entre jugador y poder
        if pygame.Rect.colliderect(avioncito.rect, poder.rect):
            poder_activo = True
            tiempo_poder_activo = pygame.time.get_ticks()  # Guardar el tiempo de activación
            tiempo_entre_balas = 300  # Aumentar velocidad de disparo
            avioncito.imagen_actual = avioncito.imagen_disfraz 
            poderes.remove(poder)

        # Eliminar poderes que salen de la pantalla
        if poder.y > ALTO:
            poderes.remove(poder)

    # Desactivar el poder después de un tiempo
    if poder_activo and pygame.time.get_ticks() - tiempo_poder_activo > duracion_poder:
        poder_activo = False
        tiempo_entre_balas = 400  # Restaurar la velocidad de disparo normal
        avioncito.imagen_actual = avioncito.imagen


    for bala in balas:
        bala.dibujar(VENTANA)
        bala.movimiento()

        if bala.y > ALTO :
            balas.remove(bala)

    for poder2 in poderes2[:]:
        poder2.movimiento() 
        poder2.dibujar(VENTANA)
    

        # Colisión entre jugador y poder
        if pygame.Rect.colliderect(avioncito.rect, poder2.rect):
            camara_lenta_activa = True
            tiempo_camara_lenta_activa = pygame.time.get_ticks()
            poderes2.remove(poder2)
            poder_activo2 = True

        # Eliminar poderes que salen de la pantalla
        if poder2.y > ALTO:
            poderes2.remove(poder2)

    # Desactivar el poder después de un tiempo
    if camara_lenta_activa and pygame.time.get_ticks() - tiempo_camara_lenta_activa > duracion_camara_lenta:
        camara_lenta_activa = False 
        avioncito.imagen_actual = avioncito.imagen
        poder_activo2 = False

    if camara_lenta_activa:
        delta_time *= factor_camara_lenta
        
    for enemigo in enemigos:
        enemigo.movimiento(delta_time, camara_lenta_activa)

    for bala in balas:
        bala.movimiento(delta_time, camara_lenta_activa)

    

   

#poniendo texto de vida y puntos en pantalla 
    VENTANA.blit(texto_vida, (880,20))
    VENTANA.blit(texto_puntos, (880,43))

    pygame.display.update()

#poniendo las puntuaciones

pygame.quit()
 

#nombre = input("Cuál es tu nombre?")
#
#with open ('puntuaciones.txt', 'a') as puntuacionesArchivo:
#    puntuacionesArchivo.write(nombre, puntos)
quit()

        