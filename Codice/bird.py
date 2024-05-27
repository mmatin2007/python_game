import pygame

class Bird:
    def __init__(self, image, x, y, size, velocity, gravity, jump_strength):
        self.image = pygame.image.load("Immagini/bird1.png")
        self.image = pygame.transform.scale(self.image, size)
        self.x = x
        self.y = y
        self.size = size
        self.velocity = velocity
        self.gravity = gravity
        self.jump_strength = jump_strength
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect = self.image.get_rect(center=(self.x, self.y))

        if self.y >= 531:  
            self.y = 531
        if self.y <= 0:  
            self.y = 0

            self.velocity = 0

    def jump(self):
        self.velocity = -self.jump_strength

    def draw(self, screen):
        screen.blit(self.image, self.rect)

