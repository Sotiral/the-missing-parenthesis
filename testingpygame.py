import pygame
import time

print(pygame.version.rev) #confirms pygame ce

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock() #main stuff
running = True
clock.tick(60)
pygame.display.set_caption("The Missing Parenthesis")
