import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Simple Sound Player")

sound = pygame.mixer.Sound('Codice/file.mp3')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            sound.play()

    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            sound.play()
    screen.fill((255, 255, 255))
    pygame.display.flip()
pygame.quit()

