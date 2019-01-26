import pygame
import math
pygame.init()

global mouse_x, mouse_y
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
WHITE = (  255,   255,   255)

run_update = False
updating = True
draw_circle = False
clear_screen = False

def drawCircle():
    print("Drawing a new circle at (x: " + str(mouse_x) + ", y: " + str(mouse_y) + ")")
    pygame.draw.circle(screen, WHITE, [mouse_x, mouse_y], 40)

def clearScreen():
    print("Clearing the screen.")
    screen.fill((0, 0, 0))

    

while(updating):
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                draw_circle = True
            elif event.button == 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clear_screen = True
                
                
    if(clear_screen):
        clearScreen()
        clear_screen = False
        draw_circle = False
 
    if(draw_circle):
        drawCircle()
        draw_circle = False

    pygame.display.flip()
    
    pygame.display.update()
