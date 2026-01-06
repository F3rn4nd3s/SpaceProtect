import pygame
import time

class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, health, fire_rate, damage):
        super().__init__()

        self.image = pygame.Surface((50, 40))
        self.image.fill((100, 200, 255))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = speed
        self.health = health
        self.max_health = health
        self.damage = damage

        self.fire_rate = fire_rate
        self.last_shot_time = 0

        self.xp = 0
        self.credits = 0

    def update(self):
        keys = pygame.key.get_pressed()

        # MOVIMENTO HORIZONTAL
        if (
            keys[pygame.K_a] or
            keys[pygame.K_LEFT] or
            keys[pygame.K_KP4]
        ):
            self.rect.x -= self.speed

        if (
            keys[pygame.K_d] or
            keys[pygame.K_RIGHT] or
            keys[pygame.K_KP6]
        ):
            self.rect.x += self.speed

        # MOVIMENTO VERTICAL
        if (
            keys[pygame.K_w] or
            keys[pygame.K_UP] or
            keys[pygame.K_KP8]
        ):
            self.rect.y -= self.speed

        if (
            keys[pygame.K_s] or
            keys[pygame.K_DOWN] or
            keys[pygame.K_KP2]
        ):
            self.rect.y += self.speed

        # LIMITES DA TELA
        screen = pygame.display.get_surface()
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(screen.get_width(), self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(screen.get_height(), self.rect.bottom)

    def shoot(self, bullets_group, bullet_class, audio=None):
        current_time = time.time() * 1000
        if current_time - self.last_shot_time >= self.fire_rate:
            bullet = bullet_class(
                self.rect.centerx,
                self.rect.top,
                self.damage
            )
            bullets_group.add(bullet)
            self.last_shot_time = current_time

            if audio:
                audio.play_sound("shoot")

    def take_damage(self, amount):
        self.health -= amount

    def gain_xp(self, amount):
        self.xp += amount

    def gain_credits(self, amount):
        self.credits += amount
    def upgrade_damage(self):
        self.damage += 2

    def upgrade_fire_rate(self):
        if self.fire_rate > 150:
            self.fire_rate -= 50

    def upgrade_health(self):
        self.max_health += 20
        self.health += 20
