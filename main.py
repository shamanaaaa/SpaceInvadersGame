import pygame
from Pixel import Pixel, draw_pixels
from Game import Game
from spacechip_gun import Gun
import sys

resolution = (1024, 768)
screen = pygame.display.set_mode(resolution)
game = Game(screen)
gun = Gun(screen, game.ship_position[0], game.ship_position[1])

# creating all wall rectangles
wall = []
pixel_x, pixel_y = 3, 200
for rows in range(0, 20):
    for columns in range(0, 102):
        pixel = Pixel(screen, "red", pixel_x, pixel_y, 9, 9)
        pixel_x += 10
        wall.append(pixel)
    pixel_y += 10
    pixel_x = 3


def space_ship_movements():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        game.ship_position[0] -= 3
    if key[pygame.K_RIGHT]:
        game.ship_position[0] += 3


while True:
    game.background()
    game.space_ship()
    space_ship_movements()
    draw_pixels(wall)
    gun.update(game.ship_position[1], game.ship_position[0])

    # check gun collision with wall
    for item in wall:
        if pygame.Rect.colliderect(gun.rect, (item.x, item.y, item.width, item.height)):
            wall.remove(item)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
