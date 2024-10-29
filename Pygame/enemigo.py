import pygame
import random

class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.ancho = 50 
        self.alto = 50
        self.velocidad = 3
        self.color = "purple"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.vida = 3
        self.enemigosLista = ["C:\\Users\\emili\\OneDrive\\Documentos\\Códigos\\Pygame\\assets\\SpriteCaca-removebg-preview.png", 
                              "C:\\Users\\emili\\OneDrive\\Documentos\\Códigos\\Pygame\\assets\\spriteBasura-removebg-preview.png"]
        self.imagen = pygame.image.load(random.choice(self.enemigosLista))
        self.imagen = pygame.transform.scale(self.imagen, (self.alto, self.ancho))

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        #pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))

    def movimiento(self, delta_time=1, camara_lenta_activa = False):
        if camara_lenta_activa:
            # Si la cámara lenta está activa, ralentizar el movimiento
            self.y += self.velocidad * (delta_time / 1000)  # delta_time en milisegundos
        else:
            # Movimiento normal
            self.y += self.velocidad
            self.rect.topleft = (self.x, self.y)

        