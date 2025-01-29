import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Définir le titre de la fenêtre
pygame.display.set_caption("Geometry Dash Clone")

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définir la vitesse de rafraîchissement
clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = screen_height -300
        self.jump_speed = -15
        self.gravity = 1
        self.velocity = 5

    def update(self):
        keys = pygame.key.get_pressed()
        print(self.rect.y)
        if keys[pygame.K_SPACE]: #and self.rect.bottom >= screen_height:
            self.velocity = self.jump_speed

        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.velocity = 0

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

obstacles = pygame.sprite.Group()

def create_obstacle():
    obstacle = Obstacle(screen_width, screen_height - 100, 50, 50)
    obstacles.add(obstacle)
    all_sprites.add(obstacle)

# Ajouter des obstacles périodiquement
pygame.time.set_timer(pygame.USEREVENT, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            create_obstacle()

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()