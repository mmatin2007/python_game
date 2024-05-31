import pygame
from pygame.locals import *
from random import randint

class Meteoriti:
    def __init__(self,screen, frames, tot):
        self.screen = screen
        self.frames = frames
        self.tot = tot
        self.pos = (950, randint(50, 500))
        self.rect = []
        self.collide_recta = pygame.rect.Rect((0,0), (40, 40))
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (100, 100))
            self.rect.append(self.frames[i].get_rect())
        for i in range(len(self.frames)):
            self.rect[i].center = self.pos
        self.collide_recta.center = self.pos

        self.lista = []
        self.j = 0
        self.velocity = 7
        

    def draw(self, j):
        for i in range(len(self.lista)):
            image = self.lista[i].frames[j]
            rect = self.lista[i].rect[j]
            self.screen.blit(image, rect)

    def move(self):
        for i in range(len(self.lista)):
            for j in range(len(self.frames)):
                self.lista[i].rect[j].x -= self.velocity
            self.lista[i].collide_recta.x -= self.velocity

    def newRock(self):
        if len(self.lista) <= self.tot:
            self.lista.append(Meteoriti(self.screen, self.frames, self.tot))
        elif 0 < self.lista[self.j].collide_recta.center[0] < 950:
            return 0
        else:
            self.lista[self.j] = Meteoriti(self.screen, self.frames, self.tot)
            if self.j < self.tot:
                self.j += 1
            else:
                self.j = 0



