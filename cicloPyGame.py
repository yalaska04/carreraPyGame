import pygame, sys

width = 640
height = 480

# Crea pantalla
screen = pygame.display.set_mode((width, height))
# rellenar pantalla color rojo
screen.fill((246, 147, 48))
pygame.display.set_caption('Ciclo básico de pygame')

pygame.init()

gameOver = False
# comprobación de eventos 
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
    # refrescar pantalla:
        pygame.display.flip()
            


pygame.quit()
sys.exit()
        