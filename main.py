import pygame
import random
import math

pygame.init()

# Define the window size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# Set up the window display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("A Groovy Town 3")
rand_green = random.randint(160, 210)
rand_blue = random.randint(160, 175)

# Create a surface for the side panel
SIDE_PANEL_WIDTH = 200
side_panel_size = (SIDE_PANEL_WIDTH, SCREEN_HEIGHT)
side_panel = pygame.Surface(side_panel_size)
side_panel.fill((230, rand_green-5, rand_blue)) # fill the panel with white

#Set the game elements
score = 0

# Define the square position and size
player_x = 100
player_y = 100
player_size = 50

# Set up the enemy square
enemy_size = 50
enemy_x = random.randint(0, SCREEN_WIDTH - SIDE_PANEL_WIDTH - enemy_size)
enemy_y = random.randint(0, SCREEN_HEIGHT - enemy_size)
enemy_speed = 0.2

# Set the movement speed
vel = 1

# Set up the text
font = pygame.font.Font(None, 36)
score_text = font.render("Score : " + str(score), True, (0, 0, 0))
text_rect = score_text.get_rect()
text_rect.center = (900, 200)


# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
game_over = False

#Fuel controls
fuel_radius = 8

def fuel_pop():
    global fuel_x 
    fuel_x = random.randint(fuel_radius, SCREEN_WIDTH - SIDE_PANEL_WIDTH - fuel_radius)
    global fuel_y 
    fuel_y = random.randint(fuel_radius, SCREEN_HEIGHT - fuel_radius)
    
fuel_pop()

while not game_over:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Check for keyboard inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= vel
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - SIDE_PANEL_WIDTH - player_size:
        player_x += vel
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= vel
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
        player_y += vel
        
    # Move the enemy square towards the player
    if enemy_x < player_x:
        enemy_x += enemy_speed
    elif enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    elif enemy_y > player_y:
        enemy_y -= enemy_speed
        
    # Check for collision between player and enemy squares
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    fuel = pygame.Rect(fuel_x, fuel_y, (2*fuel_radius)/math.sqrt(2), (2*fuel_radius)/math.sqrt(2))
    
    if player_rect.colliderect(enemy_rect):
        game_over = True
        
    if player_rect.colliderect(fuel):
        score = score + 1
        score_text = font.render("Score : " + str(score), True, (0, 0, 0))
        fuel_pop()

    # Fill the screen with black
    screen.fill((255, rand_green, rand_blue))
    
    # Draw the square
    fuel = pygame.draw.circle(screen, (0, 0, 0), (fuel_x, fuel_y), fuel_radius)
    pygame.draw.rect(screen, (255, 100, 100), (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, (0, 100, 255), (enemy_x, enemy_y, enemy_size, enemy_size))
    
    # Blit the side panel onto the main game surface
    screen.blit(side_panel, (800, 0))
    screen.blit(score_text, text_rect)
    
    # Update the screen
    pygame.display.update()

pygame.quit()