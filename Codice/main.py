import pygame, sys
from pygame.locals import *
from sfondo import *

WINDOW_SIZE = (1920, 1080)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Finestra Base')

clock = pygame.time.Clock()
fps = 60

# varibili di gioco


# immagini
sfondo_img = pygame.image.load("Immagini/immagine_sfondo.jpg")
sfondo_img = pygame.transform.scale(sfondo_img, (1920, 1080))
sfondoRect = Sfondo(screen, (0,0), sfondo_img, 5)
# sfondoRect.velocity = 5

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    sfondoRect.draw()
    sfondoRect.move()







    pygame.display.flip()
    clock.tick(fps)