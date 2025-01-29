import pygame as pg
import sys

pg.init()

screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
running = True

pg.display.set_caption("Flappy Bird")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock = pg.time.Clock()
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = screen_height - 300
        self.jump_speed = -15
        self.gravity = 1
        self.velocity = 5

    def update(self):
        keys = pg.key.get_pressed()
        print(self.rect.y)
        if keys[pg.K_SPACE]: #and self.rect.bottom >= screen_height:
            self.velocity = self.jump_speed

        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.velocity = 0




















while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False