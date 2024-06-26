import pygame, sys
from pygame.locals import *
from sfondo import *
from bird import *
from botton import *
from meteoriti import *

pygame.init()

import winsound 



larghezza = 850
altezza = 531
WINDOW_SIZE =(larghezza, altezza)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Finestra Base')

larghezzaB = 850
altezzaB = 531
colore_sfondo = (30, 30, 30)
colore_bottone = (70, 130, 180)
colore_bottone2 = (100, 149, 237)
colore_testo = (255, 255, 255)
larghezza_bottone = 200
altezza_bottone = 80

screen = pygame.display.set_mode((larghezza, altezza))
pygame.display.set_caption("Start Menu")

font = pygame.font.Font(None, 74)

def main_menu():
    start_button = Button(larghezzaB // 2 - larghezza_bottone // 2, altezzaB // 2 - altezza_bottone // 2, larghezza_bottone, altezza_bottone, "START")
    
    while True:
        screen.fill(colore_sfondo)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if start_button.handle_event(event):
                play()
        
        if start_button.mouse_sopra():
            start_button.current_color = start_button.hover_color
        else:
            start_button.current_color = start_button.color
        start_button.draw(screen)

        pygame.display.flip()


def play():

    # setto frquenza a 850
    freq = 850

    # durata di 100 millisecondi			 
    dur = 100
                
    winsound.Beep(freq, dur)

    bird_image = pygame.image.load('Immagini/bird1.png')

    meteoriti_image = []
    meteoriti_image.append(pygame.image.load("Immagini/meteoriti.png"))
    meteoriti = Meteoriti(screen, meteoriti_image, tot = 5)

    bird = Bird(image=bird_image, x=100, y=300, size = (100, 100) ,velocity=0, gravity=0.5, jump_strength=10)

    clock = pygame.time.Clock()
    fps = 60

                # Immagini
    sfondo_img = pygame.image.load('Immagini/novo_sfondo (1).jpeg').convert()
    sfondo_img = pygame.transform.scale(sfondo_img, (larghezza, altezza))
    sfondoRect = Sfondo(screen, pos=(0, 0), image=sfondo_img, velocity=5)

    sfondo_duplicato = pygame.Surface((larghezza * 2, altezza))
    sfondo_duplicato.blit(sfondo_img, (0, 0))
    sfondo_duplicato.blit(sfondo_img, (larghezza, 0))

    posizione_sfondo = 0
    keys=pygame.key.get_pressed()

    running = True

    sound = pygame.mixer.Sound('Codice/file.mp3')
    sound.play()
    
    pRsPawn=0

    cond_gameover = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        bird.jump()
                        # setto frquenza a 500 Hz
                        freq = 420

                        # durata di 100 millisecondi			 
                        dur = 50
                                    
                        winsound.Beep(freq, dur)
        if cond_gameover == False:
            posizione_sfondo -= 1
            if posizione_sfondo <= -larghezza:
                posizione_sfondo = 0

            for i in range(len(meteoriti.lista)):
                if meteoriti.lista[i].collide_recta.colliderect(bird.rect):
                    cond_gameover = True
                    
                    # pygame.quit()

            sfondoRect.move()  
            screen.blit(sfondo_duplicato, (posizione_sfondo, 0))

            bird.update()  
            bird.draw(screen) 

            meteoriti.move()
            meteoriti.draw(0)
            if pRsPawn >= randint(1000, 10000):
                meteoriti.newRock() 
                pRsPawn = 0
            pRsPawn += fps

        else:
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 80)
            text = font.render("GAME OVER", 1, (255, 255, 255))
            screen.blit(text, (250, 250))
        pygame.display.flip()
        pygame.display.update()
                    
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main_menu()

