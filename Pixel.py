import pygame


class Pixel(pygame.sprite.Sprite):
    def __init__(self, screen, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill("red")
        self.color = color
        self.screen = screen
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def draw_pixels(wall):
    for pixel in wall:
        pygame.draw.rect(pixel.screen, pixel.color, (pixel.x, pixel.y, pixel.width, pixel.height))

