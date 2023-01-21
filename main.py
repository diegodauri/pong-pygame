import pygame
import random

# Initialize window constants
WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)

# Initialize pygame and the screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize the fonts for the counter, game over and play again texts
counter_font = pygame.font.SysFont(None, 48)
game_over_font = pygame.font.SysFont(None, 100)
play_again_font = pygame.font.SysFont(None, 70)

# Create the tile rect
tile = pygame.Rect(0, HEIGHT - 15, 150, 15)

# Generates 3 balls
ball1_image = pygame.image.load("small_tennis.png")
ball1_rect = ball1_image.get_rect()
ball1_speed = [random.uniform(-4, 4), random.uniform(1, 4)]
ball1_alive = True

ball2_image = pygame.image.load("small_tennis.png")
ball2_rect = ball2_image.get_rect()
ball2_speed = [random.uniform(-4, 4), random.uniform(1, 4)]
ball2_alive = True

ball3_image = pygame.image.load("small_tennis.png")
ball3_rect = ball3_image.get_rect()
ball3_speed = [random.uniform(-4, 4), random.uniform(1, 4)]
ball3_alive = True

clock = pygame.time.Clock()

# Runs forever, until the user stops the program
while True:
    # Fill the screen with the background color set earlier
    screen.fill(BACKGROUND)

    # Ball 1
    if ball1_alive:
        # If the ball is alive the blit function displays it on the screen
        screen.blit(ball1_image, ball1_rect)

        # Check for collisions
        if ball1_rect.top < 0:
            ball1_speed[1] = -ball1_speed[1]
            ball1_speed[0] = random.uniform(-4, 4)

        if ball1_rect.left < 0 or ball1_rect.right > WIDTH:
            ball1_speed[0] = -ball1_speed[0]

        if ball1_rect.bottom > HEIGHT:
            ball1_alive = False

        ball1_rect = ball1_rect.move(ball1_speed)
    if ball1_rect.colliderect(tile):
        # If the ball collides with the tile invert its speed and give it a new speed
        ball1_speed[1] = -(ball1_speed[1] + 0.5)
        ball1_speed[0] = random.uniform(-(ball1_speed[1] + 2), ball1_speed[1] + 2)

    # Ball 2

    if ball2_alive:
        # If the ball is alive the blit function displays it on the screen
        screen.blit(ball2_image, ball2_rect)

        # Check for collisions
        if ball2_rect.top < 0:
            ball2_speed[1] = -ball2_speed[1]
            ball2_speed[0] = random.uniform(-4, 4)

        if ball2_rect.left < 0 or ball2_rect.right > WIDTH:
            ball2_speed[0] = -ball2_speed[0]

        if ball2_rect.bottom > HEIGHT:
            ball2_alive = False

        ball2_rect = ball2_rect.move(ball2_speed)
    if ball2_rect.colliderect(tile):
        # If the ball collides with the tile invert its speed and give it a new speed
        ball2_speed[1] = -(ball2_speed[1] + 0.5)
        ball2_speed[0] = random.uniform(-(ball2_speed[1] + 2), ball2_speed[1] + 2)

    # Ball 3

    if ball3_alive:
        # If the ball is alive the blit function displays it on the screen
        screen.blit(ball3_image, ball3_rect)

        # Check for collisions
        if ball3_rect.top < 0:
            ball3_speed[1] = -ball3_speed[1]
            ball3_speed[0] = random.uniform(-4, 4)

        if ball3_rect.left < 0 or ball3_rect.right > WIDTH:
            ball3_speed[0] = -ball3_speed[0]

        if ball3_rect.bottom > HEIGHT:
            ball3_alive = False

        ball3_rect = ball3_rect.move(ball3_speed)
    if ball3_rect.colliderect(tile):
        # If the ball collides with the tile invert its speed and give it a new speed
        ball3_speed[1] = -(ball3_speed[1] + 0.5)
        ball3_speed[0] = random.uniform(-(ball3_speed[1] + 2), ball3_speed[1] + 2)

    if ball1_alive or ball2_alive or ball3_alive:
        balls_alive = 0
        # Calculate the number of balls alive
        if ball1_alive:
            balls_alive += 1
        if ball2_alive:
            balls_alive += 1
        if ball3_alive:
            balls_alive += 1
        # If there is at least one ball alive the game has not ended yet
        game_is_over = False
        # Generate the counter text with the font initialized before and display it on the screen a (20, 20) coordinates, so on the top left
        if balls_alive == 1:
            counter_text = counter_font.render(f"{balls_alive} ball alive", True, (255, 255, 255))
        else:
            counter_text = counter_font.render(f"{balls_alive} balls alive", True, (255, 255, 255))

        screen.blit(counter_text, (20, 20))
    else:
        # If there is NOT at least one ball alive the game has ended
        game_is_over = True
        # Generate game over text
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        # Generate a game over rect form the text to get the total dimensions of the text
        game_over_rect = game_over_text.get_rect()
        # Calculate the position of the text (at the center of the screen so total width dived by two minus half of the width of the text itself, same for height but adding 100 to put it a little higher)
        game_over_position = (
            (WIDTH / 2) - game_over_rect.width / 2, (HEIGHT / 2) - game_over_rect.height - 100 / 2)
        # Display the text at the calculated position
        screen.blit(game_over_text, game_over_position)
        # Generate play again text and its rect for positioning and to check for collisions with the mouse
        play_again_text = play_again_font.render("Play Again", True, (0, 0, 255))
        play_again_rect = play_again_text.get_rect()

        # Calculate position like before but subtracting 100 to height to put it a little lower and move the rect to the correct position
        play_again_position = (
            (WIDTH / 2) - play_again_rect.width / 2, (HEIGHT / 2) - play_again_rect.height + 100 / 2)
        play_again_rect = play_again_rect.move(play_again_position[0], play_again_position[1])

        # Calculate the starting position of the underline so: same width, then same height plus its rect height to put it under the text
        play_again_underline_start = (play_again_position[0], play_again_position[1] + play_again_rect.height)
        # Same here but adding its width
        play_again_underline_end = (
            play_again_position[0] + play_again_rect.width, play_again_position[1] + play_again_rect.height)
        # Draw the line
        pygame.draw.line(screen, (0, 0, 255), play_again_underline_start, play_again_underline_end, 5)
        # Display the line on the screen
        screen.blit(play_again_text, play_again_position)

    for event in pygame.event.get():
        # Check for event
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # The user right-clicked somewhere
            if game_is_over:

                if play_again_rect.collidepoint(pygame.mouse.get_pos()):
                    # If the mouse is over the text and has right-clicked on the text generate 5 new balls
                    ball1_image = pygame.image.load("small_tennis.png")
                    ball1_rect = ball1_image.get_rect()
                    ball1_speed = [random.uniform(-4, 4), random.uniform(1, 4)]
                    ball1_alive = True

                    ball2_image = pygame.image.load("small_tennis.png")
                    ball2_rect = ball2_image.get_rect()
                    ball2_speed = [random.uniform(-4, 4), random.uniform(1, 4)]
                    ball2_alive = True

                    ball3_image = pygame.image.load("small_tennis.png")
                    ball3_rect = ball3_image.get_rect()
                    ball3_speed = [random.uniform(-4, 4), random.uniform(1, 4)]
                    ball3_alive = True

    # Set x axis of the tile to the mouse position
    tile.centerx = pygame.mouse.get_pos()[0]
    if not game_is_over:
        # Draw the tile on the screen if the game is not over
        pygame.draw.rect(screen, (255, 0, 0), tile)

    # Refresh the screen
    pygame.display.update()
    pygame.display.flip()
    # Limit screen updates to 60 times a second
    clock.tick(60)
