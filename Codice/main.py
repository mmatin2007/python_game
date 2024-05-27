import pygame
from pygame.locals import *
from sfondo import *
from bird import *
from tubi import *

pygame.init()

larghezza = 850
altezza = 531
WINDOW_SIZE =(larghezza, altezza)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Finestra Base')

bird_image = pygame.image.load('Immagini/bird1.png')

bird = Bird(image=bird_image, x=100, y=300, size = (100, 100) ,velocity=0, gravity=0.5, jump_strength=10)
#bird = Bird(image=bird_image, x=100, y=300, velocity=0, gravity=0.5, jump_strength=10)

clock = pygame.time.Clock()
fps = 60

# Immagini
sfondo_img = pygame.image.load('Immagini/spazio_Img.jpg').convert()
sfondo_img = pygame.transform.scale(sfondo_img, (larghezza, altezza))
sfondoRect = Sfondo(screen, pos=(0, 0), image=sfondo_img, velocity=5)

sfondo_duplicato = pygame.Surface((larghezza * 2, altezza))
sfondo_duplicato.blit(sfondo_img, (0, 0))
sfondo_duplicato.blit(sfondo_img, (larghezza, 0))

posizione_sfondo = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    posizione_sfondo -= 1
    if posizione_sfondo <= -larghezza:
        posizione_sfondo = 0

    sfondoRect.move()  # Aggiorna la posizione dello sfondo
    screen.blit(sfondo_duplicato, (posizione_sfondo, 0))

    bird.update()  # Aggiorna la posizione dell'uccello
    bird.draw(screen)  # Disegna l'uccello sullo schermo

    pygame.display.update()
    clock.tick(fps)

pygame.quit()