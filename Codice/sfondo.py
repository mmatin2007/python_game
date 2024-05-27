import pygame
class Sfondo:
    def __init__(self, screen, pos, image, velocity = 5) -> None:
        self.screen = screen
        self.pos = pos
        self.image = image
        self.velocity = velocity

        self.rect = []
        self.rect.append(self.image.get_rect())
        self.rect.append(self.image.get_rect())

    def draw(self):
        self.screen.blit(self.image, self.rect[0],self.rect[1])
    
    def move(self):
        if self.rect[1].x == 0:
            self.rect[0].x = 1921
        elif self.rect[0].x == 0:
            self.rect[1].x = 1921
    
        self.rect[0].x -= self.velocity
        self.rect[1].x -= self.velocity