import pygame, sys
from pygame.locals import *

WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Finestra Base')

clock = pygame.time.Clock()
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()







    pygame.display.flip()





    clock.tick(fps)




