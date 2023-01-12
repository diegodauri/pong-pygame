import pygame
import random

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)

balls = []

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Ball:
    def __init__(self):
        self.image = pygame.image.load("small_tennis.png")
        self.rect = self.image.get_rect()
        self.speed = [random.uniform(-4, 4), random.uniform(1, 4)]
        self.alive = True

    def update(self):
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
            self.speed[0] = random.uniform(-4, 4)

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]

        if self.rect.bottom > HEIGHT:
            self.alive = False

        self.move()

    def move(self):
        self.rect = self.rect.move(self.speed)


class Tile():
    def __init__(self):
        self.rect = pygame.Rect(0, HEIGHT - 15, 150, 15)


clock = pygame.time.Clock()

counter_font = pygame.font.SysFont(None, 48)
game_over_font = pygame.font.SysFont(None, 100)
play_again_font = pygame.font.SysFont(None, 70)

tile = Tile()

for i in range(5):
    ball = Ball()
    balls.append(ball)

while True:
    screen.fill(BACKGROUND)

    balls_alive = 0
    for i, ball in enumerate(balls):
        if ball.alive:
            screen.blit(ball.image, ball.rect)
            ball.update()
            balls_alive += 1
        if not ball.alive:
            balls.pop(i)

        if ball.rect.colliderect(tile.rect):
            ball.speed[1] = -(ball.speed[1] + 0.5)
            ball.speed[0] = random.uniform(-(ball.speed[1] + 2), ball.speed[1] + 2)

    if balls_alive > 0:
        game_is_over = False
        counter_img = counter_font.render(f"{balls_alive} balls alive", True, (255, 255, 255))
        screen.blit(counter_img, (20, 20))
    else:
        game_is_over = True
        game_over_img = game_over_font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_img.get_rect()
        game_over_position = (
            (WIDTH / 2) - game_over_rect.width / 2, (HEIGHT / 2) - game_over_rect.height - 100 / 2)
        screen.blit(game_over_img, game_over_position)

        play_again_img = play_again_font.render("Play Again", True, (0, 0, 255))
        play_again_rect = play_again_img.get_rect()
        play_again_position = (
            (WIDTH / 2) - play_again_rect.width / 2, (HEIGHT / 2) - play_again_rect.height + 100 / 2)
        play_again_underline_start = (play_again_position[0], play_again_position[1] + play_again_rect.height)
        play_again_underline_end = (
            play_again_position[0] + play_again_rect.width, play_again_position[1] + play_again_rect.height)
        pygame.draw.line(screen, (0, 0, 255), play_again_underline_start, play_again_underline_end, 5)

        screen.blit(play_again_img, play_again_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_is_over:
                if play_again_rect.move(play_again_position[0], play_again_position[1]).collidepoint(
                        pygame.mouse.get_pos()):
                    for i in range(5):
                        ball = Ball()
                        balls.append(ball)

    tile.rect.centerx = pygame.mouse.get_pos()[0]
    if not game_is_over:
        pygame.draw.rect(screen, (255, 0, 0), tile.rect)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
