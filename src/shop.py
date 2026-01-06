def draw_shop(screen, font, player, draw_text):
    screen.fill((20, 20, 40))

    draw_text(screen, "SHOP", 40, 40, font)
    draw_text(screen, f"Credits: {player.credits}", 40, 80, font)

    draw_text(screen, "1 - Upgrade Damage (+2) [20 credits]", 40, 140, font)
    draw_text(screen, "2 - Upgrade Fire Rate [30 credits]", 40, 180, font)
    draw_text(screen, "3 - Upgrade Health (+20) [25 credits]", 40, 220, font)

    draw_text(screen, "ESC - Voltar ao jogo", 40, 300, font)


def handle_shop_input(player):
    import pygame
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1] and player.credits >= 20:
        player.credits -= 20
        player.upgrade_damage()

    if keys[pygame.K_2] and player.credits >= 30:
        player.credits -= 30
        player.upgrade_fire_rate()

    if keys[pygame.K_3] and player.credits >= 25:
        player.credits -= 25
        player.upgrade_health()
