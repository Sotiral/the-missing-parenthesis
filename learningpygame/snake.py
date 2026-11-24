import pygame
from random import randint

#declaration of independeace
pygame.init()
widht, height = pygame.display.get_desktop_sizes()[0]
cell = 30
cols = int(widht / 1.5) // cell
rows = int(height / 1.5) // cell
pygame.display.set_caption("HELLO MISTERM SNAKIES")

screen = pygame.display.set_mode((cols * cell, rows * cell))
widht, height = screen.get_size()
clock = pygame.time.Clock()
running = True

snake = [(cols // 2, rows // 2)]
dx ,dy = 1, 0
apple = (randint(0, cols -1), randint(0, rows - 1))
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dx, dy = 0, -1
            elif event.key == pygame.K_s:
                dx, dy = 0, 1
            elif event.key == pygame.K_a:
                dx, dy = -1, 0
            elif event.key == pygame.K_d:
                dx, dy = 1, 0
    head = (snake[0][0] +dx, snake[0][1] + dy)

    if head[0] < 0 or head[0] >= cols or head[1] < 0 or head[1] >= rows or head in snake:
        running = False
        print("Get rekt " + str(score) )
    snake.insert(0, head)

    if head == apple:
        score += 1
        apple = (randint(0, cols -1), randint(0, rows -1))
    else:
        snake.pop()

    screen.fill((67, 67, 67))
    pygame.draw.rect(screen, (0, 200, 0), (apple[0] * cell, apple[1] * cell, cell, cell))

    for part in snake:
        pygame.draw.rect(screen, (220, 0, 0), (part[0] * cell, part[1] * cell, cell, cell))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()