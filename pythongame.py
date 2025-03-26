import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Shooting Overhead Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_size = 50
player_speed = 5
player = pygame.Rect(WIDTH // 2, HEIGHT - player_size - 10, player_size, player_size)

# Bullet settings
bullet_size = 10
bullet_speed = -7
bullets = []

# Enemy settings
enemy_size = 50
enemy_speed = 3
enemies = []
enemy_spawn_time = 30  # Frames between enemy spawns
enemy_timer = 0

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=WHITE):
    """Draw text on the screen."""
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit the number of bullets on screen
            bullets.append(pygame.Rect(player.centerx - bullet_size // 2, player.top, bullet_size, bullet_size))

    # Update bullets
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Spawn enemies
    enemy_timer += 1
    if enemy_timer >= enemy_spawn_time:
        enemy_timer = 0
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemies.append(pygame.Rect(enemy_x, 0, enemy_size, enemy_size))

    # Update enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.top > HEIGHT:
            enemies.remove(enemy)
        # Check for collision with player
        if enemy.colliderect(player):
            running = False

    # Check for bullet collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Draw player
    pygame.draw.rect(screen, GREEN, player)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Draw score
    draw_text(f"Score: {score}", 10, 10)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()