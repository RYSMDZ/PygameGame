import pygame

class Bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.ancho = 10 
        self.alto = 20
        self.velocidad = 7
        self.color = "white"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)

    def movimiento(self, delta_time=1, camara_lenta_activa = False):
        if camara_lenta_activa:
            # Si la cámara lenta está activa, ralentizar el movimiento
            self.y -= self.velocidad * (delta_time / 1000)  # delta_time en milisegundos
        else:
            # Movimiento normal
            self.y -= self.velocidad
            self.rect.topleft = (self.x, self.y)