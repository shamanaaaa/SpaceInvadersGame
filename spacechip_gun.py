import time

import pygame


class Gun(pygame.sprite.Sprite):
    def __init__(self, screen, start_x, start_y):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.start_x = start_x + 22
        self.start_y = start_y
        self.width = 2
        self.height = 30

    def update(self, ship_position_1, ship_position_2):
        if self.start_y < -40:
            self.start_y = ship_position_1
            self.start_x = ship_position_2 + 22
        self.start_y -= 10
        self.gun = pygame.draw.rect(self.screen, "orange", [self.start_x, self.start_y, self.width, self.height])
        self.rect = pygame.Rect(self.start_x, self.start_y, self.width, self.height)

