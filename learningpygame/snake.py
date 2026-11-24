# Great demo for input and moving things around - took about an hour to complete.

import pygame
from random import randint
import time

# SPEED + BCOLOR
print("Hello there! This is Snake, please confirm the following:")
time.sleep(0.3)
print("Speed -> how fast your snake moves. Select (1) for SLOW (2) for NORMAL (3) for FAST")
time.sleep(0.3)
speed = int(input("SELECTION: "))
time.sleep(0.3)
print("Snake color -> color of the snake. Select (1) for RED (2) for YELLOW (3) for BROWN")
time.sleep(0.3)
scolor = int(input("SELECTION: "))
time.sleep(0.3)
print("Background color -> color of the background. Select (1) for PINK (2) for PURPLE (3) for BLUE (4) for GREEN (5) for PEACH")
time.sleep(0.3)
bcolor = int(input("SELECTION: "))


#declaration of independeace

bcolors = {
    1: (245, 189, 230),
    2: (198, 160, 246),
    3: (30, 32, 48),
    4: (45, 90, 69),
    5: (245, 169, 127)
}

scolors = {
    1: (237, 135, 150),
    2: (238, 212, 159),
    3: (166, 123, 91)
}

pygame.init()
widht, height = pygame.display.get_desktop_sizes()[0]
cell = 30
cols = int(widht / 1.5) // cell
rows = int(height / 1.5) // cell
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((cols * cell, rows * cell))
widht, height = screen.get_size()
clock = pygame.time.Clock()
icon = pygame.image.load("art/doggie.jpg").convert()
pygame.display.set_icon(icon)

snake = [(cols // 2, rows // 2)]
dx ,dy = 1, 0
apple = (randint(0, cols -1), randint(0, rows - 1))
score = 0

time.sleep(0.5)

running = True



#run forest run
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
        print("Get rekt!!! SCORE:", score) #im stupid I could have used {score}, or , score instead of converting it into a string in older versions
    snake.insert(0, head)

    if head == apple:
        score += 1
        apple = (randint(0, cols -1), randint(0, rows -1))
    else:
        snake.pop()

    screen.fill(bcolors[bcolor])
    pygame.draw.rect(screen, (0, 200, 0), (apple[0] * cell, apple[1] * cell, cell, cell))

    for part in snake:
        pygame.draw.rect(screen, scolors[scolor], (part[0] * cell, part[1] * cell, cell, cell))

    pygame.display.flip()

    if speed == 1:
        clock.tick(5)
    elif speed == 2:
        clock.tick(10)
    elif speed == 3:
        clock.tick(15)
    else:
        print("1 / 2 / 3")

pygame.quit()
