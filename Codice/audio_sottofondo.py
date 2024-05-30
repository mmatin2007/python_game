import pygame, sys
from pygame.locals import *
import subprocess
import winsound
# Play Windows exit sound.
# winsound.PlaySound("SystemDefault sound", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
# winsound.PlaySound("*", winsound.SND_ALIAS)





# import winsound
 
# freq = 100
# dur = 50
 
# # loop iterates 5 times i.e, 5 beeps will be produced.
# for i in range(0, 5):    
#     winsound.Beep(freq, dur)    
#     freq+= 100
#     dur+= 50

# import pygame 
# pygame. init()
# my_sound = pygame. mixer. Sound('C:\Users\Lenovo\Documents\abc.wav')
# my_sound. play()




# import winsound
 
 
# # Play Windows question sound
# winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Simple Sound Player")

# Load the sound file
# Replace 'your_sound_file.wav' with the path to your sound file
sound = pygame.mixer.Sound('Codice/file.mp3')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Play the sound when any key is pressed
            sound.play()

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
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

