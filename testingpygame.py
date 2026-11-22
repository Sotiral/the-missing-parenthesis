import pygame
import time
from random import randint

# Main stuff

pygame.init()
width, height = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((width // 2, height // 2))
width, height = screen.get_size()
clock = pygame.time.Clock() #main stuff vol2
running = True
pygame.display.set_caption("The Missing Parenthesis")
icon = pygame.image.load("art/doggie.jpg")
pygame.display.set_icon(icon)


#declaration of independence

font = pygame.font.Font(None, 36)
text = font.render("This is some text ig", True, (255, 255, 255))
text_rect = text.get_rect(center=(width // 2, height // 2))




#running loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    
    screen.fill((0, 0, 0)) 
    screen.blit(text, text_rect)
    scaled_icon = pygame.transform.scale(icon, (60, 60))
    screen.blit(scaled_icon, (randint(0, width), randint(0, height)))
    pygame.display.flip() 
    clock.tick(60)

pygame.quit()