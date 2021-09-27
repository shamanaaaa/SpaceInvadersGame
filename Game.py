import pygame


class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.ship_position = [512, 600]
        self.shot_start_x = 0
        self.shot_start_y = 0

    def background(self):
        self.image = pygame.image.load('images/background.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1024, 768))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]
        self.screen.blit(self.image, self.rect)

    def space_ship(self):
        self.ship = pygame.image.load('images/spaceship.png').convert_alpha()
        self.ship = pygame.transform.scale(self.ship, (50, 100))
        self.ship_rect = self.ship.get_rect()
        self.ship_rect.left, self.ship_rect.top = self.ship_position
        self.screen.blit(self.ship, self.ship_rect)

    def reset_game(self):
        self.ship_position = [512, 600]
        self.shot_start_x = 0
        self.shot_start_y = 0



