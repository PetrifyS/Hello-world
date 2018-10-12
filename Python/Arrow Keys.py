# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initailize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH / 2, HEIGHT / 2
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx -= 10
        if key[pygame.K_RIGHT]:
            self.speedx += 10        
        if key[pygame.K_DOWN]:
            self.speedy += 10
        if key[pygame.K_UP]:
            self.speedy -= 10
        if self.speedx >= 10:
            self.speedx = 10
        if self.speedy >= 10:
            self.speedy = 10
        if self.rect.right > WIDTH:
            self.rect.right = 0
             
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        

all_sprites = pygame.sprite.Group()
sprite = Sprite()
all_sprites.add(sprite)
# Game loop
running = True
while running:
    # keep loop runinng at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
