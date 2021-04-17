import pygame
import sys
 
class Game():
    
    corredores = []
    
    def __init__(self):
        
        # crear pantalla
        self.__screen = pygame.display.set_mode((1002, 632))
        # título de la pantalla
        pygame.display.set_caption('Carrera de bichos')
        # hay que cargar la imagen de fondo de la pantalla
        self.background = pygame.image.load('images/background2.jpg')
        
        self.runner = pygame.image.load('images/smallball.png')
    
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
            # comprobación de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # pinta la pantalla en la posición (0,0)
                # refrescar/renderizar la pantalla
                self.__screen.blit(self.background, (0,0))
                self.__screen.blit(self.runner, (x, 240))
                pygame.display.flip()
                
                x += 3
                if x >= 250:
                    hayGanador = True
            
            pygame.quit()
            sys.exit() 
        
if  __name__ == '__main__':
    pygame.init()
    game = Game()
    