import pygame as pg
from pygame import mixer
from random import randrange, random

# Screen dimensions and layout configs
S_WIDTH = 600
S_HEIGHT = 400
TOP_MARGIN = 50
SIDE_MARGIN = 10

# Allow Area dimensions(where snake can move)
AREA_WIDTH = 580  # S_WIDTH-(MARGIN*2) = 580px
AREA_HEIGHT = 340 # S_HEIGHT-TOP_MARGIN-SIDE_MARGIN = 340px

# colors those used in game (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (25, 25, 25)
NEON_GREEN = (57, 255, 20)
LIGHT_GRAY = (200, 200, 200)

# Initialize mixer and load Sounds
mixer.init()
SNAKE_FX = mixer.Sound("Assets\\SnakeFX.mp3")
SNAKE_FX.set_volume(10)
EAT_FX = mixer.Sound("Assets\\EatFX.mp3")
EAT_FX.set_volume(0.3)
GAME_OVER_FX = mixer.Sound("Assets\\GameOverFX.mp3")

# Load images for foods and config them
APPLE_IMG = pg.image.load('Assets\\apple.jpg')
APPLE_IMG = pg.transform.scale(APPLE_IMG, (12, 12))

MANGO_IMG = pg.image.load('Assets\\mango.png')
MANGO_IMG = pg.transform.scale(MANGO_IMG, (12, 12))

# Define Font for Game
FONT = lambda size: pg.font.SysFont('Impact', size)

def show_score(score: int, top_score:int) -> None:
    """
    Displays the current score and top score on top-left of the screen.
    """
    txt = FONT(25).render(
        f"Score: {score} | TopScore: {top_score}",
                          True, WHITE)
    screen.blit(txt, (10, 10))

def draw_snake(snake_size: int, snake_pixels: list[list[int]]) -> None:
    """
    Draws the snake on the screen using a list of pixels.
    """
    for pixel in snake_pixels:
        center_x = pixel[0] + snake_size // 2
        center_y = pixel[1] + snake_size // 2
        radius = snake_size // 2
        pg.draw.circle(screen, NEON_GREEN, (center_x, center_y), radius)

def draw_area() -> None:
    """
    Draws the boundary of the game area.
    """
    pg.draw.rect(screen, DARK_GRAY,
                  [SIDE_MARGIN, TOP_MARGIN, AREA_WIDTH, AREA_HEIGHT], 0)

def random_food(snake_size: int) -> tuple:
    """
    Generates a random position for the food within the game area.
    """
    return(
        round(randrange(SIDE_MARGIN, 590-snake_size)/10)*10, # SIDE_MARGIN + AREA_WIDTH = 590
        round(randrange(TOP_MARGIN, 390-snake_size)/10)*10 # TOP_MARGIN + AREA_HEIGHT = 390
    )

def update_top_score(score: int) -> None:
    """
    Updates the top score if the current score is higher.
    """
    global top_score
    if score > top_score:
        top_score = score
    show_score(score, top_score)
       
