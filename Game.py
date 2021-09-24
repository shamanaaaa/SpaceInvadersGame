import pygame


class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.ship_position = [512, 512]

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

    def space_ship_gun(self):
        self.gun = pygame.image.load('images/spaceship.png').convert_alpha()
        self.gun = pygame.transform.scale(self.gun, (5, 40))
        self.gun_rect = self.gun.get_rect()

    def shot(self):
        self.gun_rect.left, self.gun_rect.top = self.ship_position
        self.screen.blit(self.gun, self.gun_rect)
