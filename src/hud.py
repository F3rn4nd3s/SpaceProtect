import pygame

class HUD:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 20)

    def draw(self, screen, player):
        texts = [
            f"Vida: {player.health}/{player.max_health}",
            f"Nível: {player.level}",
            f"XP: {player.xp}/{player.xp_to_next_level}",
            f"Créditos: {player.credits}"
        ]

        for i, text in enumerate(texts):
            surface = self.font.render(text, True, (255, 255, 255))
            screen.blit(surface, (10, 10 + i * 25))
