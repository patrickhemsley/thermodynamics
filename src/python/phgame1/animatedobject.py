import pygame
import include 

class PHAnimation:
	
    def draw3(self, screen):
        pygame.draw.polygon(screen,include.black,[[100,100],[0,200],[200,200]],5) 
        
