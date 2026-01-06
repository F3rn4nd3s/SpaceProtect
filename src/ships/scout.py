from ship import Ship
import pygame

class ScoutShip(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.image.fill((120, 220, 255))

        self.speed = 8
        self.max_health = 70
        self.health = self.max_health
        self.fire_rate = 200
        self.damage = 8
