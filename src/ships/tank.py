from ship import Ship
import pygame

class TankShip(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.image = pygame.Surface((60, 50))
        self.image.fill((200, 200, 80))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 4
        self.max_health = 160
        self.health = self.max_health
        self.fire_rate = 450
        self.damage = 14