def run_game() -> None:
    """
    Main function that runs the Snake game loop.
    Handles all logic for snake movement, collisions, food, scoring, etc...
    """
    score = 0

    # Snake configuration
    SNAKE_SIZE = 10
    SNAKE_SPEED = 14
    SNAKE_PIXELS = []
    SNAKE_LEN = 1

    # Speed increment logic: every 5 points, speed up by 2
    SPEED_INCREMENT_STEP = 5
    SPEED_STEP = 2
    NEXT_SPEED_INCREASE = SPEED_INCREMENT_STEP

    # Mango
    MANGO_ACTIVE = False            # Whether the mango is currently on-screen
    MANGO_SPAWN_TIME = 0            # When the mango was spawned
    MANGO_DURATION = 5000           # Mango remains for 5s(5000ms)
    MANGO_SPAWN_POSABILITY = 0.002  # Chance the mango spawns on any given frame update

    # Game state variables
    GAME_OVER = False
    GAME_CLOSE = False

    # Initial snake positions (somewhere in the allow area)
    X = 300  # S_WIDTH // 2 = 300
    Y = 200  # S_HEIGHT // 2 = 200
    X_SPEED = 0
    Y_SPEED = 0

    # Initial apple position
    APPLE_X, APPLE_Y = random_food(SNAKE_SIZE)

    # Play SnakeFX in a loop
    SNAKE_FX.play(-1)

    while not GAME_OVER:
        while GAME_CLOSE:
            # Display "Restart/Quit" screen
            screen.fill(BLACK)
            draw_area()

            msg = FONT(30).render("(R)Restart (Q)Quit", True, WHITE)
            # Position the message in the center of the game area
            # AREA_WIDTH // 2 = 290, AREA_HEIGHT // 2 = 170
            screen_center = msg.get_rect(center=(290, 170)) 
            screen.blit(msg, screen_center)

            # Show final score
            show_score(score, top_score)
            pg.display.update()

            # Handle restart or quit events
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:   #Quit
                        pg.quit()
                        return
                    elif event.key == pg.K_r: #Restart
                        return run_game()  
                elif event.type == pg.QUIT:
                    pg.quit()
                    return
        
        # Handle controls (keyboard events)
        for event in pg.event.get():
            if event.type == pg.QUIT: # Window close button
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and X_SPEED == 0:
                    # move left
                    X_SPEED = -SNAKE_SIZE
                    Y_SPEED = 0
                elif event.key == pg.K_RIGHT and X_SPEED == 0:
                    # move right    
                    X_SPEED = SNAKE_SIZE
                    Y_SPEED = 0
                elif event.key == pg.K_UP and Y_SPEED == 0:
                    # move up
                    X_SPEED = 0
                    Y_SPEED = -SNAKE_SIZE
                elif event.key == pg.K_DOWN and Y_SPEED == 0:
                    # move down
                    X_SPEED = 0
                    Y_SPEED = SNAKE_SIZE

        # Check snake collision with boundaries
        if X < SIDE_MARGIN or X >= 590 or Y < TOP_MARGIN or Y >= 390:
            SNAKE_FX.stop()
            GAME_OVER_FX.play()
            GAME_CLOSE = True

        # Update snake position
        X += X_SPEED
        Y += Y_SPEED

        # Reset the background
        screen.fill(BLACK)
        draw_area()

        # Draw the apple at its coordinates
        screen.blit(APPLE_IMG, (APPLE_X, APPLE_Y))

        # Mango spawning logic:
        # If mango isn't on screen but random() < spawn probability, spawn it
        if (not MANGO_ACTIVE) and (random() < MANGO_SPAWN_POSABILITY):
            MANGO_X, MANGO_Y = random_food(SNAKE_SIZE)
            MANGO_ACTIVE = True
            MANGO_SPAWN_TIME = pg.time.get_ticks()

        # If a mango is active, draw it until the time limit expires
        if MANGO_ACTIVE:
            # Draw the mango at its coordinates
            screen.blit(MANGO_IMG, (MANGO_X, MANGO_Y))
            # Remove mango after MANGO_DURATION(5s)
            if pg.time.get_ticks() - MANGO_SPAWN_TIME > MANGO_DURATION:
                MANGO_ACTIVE = False

        # Update snake body list
        SNAKE_PIXELS.append([int(X), int(Y)])
        if len(SNAKE_PIXELS) > SNAKE_LEN:
            del SNAKE_PIXELS[0]
            
        # Check if the snake collided with itself 
        for pixel in SNAKE_PIXELS[:-1]:
            if pixel == [int(X), int(Y)]:
                SNAKE_FX.stop()
                GAME_OVER_FX.play()
                GAME_CLOSE = True

        # Draw the snake on the screen
        draw_snake(SNAKE_SIZE, SNAKE_PIXELS)

        # Update and display the scores
        score = SNAKE_LEN-1
        update_top_score(score)

        # Increase snake speed in increments 
        if score >= NEXT_SPEED_INCREASE:
            SNAKE_SPEED += SPEED_STEP
            NEXT_SPEED_INCREASE += SPEED_INCREMENT_STEP
            
        # Update the Pygame display fully
        pg.display.update()

        if int(X) == APPLE_X and int(Y) == APPLE_Y:
            EAT_FX.play() # Play the eat sound effect
            # Draw the apple at its coordinates again
            APPLE_X, APPLE_Y = random_food(SNAKE_SIZE)
            SNAKE_LEN += 1

        # Check if the snake eats the mango
        if MANGO_ACTIVE:
            if int(X) == MANGO_X and int(Y) == MANGO_Y:
                EAT_FX.play()
                score += 3       # Increase score by +3 for rare mango
                SNAKE_LEN += 3   # Snake grow
                MANGO_ACTIVE = False # Mango gets consumed

        # FPS
        clock.tick(SNAKE_SPEED)


if __name__ == "__main__":
    pg.init() # Initialize the pygame
    screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
    pg.display.set_caption("Snake Game")
    
    clock = pg.time.Clock()
    top_score = 0

    run_game()
