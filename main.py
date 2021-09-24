import pygame
from Pixel import Pixel, draw_pixels
from Game import Game
import sys

resolution = (1024, 768)
screen = pygame.display.set_mode(resolution)
game = Game(screen)
gun = game.space_ship_gun()

# creating all wall rectangles
wall = []
pixel_x, pixel_y = 3, 200
for rows in range(0, 10):
    for columns in range(0, 51):
        pixel = Pixel(screen, "red", pixel_x, pixel_y, 19, 19)
        pixel_x += 20
        wall.append(pixel)
    pixel_y += 20
    pixel_x = 3


def space_ship_movements():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        game.ship_position[0] -= 3
    if key[pygame.K_RIGHT]:
        game.ship_position[0] += 3
    if key[pygame.K_UP]:
        game.ship_position[1] -= 3
    if key[pygame.K_DOWN]:
        game.ship_position[1] += 3
    if key[pygame.K_SPACE]:
        game.shot()


while True:
    game.background()
    game.space_ship()
    space_ship_movements()
    draw_pixels(wall)
    for item in wall:
        if pygame.Rect.colliderect(game.gun_rect, (item.x, item.y, item.width, item.height)):
            wall.remove(item)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
