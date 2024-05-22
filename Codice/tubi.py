import pygame
from pygame import *

# class Tubi:
#     def __init__(self, screen, pos, tubi, velocity = 5) -> None:
#         self.screen = screen
#         self.pos = pos
#         self.tubi = tubi
#         self.velocity = velocity

#         self.rect = []
#         self.rect.append(self.tubi.get_rect())
#         self.rect.append(self.tubi.get_rect())

#     def draw(self):
#         self.screen.blit(self.tubi, self.rect[0],self.rect[1])
    
#     def move(self):
#         if self.rect[1].x == 0:
#             self.rect[0].x = 1921
#         elif self.rect[0].x == 0:
#             self.rect[1].x = 1921
    
#         self.rect[0].x -= self.velocity
#         self.rect[1].x -= self.velocity