from ship import Ship
import pygame

class FighterShip(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.image.fill((80, 200, 120))

        self.speed = 6
        self.max_health = 100
        self.health = self.max_health
        self.fire_rate = 300
        self.damage = 10
