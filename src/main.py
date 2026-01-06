import pygame
import sys
import random

from ship import Ship
from enemy import ScouterEnemy, FighterEnemy, KamikazeEnemy
from bullet import Bullet
from audio import AudioManager
from shop import draw_shop, handle_shop_input

# CONFIGURAÇÕES GERAIS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Estados do jogo
MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"
STATE_PLAYING = "playing"
STATE_GAME_OVER = "game_over"
STATE_SHOP = "shop"

# DEFINIÇÃO DAS NAVES
SHIP_TYPES = [
    {
        "name": "Fighter",
        "speed": 5,
        "health": 100,
        "fire_rate": 400,
        "damage": 12,
        "color": (120, 180, 255)
    },
    {
        "name": "Scouter",
        "speed": 7,
        "health": 70,
        "fire_rate": 300,
        "damage": 9,
        "color": (180, 255, 180)
    },
    {
        "name": "Tank",
        "speed": 3,
        "health": 160,
        "fire_rate": 700,
        "damage": 8,
        "color": (255, 180, 180)
    }
]


def draw_text(surface, text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, rect)


def ship_selection_menu(screen, clock):
    selected_index = 0

    while True:
        clock.tick(FPS)
        screen.fill((10, 10, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and game_state == STATE_PLAYING:
                    game_state = STATE_SHOP

                elif event.key == pygame.K_ESCAPE:
                        if game_state == STATE_SHOP:
                            game_state = STATE_PLAYING
                        else:
                            running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(SHIP_TYPES)

                if event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(SHIP_TYPES)

                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return SHIP_TYPES[selected_index]

        draw_text(screen, "ESCOLHA SUA NAVE", 48, SCREEN_WIDTH // 2, 80)

        for i, ship in enumerate(SHIP_TYPES):
            x = SCREEN_WIDTH // 2 + (i - selected_index) * 220
            y = SCREEN_HEIGHT // 2

            rect = pygame.Rect(0, 0, 120, 80)
            rect.center = (x, y)

            pygame.draw.rect(screen, ship["color"], rect)

            draw_text(screen, ship["name"], 28, x, y - 70)
            draw_text(screen, f"Vida: {ship['health']}", 20, x, y + 60)
            draw_text(screen, f"Vel: {ship['speed']}", 20, x, y + 80)
            draw_text(screen, f"Dano: {ship['damage']}", 20, x, y + 100)

            if i == selected_index:
                pygame.draw.rect(screen, (255, 255, 255), rect, 3)

        draw_text(
            screen,
            "← → escolher | ENTER ou ESPAÇO iniciar | ESC sair",
            22,
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 40
        )

        pygame.display.flip()

def draw_shop(screen, font, player):
    screen.fill((20, 20, 40))

    draw_text(screen, "SHOP", 40, 40, font)
    draw_text(screen, f"Credits: {player.credits}", 40, 80, font)

    draw_text(screen, "1 - Upgrade Damage (+2) [20 credits]", 40, 140, font)
    draw_text(screen, "2 - Upgrade Fire Rate [30 credits]", 40, 180, font)
    draw_text(screen, "3 - Upgrade Health (+20) [25 credits]", 40, 220, font)

    draw_text(screen, "ESC - Voltar ao jogo", 40, 300, font)

def main():
    
    pygame.init()
    pygame.mixer.init()

    font = pygame.font.SysFont("arial", 20)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SpaceProtect")
    clock = pygame.time.Clock()

    audio = AudioManager()

    # MENU DE SELEÇÃO
    ship_data = ship_selection_menu(screen, clock)

    # GRUPOS
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    enemy_spawn_timer = 0
    ENEMY_SPAWN_DELAY = 1200  # milissegundos


    player = Ship(
        x=SCREEN_WIDTH // 2,
        y=SCREEN_HEIGHT - 80,
        speed=ship_data["speed"],
        health=ship_data["health"],
        fire_rate=ship_data["fire_rate"],
        damage=ship_data["damage"]
    )

    player.image.fill(ship_data["color"])
    all_sprites.add(player)

    state = PLAYING
    game_state = STATE_PLAYING

    def draw_health_bar(surface, x, y, width, height, current, maximum):
        ratio = max(current / maximum, 0)
        pygame.draw.rect(surface, (200, 0, 0), (x, y, width, height))
        pygame.draw.rect(surface, (0, 200, 0), (x, y, width * ratio, height))
        pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height), 2)


    def draw_text(surface, text, x, y, font):
        text_surface = font.render(text, True, (255, 255, 255))
        surface.blit(text_surface, (x, y))

    # LOOP PRINCIPAL
    while True:
        clock.tick(FPS)

        current_time = pygame.time.get_ticks()

        if current_time - enemy_spawn_timer > ENEMY_SPAWN_DELAY:
            enemy_spawn_timer = current_time

            enemy_type = random.choice([
                ScouterEnemy,
                FighterEnemy,
                FighterEnemy,
                KamikazeEnemy
            ])

            enemy = enemy_type(
                x=random.randint(40, SCREEN_WIDTH - 40),
                y=-30
            )

            enemies.add(enemy)
            all_sprites.add(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if state == PLAYING and event.key == pygame.K_SPACE:
                    player.shoot(bullets, Bullet, audio)

        if state == PLAYING:
            all_sprites.update()
            bullets.update()
            enemies.update()

            # Colisão com inimigos
            if pygame.sprite.spritecollide(player, enemies, True):
                player.take_damage(20)
                if player.health <= 0:
                    state = GAME_OVER

            if game_state == STATE_SHOP:
                draw_shop(screen, font, player, draw_text)
                handle_shop_input(player)

                pygame.display.flip()
                clock.tick(60)
                continue

        screen.fill((20, 20, 40))
        all_sprites.draw(screen)
        bullets.draw(screen)
        enemies.draw(screen)

        # HUD
        draw_health_bar(
            screen,
            x=20,
            y=20,
            width=200,
            height=20,
            current=player.health,
            maximum=player.max_health
        )

        draw_text(
            screen, 
            f"XP: {player.xp}",
            x=20,
            y=50,
            font=font
        )

        draw_text(
            screen,
            f"Credits: {player.credits}",
            x=20,
            y=75,
            font=font
        )


        hits = pygame.sprite.groupcollide(
            enemies,
            bullets,
            False,  # inimigo NÃO morre automaticamente
            True    # bala sempre some
        )

        for enemy, bullets_hit in hits.items():
            for bullet in bullets_hit:
                enemy.take_damage(bullet.damage)

            if not enemy.alive():
                player.gain_xp(10)
                player.gain_credits(5)

        if state == GAME_OVER:
            draw_text(
                screen,
                "GAME OVER",
                SCREEN_WIDTH // 2 - 80,
                SCREEN_HEIGHT // 2 - 20,
                font
            )
            draw_text(
                screen,
                "ESC para sair",
                SCREEN_WIDTH // 2 - 70,
                SCREEN_HEIGHT // 2 + 40,
                font
            )

        pygame.display.flip()


if __name__ == "__main__":
    main()
