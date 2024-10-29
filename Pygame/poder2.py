import pygame


class PoderDos:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.ancho = 20 
        self.alto = 20
        self.velocidad = 5
        self.color = "green"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load("C:\\Users\\emili\\OneDrive\\Documentos\\Códigos\\Pygame\\assets\\algaSprite.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.alto, self.ancho))


    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        #pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))

    def movimiento(self):
        self.y += self.velocidad
        self.rect.y = self.y