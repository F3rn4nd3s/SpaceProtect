import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, health, color):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = speed
        self.health = health

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 700:
            self.kill()

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

# TIPOS DE INIMIGOS

class ScouterEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            speed=4,
            health=20,
            color=(180, 255, 180)
        )


class FighterEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            speed=2,
            health=40,
            color=(255, 180, 180)
        )


class KamikazeEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            speed=6,
            health=15,
            color=(255, 120, 120)
        )

    def update(self):
        self.rect.y += self.speed
        self.rect.x += random.choice([-2, 0, 2])

        if self.rect.top > 700:
            self.kill()
