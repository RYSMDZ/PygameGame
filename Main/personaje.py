import pygame

class Avioncito:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.ancho = 50 
        self.alto = 50
        self.velocidad = 8
        self.color = "red"
        
        # Cargar las imágenes
        self.imagen = pygame.image.load("C:\\Users\\emili\\OneDrive\\Documentos\\Códigos\\Pygame\\assets\\PezSprite2.png")
        self.imagen_disfraz = pygame.image.load("C:\\Users\\emili\\OneDrive\\Documentos\\Códigos\\Pygame\\assets\\PezSpritePoderes2.png")

        # Escalar y rotar ambas imágenes
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.imagen_disfraz = pygame.transform.scale(self.imagen_disfraz, (self.ancho, self.alto))

        self.imagen = pygame.transform.rotate(self.imagen, -90)
        self.imagen_disfraz = pygame.transform.rotate(self.imagen_disfraz, -90)

        # Inicialmente, la imagen actual es la normal
        self.imagen_actual = self.imagen

        # Crear el rectángulo con el tamaño y posición inicial
        self.rect = self.imagen_actual.get_rect(topleft=(self.x, self.y))

    def dibujar(self, ventana):
        # Actualizar el rectángulo del personaje para mantener la posición actualizada
        self.rect.topleft = (self.x, self.y)
        
        # Dibujar el personaje con la imagen actual
        ventana.blit(self.imagen_actual, (self.x, self.y))
