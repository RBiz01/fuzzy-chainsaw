import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions for vertical phone orientation
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1280

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Angry Tanks")

# Load tank and ammo images (user needs to provide colorful images)
player_ammo_image = pygame.image.load("angry_tanks/Images/player_ammo.png")  # Replace with ammo image
enemy_target_image = pygame.image.load("angry_tanks/Images/enemy_target.png")    # Replace with enemy image (e.g., pigs or enemy bases)

# Load background image (use a colorful, beautiful background)
background_image = pygame.image.load("angry_tanks/Images/background.png")  # Replace with beautiful background

# Scale the background image to fit the screen dimensions
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# TankAmmo class (replaces Bird, but functions like projectiles in Angry Birds)
class TankAmmo(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = [0, 0]
        self.dragging = False
        self.drag_start_pos = (0, 0)
        self.gravity = 0.5  # Add gravity for projectile motion like Angry Birds

    def update(self):
        if self.dragging:
            mouse_pos = pygame.mouse.get_pos()
            self.rect.centerx = mouse_pos[0]
            self.rect.centery = mouse_pos[1]
        else:
            self.velocity[1] += self.gravity  # Apply gravity
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

    def start_drag(self):
        self.dragging = True
        self.drag_start_pos = self.rect.center

    def end_drag(self):
        self.dragging = False
        mouse_pos = pygame.mouse.get_pos()
        direction = math.atan2(self.drag_start_pos[1] - mouse_pos[1], self.drag_start_pos[0] - mouse_pos[0])
        speed = 20  # Increased speed for better projection
        self.velocity = [speed * math.cos(direction), speed * math.sin(direction)]

    def hit_enemy(self):
        global score
        score += 100  # Increase the score by 100 when an enemy is hit

# Button class
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, action):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.action = action

# Create player ammo (starts from a "tank" position at bottom left)
player_ammo = TankAmmo(100, SCREEN_HEIGHT - 200, player_ammo_image)

# Function to spawn enemies for a level
def spawn_enemies(level):
    enemies = pygame.sprite.Group()
    num_enemies = 3 + level  # Increase enemies per level
    for _ in range(num_enemies):
        x = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH - 50)
        y = random.randint(SCREEN_HEIGHT // 4, SCREEN_HEIGHT - 50)  # Spread vertically
        enemy = TankAmmo(x, y, enemy_target_image)  # Use same class for simplicity, but stationary
        enemy.velocity = [0, 0]  # Enemies are stationary like pigs
        enemies.add(enemy)
    return enemies

# Initial level
current_level = 1
enemy_targets = spawn_enemies(current_level)

# Calculating button positions
button_margin = 10
button_top = button_margin
button_left = button_margin
button_spacing = 5

# Initialize player's score
score = 0

# Calculate score position (adjusted for vertical screen)
score_position = (SCREEN_WIDTH - 200, 80)

# Create buttons (use colorful button images)
quit_button_image = pygame.image.load("angry_tanks/Images/quit_button.png")        # Replace path if needed
refresh_button_image = pygame.image.load("angry_tanks/Images/refresh_button.png")  # Replace path if needed

quit_button = Button(button_left, button_top, quit_button_image, "quit")
refresh_button = Button(button_left + quit_button_image.get_width() + button_spacing, button_top, refresh_button_image, "refresh")

# Game loop
clock = pygame.time.Clock()

# Initialize game state
try_again_counter = 0
max_try_again = 3
level_cleared = False
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.rect.collidepoint(event.pos):
                # Quit button clicked - exit the game
                pygame.quit()
                sys.exit()

            elif refresh_button.rect.collidepoint(event.pos):
                # Refresh button clicked - reset game
                player_ammo.rect.center = (100, SCREEN_HEIGHT - 200)  # Reset player ammo position
                player_ammo.velocity = [0, 0]
                enemy_targets = spawn_enemies(current_level)
                # Reset flags
                level_cleared = False
                game_over = False
                try_again_counter = 0
                score = 0
                current_level = 1

            elif player_ammo.rect.collidepoint(event.pos):
                # Player ammo clicked - start dragging (simulate aiming from tank)
                player_ammo.start_drag()

        elif event.type == pygame.MOUSEBUTTONUP:
            if player_ammo.dragging:
                # Release the player ammo
                player_ammo.end_drag()
                hits = pygame.sprite.spritecollide(player_ammo, enemy_targets, False)
                if not hits:
                    try_again_counter += 1  # Increment try_again_counter when no hits occur

    # Update enemy positions and collisions (enemies are stationary)
    hits = pygame.sprite.spritecollide(player_ammo, enemy_targets, True)

    if hits:
        for hit_enemy in hits:
            hit_enemy.hit_enemy()  # Call hit_enemy method to update score

    # Reset player ammo to origin position if it goes out of the screen
    if player_ammo.rect.left > SCREEN_WIDTH or player_ammo.rect.right < 0 or \
            player_ammo.rect.top > SCREEN_HEIGHT or player_ammo.rect.bottom < 0:
        player_ammo.rect.center = (100, SCREEN_HEIGHT - 200)
        player_ammo.velocity = [0, 0]

    # Check if all enemies are destroyed
    if len(enemy_targets) == 0:
        level_cleared = True

    # Clear the screen and draw the background
    screen.blit(background_image, (0, 0))

    # Update and draw player ammo
    player_ammo.update()
    screen.blit(player_ammo.image, player_ammo.rect)

    # Draw enemy targets
    enemy_targets.draw(screen)

    # Display font
    font = pygame.font.Font(None, 50)
    level_font = pygame.font.Font(None, 36)

    # Draw and update player's score and level
    score_text = level_font.render(f"Score: {score}", True, (0, 0, 0))
    level_text = level_font.render(f"Level: {current_level}", True, (0, 0, 0))
    screen.blit(score_text, score_position)
    screen.blit(level_text, (score_position[0], score_position[1] + 40))

    # Draw buttons
    screen.blit(quit_button.image, quit_button.rect)
    screen.blit(refresh_button.image, refresh_button.rect)

    # Display "Level Cleared" and advance level
    if level_cleared:
        level_cleared_text = font.render("LEVEL CLEARED", True, (0, 0, 0))
        text_rect = level_cleared_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(level_cleared_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait 2 seconds
        current_level += 1
        enemy_targets = spawn_enemies(current_level)
        player_ammo.rect.center = (100, SCREEN_HEIGHT - 200)
        player_ammo.velocity = [0, 0]
        level_cleared = False

    # Display "Game Over" if too many misses
    if try_again_counter >= max_try_again:
        game_over_text = font.render("GAME OVER - REPLAY", True, (0, 0, 0))
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
        game_over = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
