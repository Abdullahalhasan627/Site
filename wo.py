import pygame
import random

# إعداد الألوان
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# تهيئة اللعبة
pygame.init()
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# اللعبة الرئيسية
def game():
    snake = [[WIDTH // 2, HEIGHT // 2]]
    direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
    food = [random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE]

    speed = 12  # تعديل سرعة الحركة

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, 1):
            direction = (0, -1)
        elif keys[pygame.K_DOWN] and direction != (0, -1):
            direction = (0, 1)
        elif keys[pygame.K_LEFT] and direction != (1, 0):
            direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and direction != (-1, 0):
            direction = (1, 0)

        head = list(snake[0])
        head[0] += direction[0] * GRID_SIZE
        head[1] += direction[1] * GRID_SIZE
        snake.insert(0, head)

        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]:
            running = False

        if head[0] == food[0] and head[1] == food[1]:
            food = [random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE]
        else:
            snake.pop()

        window.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(window, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(window, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
        pygame.display.flip()
        clock.tick(speed)  # تعديل سرعة الحركة

    pygame.quit()

# تشغيل اللعبة
game()
