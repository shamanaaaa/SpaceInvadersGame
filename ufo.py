import pygame
import random


class Ufo(pygame.sprite.Sprite):
    def __init__(self, screen, gun_speed):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.ufo = pygame.image.load('images/ufo.png').convert_alpha()
        self.ufo = pygame.transform.scale(self.ufo, (70, 50))
        self.rect = self.ufo.get_rect()
        self.rect[0] = random.randint(0, 950)
        self.rect[1] = random.randint(0, 140)
        self.going_right = True
        self.speed = [random.randint(1, 5), 0]
        self.gun_width, self.gun_height = 2, 30
        self.start_y = self.rect[1] + 30
        self.start_x = self.rect[0] + 35
        self.collision_pixel_counter = 0
        self.gun_speed = gun_speed

    def draw_ufo(self):
        self.rect[0] += self.speed[0]
        self.rect[1] += self.speed[1]
        self.screen.blit(self.ufo, self.rect)
        if self.rect[0] > 1000 and self.going_right:
            self.speed[0] = - random.randint(1, 5)
            self.going_right = False
        if self.rect[0] < -40 and not self.going_right:
            self.speed[0] = random.randint(1, 5)
            self.going_right = True

    def draw_gun(self, wall):
        self.gun = pygame.draw.rect(self.screen, "red", [self.start_x, self.start_y, self.gun_width, self.gun_height])
        self.gun_rect = pygame.Rect(self.start_x, self.start_y, self.gun_width, self.gun_height)
        if self.start_y > 700:
            self.start_y = self.rect[1] + 30
            self.start_x = self.rect[0] + 35
            self.collision_pixel_counter = 0
        self.start_y = self.start_y + self.gun_speed
        self.ufo_gun_collision(wall)

    def ufo_gun_collision(self, wall):
        for pixel in wall:
            if pygame.Rect.colliderect(self.gun_rect, [pixel.x, pixel.y, pixel.width, pixel.height]):
                self.collision_pixel_counter += 1
                if self.collision_pixel_counter < random.choice([5, 6, 7, 8, 9, 10]):
                    wall.remove(pixel)
                else:
                    self.start_y = self.rect[1] + 30
                    self.start_x = self.rect[0] + 35
                    self.collision_pixel_counter = 0
