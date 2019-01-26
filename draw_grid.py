import pygame
import random
from time import sleep

pygame.init()
pygame.display.set_caption('My Game @ Pygame')

height = 800
width = 800
window = pygame.display.set_mode((width, height))
x = 0
y = 100
big = 8
small = 1

WHITE = (255,255,255)
GREY = (100,100,100)

while x < width:
    for z in range(0, 8):
      player = pygame.draw.circle(window, GREY, (x,z * 100), small)
    
    if x % 100 == 0:
      for z in range(0, height):
        player = pygame.draw.circle(window, GREY, (x,z), small)

    
    x = x + 1
    
    pygame.display.update()

x = 100

while x < width:
    
    if x % 100 == 0:
      for z in range(1, 8):
        player = pygame.draw.circle(window, WHITE, (x,z * 100), big)

    x = x + 1
    
    pygame.display.update()


  
pygame.quit()
