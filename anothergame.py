import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player settings
player_size = (40, 60)
player_x, player_y = 50, HEIGHT - player_size[1] - 50
player_speed = 5
player_jump = -15
player_velocity_y = 0
gravity = 0.8
on_ground = False

# Platforms
platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),  # Ground
    pygame.Rect(200, 300, 100, 20),
    pygame.Rect(400, 250, 100, 20),
    pygame.Rect(600, 200, 100, 20),
]

# Main game loop
def main():
    global player_x, player_y, player_velocity_y, on_ground

    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE] and on_ground:
            player_velocity_y = player_jump
            on_ground = False

        # Gravity
        player_velocity_y += gravity
        player_y += player_velocity_y

        # Player rectangle
        player_rect = pygame.Rect(player_x, player_y, *player_size)

        # Collision detection
        on_ground = False
        for platform in platforms:
            if player_rect.colliderect(platform) and player_velocity_y > 0:
                player_y = platform.top - player_size[1]
                player_velocity_y = 0
                on_ground = True

        # Draw platforms
        for platform in platforms:
            pygame.draw.rect(screen, BLUE, platform)

        # Draw player
        pygame.draw.rect(screen, RED, player_rect)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    # Adjust screen size and scale
    WIDTH, HEIGHT = 4000, 2000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Platformer Game - Expanded")

    # Adjust player size and speed
    player_size = (200, 300)
    player_x, player_y = 250, HEIGHT - player_size[1] - 250
    player_speed = 25
    player_jump = -75
    gravity = 4

    # Adjust platforms
    platforms = [
        pygame.Rect(0, HEIGHT - 250, WIDTH, 250),  # Ground
        pygame.Rect(1000, 1500, 500, 100),
        pygame.Rect(2000, 1200, 500, 100),
        pygame.Rect(3000, 900, 500, 100),
        pygame.Rect(1500, 600, 500, 100),
        pygame.Rect(2500, 300, 500, 100),
    ]

    def main():
        global player_x, player_y, player_velocity_y, on_ground

        running = True
        while running:
            screen.fill(WHITE)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Key handling
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
            if keys[pygame.K_RIGHT]:
                player_x += player_speed
            if keys[pygame.K_SPACE] and on_ground:
                player_velocity_y = player_jump
                on_ground = False

            # Gravity
            player_velocity_y += gravity
            player_y += player_velocity_y

            # Player rectangle
            player_rect = pygame.Rect(player_x, player_y, *player_size)

            # Collision detection
            on_ground = False
            for platform in platforms:
                if player_rect.colliderect(platform) and player_velocity_y > 0:
                    player_y = platform.top - player_size[1]
                    player_velocity_y = 0
                    on_ground = True

            # Check if player falls off the screen
            if player_y > HEIGHT:
                print("You died!")
                running = False

            # Draw platforms
            for platform in platforms:
                pygame.draw.rect(screen, BLUE, platform)

            # Draw player
            pygame.draw.rect(screen, RED, player_rect)

            # Update display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(60)

        pygame.quit()
        sys.exit()

    # Enable full screen mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()

    # Adjust player and platform positions for the new screen size
    player_x, player_y = 250, HEIGHT - player_size[1] - 250
    platforms = [
        pygame.Rect(0, HEIGHT - 250, WIDTH * 2, 250),  # Ground
        pygame.Rect(1000, 1500, 500, 100),
        pygame.Rect(2000, 1200, 500, 100),
        pygame.Rect(3000, 900, 500, 100),
        pygame.Rect(1500, 600, 500, 100),
        pygame.Rect(2500, 300, 500, 100),
    ]

    def main():
        global player_x, player_y, player_velocity_y, on_ground

        camera_x = 0  # Camera offset
        running = True
        while running:
            screen.fill(WHITE)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass

            # Key handling
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
            if keys[pygame.K_RIGHT]:
                player_x += player_speed
            if keys[pygame.K_SPACE] and on_ground:
                player_velocity_y = player_jump
                on_ground = False

            # Gravity
            player_velocity_y += gravity
            player_y += player_velocity_y

            # Player rectangle
            player_rect = pygame.Rect(player_x, player_y, *player_size)

            # Collision detection
            on_ground = False
            for platform in platforms:
                if player_rect.colliderect(platform) and player_velocity_y > 0:
                    player_y = platform.top - player_size[1]
                    player_velocity_y = 0
                    on_ground = True

            # Check if player falls off the screen
            if player_y > HEIGHT:
                print("You died!")
                running = False

            # Camera movement
            if player_x - camera_x > WIDTH * 0.7:
                camera_x = player_x - WIDTH * 0.7
            elif player_x - camera_x < WIDTH * 0.3:
                camera_x = player_x - WIDTH * 0.3

            # Draw platforms
            for platform in platforms:
                pygame.draw.rect(screen, BLUE, platform.move(-camera_x, 0))

            # Draw player
            pygame.draw.rect(screen, RED, player_rect.move(-camera_x, 0))

            # Update display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(60)

        pygame.quit()
        sys.exit()

    import os

    # Load background image
    try:
        background = pygame.image.load("background.jpg")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    except pygame.error:
        print("Error: 'background.jpg' not found. Using a white background.")
        background = pygame.Surface((WIDTH, HEIGHT))
        background.fill(WHITE)

    # Load player image
    try:
        player_image = pygame.image.load("player.png")
        player_image = pygame.transform.scale(player_image, player_size)
    except pygame.error:
        print("Error: 'player.png' not found. Using a red rectangle as the player.")
        player_image = pygame.Surface(player_size)
        player_image.fill(RED)

    # Load platform image
    try:
        platform_image = pygame.image.load("platform.png")
        platform_image = pygame.transform.scale(platform_image, (500, 100))
    except pygame.error:
        print("Error: 'platform.png' not found. Using a blue rectangle as the platform.")
        platform_image = pygame.Surface((500, 100))
        platform_image.fill(BLUE)

    def draw_platforms():
        for platform in platforms:
            platform_rect = platform.move(-camera_x, 0)
            screen.blit(platform_image, platform_rect)

    def draw_player():
        player_rect = pygame.Rect(player_x, player_y, *player_size)
        screen.blit(player_image, player_rect.move(-camera_x, 0))

    def main():
        global player_x, player_y, player_velocity_y, on_ground

        camera_x = 0  # Camera offset
        running = True
        while running:
            screen.blit(background, (0, 0))

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Key handling
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
            if keys[pygame.K_RIGHT]:
                player_x += player_speed
            if keys[pygame.K_SPACE] and on_ground:
                player_velocity_y = player_jump
                on_ground = False

            # Gravity
            player_velocity_y += gravity
            player_y += player_velocity_y

            # Player rectangle
            player_rect = pygame.Rect(player_x, player_y, *player_size)

            # Collision detection
            on_ground = False
            for platform in platforms:
                if player_rect.colliderect(platform) and player_velocity_y > 0:
                    player_y = platform.top - player_size[1]
                    player_velocity_y = 0
                    on_ground = True

            # Check if player falls off the screen
            if player_y > HEIGHT:
                print("You died!")
                running = False

            # Camera movement
            if player_x - camera_x > WIDTH * 0.7:
                camera_x = player_x - WIDTH * 0.7
            elif player_x - camera_x < WIDTH * 0.3:
                camera_x = player_x - WIDTH * 0.3

            # Draw platforms and player
            draw_platforms()
            draw_player()

            # Update display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(60)

        pygame.quit()
        sys.exit()

    main()