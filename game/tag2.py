import pygame
import os
import random

# Create our Main Surface
WIDTH, HEIGHT = 1200, 800  # Define Width and Height as a Tuple
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the surface
pygame.display.set_caption("Play Tag!")  # Label the window with game name


# Color Pallette
GRASS_GREEN = (20, 50, 50)

# Sprites
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 40
DEER_SPRITE = pygame.image.load(os.path.join('Assets', 'deerbitmap.png'))
DEER = pygame.transform.scale(DEER_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))

WOLF_SPRITE = pygame.image.load(os.path.join('Assets', 'wolfbitmap.png'))
WOLF = pygame.transform.scale(WOLF_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))

# Define
FPS = 60

# User Events
CAUGHT = pygame.USEREVENT + 1

# Game Parameters
SPEED = random.randint(2,6) # they move at random speeds
SPEED2 = random.randint(2,6)


# Define a main function that runs the game
def main():
    # Create hit boxes
    deer = pygame.Rect(random.randint(1,1200), random.randint(1,800), SPRITE_WIDTH, SPRITE_HEIGHT)
    wolf = pygame.Rect(random.randint(1,1200), random.randint(1,800), SPRITE_WIDTH, SPRITE_HEIGHT)

    clock = pygame.time.Clock()
    run = True  # set run to True
    # While loop that runs the game
    while run:  # Game Loop
        clock.tick(FPS)
        for event in pygame.event.get():  # Checks for EVENTS
            if event.type == pygame.QUIT:  # if close clicked
                run = False  # change run to False to break loop

            if event.type == CAUGHT:
                run = False
                print('GOTCHA')

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and deer.x - SPEED > 50:  # Deer Left
            deer.x -= SPEED + random.randint(1,30)
        if keys_pressed[pygame.K_d] and deer.x + SPEED + SPRITE_WIDTH < 1150:  # Deer Right
            deer.x += SPEED + random.randint(1,30)
        if keys_pressed[pygame.K_w] and deer.y - SPEED > 50:  # Deer Up
            deer.y -= SPEED + random.randint(1,30)
        if keys_pressed[pygame.K_s] and deer.y + SPEED + SPRITE_HEIGHT < 750:  # Deer Down
            deer.y += SPEED + random.randint(1,30)

        if keys_pressed[pygame.K_LEFT] and wolf.x - SPEED2 > 50:  # Wolf Left
            wolf.x -= SPEED2 + random.randint(1,30)
        if keys_pressed[pygame.K_RIGHT] and wolf.x + SPEED2 + SPRITE_WIDTH < 1150:  # Wolf Right
            wolf.x += SPEED2 + random.randint(1,30)
        if keys_pressed[pygame.K_UP] and wolf.y - SPEED2 > 50:  # Wolf Up
            wolf.y -= SPEED2 + random.randint(1,30)
        if keys_pressed[pygame.K_DOWN] and wolf.y + SPEED2 + SPRITE_HEIGHT < 750:  # Wolf Down
            wolf.y += SPEED2 + random.randint(1,30)

        draw_window(deer, wolf)  # This function draws the screen
        deer_tagged(deer, wolf)  # Check if tagged


    pygame.quit()  # will close game


# Draw Window Function
def draw_window(deer, wolf):
    WIN.fill(GRASS_GREEN)  # Draw the Grass
    WIN.blit(DEER, (deer.x, deer.y))  # Sprites
    WIN.blit(WOLF, (wolf.x, wolf.y))  # Sprites
    pygame.display.update()  # Update the screen


# Create a function to determine if tagged
def deer_tagged(deer, wolf):
    if deer.colliderect(wolf):
        pygame.event.post(pygame.event.Event(CAUGHT))


if __name__ == "__main__":
    main()