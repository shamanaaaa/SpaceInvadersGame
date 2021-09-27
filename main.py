import time

import pygame
import random
import sys

from ufo import Ufo
from Game import Game
from Pixel import Pixel, draw_pixels
from spacechip_gun import Gun

resolution = (1024, 768)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Space invaders game')
game = Game(screen)
gun = Gun(screen, game.ship_position[0], game.ship_position[1])
pygame.font.init()
my_font = pygame.font.SysFont("monospace", 26)
my_font_2 = pygame.font.SysFont("monospace", 100)
score = 0
lives = 3
wall = []
ufos = []
game_over = ""
is_game_over = False
ufos_gun_start_speed = 10
level = 1


# creating all wall rectangles
def create_wall():
    global wall
    pixel_x, pixel_y = 3, 200
    for rows in range(0, 20):
        for columns in range(0, 204):
            pixel = Pixel(screen, "red", pixel_x, pixel_y, 4, 4)
            pixel_x += 5
            wall.append(pixel)
        pixel_y += 5
        pixel_x = 3


create_wall()


# creating ufos enemy objects
def create_ufos(speed):
    global ufos
    for x in range(0, 10):
        ufos.append(Ufo(screen, speed))


create_ufos(5)


def space_ship_movements():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if game.ship_position[0] < -19:
            pass
        else:
            game.ship_position[0] -= 3

    if key[pygame.K_RIGHT]:
        if game.ship_position[0] > 995:
            pass
        else:
            game.ship_position[0] += 3
    if key[pygame.K_q]:
        sys.exit()


def reset_game():
    global game_over, is_game_over
    if lives <= 1:
        game_over = "GAME OVER q=QUIT"
        is_game_over = True
    game.reset_game()
    ufos.clear()
    create_ufos(5)
    wall.clear()
    create_wall()


def level_up():
    global level
    level += 1
    global ufos_gun_start_speed
    ufos_gun_start_speed += 2
    create_ufos(ufos_gun_start_speed)
    wall.clear()
    create_wall()


collision_pixel_counter = 0

while True:
    game.background()
    game.space_ship()
    space_ship_movements()
    draw_pixels(wall)

    if len(ufos) == 0:
        level_up()

    for ufo in ufos:
        ufo.draw_ufo()

    for ufo in ufos:
        ufo.draw_gun(wall)

    gun.update(game.ship_position[1], game.ship_position[0])
    # check ship gun collision with wall
    for item in wall:
        if gun.rect[1] == -50:
            collision_pixel_counter = 0
        if pygame.Rect.colliderect(gun.rect, (item.x, item.y, item.width, item.height)):
            collision_pixel_counter += 1
            if collision_pixel_counter < random.choice([5, 6, 7, 8, 9, 10]):
                wall.remove(item)
            else:
                gun.start_y = -20

    # check gun collision with ufo
    for ufo in ufos:
        if pygame.Rect.colliderect(gun.rect, ufo.rect):
            if not is_game_over:
                ufos.remove(ufo)
                score += 1
                pass

    # check ufo gun collision with ship
    if not is_game_over:
        for ufo in ufos:
            if pygame.Rect.colliderect(ufo.gun_rect, game.ship_rect):
                reset_game()
                lives -= 1
                break

    game_over_text = my_font_2.render(f"{game_over}".format(screen), True, (255, 255, 0))
    screen.blit(game_over_text, (30, 200))

    score_text = my_font.render(f"Score:{score} Lives:{lives} Level:{level}".format(screen), True, (255, 255, 0))
    screen.blit(score_text, (5, 740))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
