import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, damage):
        super().__init__()

        self.image = pygame.Surface((6, 14))
        self.image.fill((255, 230, 120))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = -10
        self.damage = damage

    def update(self):
        self.rect.y += self.speed

        if self.rect.bottom < 0:
            self.kill()
