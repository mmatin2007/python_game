import pygame
from pygame.locals import *

pygame.init()

larghezza = 850
altezza = 531
colore_sfondo = (30, 30, 30)
colore_bottone = (70, 130, 180)
colore_bottone2 = (100, 149, 237)
colore_testo = (255, 255, 255)
larghezza_bottone = 200
altezza_bottone = 80

screen = pygame.display.set_mode((larghezza, altezza))
pygame.display.set_caption("Start Menu")

font = pygame.font.Font(None, 74)

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = colore_bottone
        self.hover_color = colore_bottone2
        self.current_color = self.color

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect)
        text_surface = font.render(self.text, True, colore_testo)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def mouse_sopra(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_sopra():
            return True
        return False




