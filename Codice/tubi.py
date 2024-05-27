


# import pygame
# from pygame import *
# import random

# class Tubo:
#     def __init__(self, screen, x, y_top, y_bottom, width, height, velocity):
#         self.screen = screen
#         self.x = x
#         self.y_top = y_top
#         self.y_bottom = y_bottom
#         self.width = width
#         self.height = height
#         self.velocity = velocity

#     def update(self):
#         self.x -= self.velocity

#     def draw(self):
#         pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y_top, self.width, self.height))
#         pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y_bottom, self.width, self.height))

# # Nella parte iniziale del tuo codice:
# tubi = []  # Lista per tenere traccia dei tubi

# # Nel ciclo while:
# if len(tubi) == 0 or tubi[-1].x < larghezza - 200:
#     # Genera un nuovo tubo
#     y_top = random.randint(50, 300)
#     y_bottom = y_top + 200
#     tubo = Tubo(screen, larghezza, y_top, y_bottom, 50, 300, 5)
#     tubi.append(tubo)

# # Aggiorna e disegna i tubi
# for tubo in tubi:
#     tubo.update()
#     tubo.draw()

# # Nel ciclo while:
# for tubo in tubi:
#     if bird.x + bird.size[0] > tubo.x and bird.x < tubo.x + tubo.width:
#         if bird.y < tubo.y_top or bird.y + bird.size[1] > tubo.y_bottom:
#             print("Game Over")
#             running = False

# # Inizializza il punteggio all'inizio del tuo codice:
# punteggio = 0

# # Nel ciclo while:
# for tubo in tubi:
#     if bird.x > tubo.x + tubo.width:
#         punteggio += 1
#         print(f"Punteggio: {punteggio}")



# import pygame
# from pygame import *
