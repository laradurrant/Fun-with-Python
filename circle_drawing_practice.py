# This is a simple pygame app that will allow the creation of randomly colored circles.

import pygame
import math
import random
pygame.init()

# Makes mouse_x and mouse_y into global variables
global mouse_x, mouse_y

# Sets up the initial screen
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
WHITE = (  255,   255,   255)

run_update = False
updating = True
draw_circle = False
clear_screen = False

    # Draws a circle
def drawCircle():
    print("Drawing a new circle at (x: " + str(mouse_x) + ", y: " + str(mouse_y) + ")")
    
    pygame.draw.circle(screen, randomColor(), [mouse_x, mouse_y], 40)




    # Clears the screen by filling it black
def clearScreen():
    print("Clearing the screen.")
    screen.fill((0, 0, 0))

    # + Hexademical is base 16 (as opposed to base 10, our everyday decimal system)
    #
    # + How to convert RGB tuple to hexadecimal:
    # https://stackoverflow.com/questions/3380726/converting-a-rgb-color-tuple-to-a-six-digit-code-in-python
    # + HTML color picker:
    # https://www.w3schools.com/colors/colors_picker.asp
    #
    # The function randomColor makes use of the randint() function
    # This allows us to pick a random number between 0 and 255

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # + About Tuples:
    # https://www.w3schools.com/python/python_tuples.asp
    tuple = (r, g, b)  
    print("RGB Color: " + str(tuple))

    # + About this code
    # The 02 portion formats the numbers (0 through 255) as 2 digits with
    # a 0 at the front to pad it -- aka "hex" format
    # The 'x' portion means lower-case
    # You could also use 'X' for upper-case
    #
    # See also:
    # https://stackoverflow.com/questions/14678132/python-hexadecimal
    # https://docs.python.org/2/library/string.html#formatspec
    
    hex = '#%02X%02X%02X' % (r, g, b)
    print("Hexadecimal: " + hex)
    
    return tuple


while(updating):
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # In Pygame, you can access the left & right click of the mouse
            # separately. In this case, button 1 is for left click and 3 is for
            # right click.
            
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                draw_circle = True
            elif event.button == 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clear_screen = True
                
    # Part of our main loop. If either variable clear_screen or draw_circle
    # are set as true during a MOUSE BUTTON DOWN event (a 'click'), then
    # we will either clear the screen or draw a circle, depending on the type
    # of input that we received.
                
    if(clear_screen):
        clearScreen()
        clear_screen = False
        draw_circle = False
 
    if(draw_circle):
        drawCircle()
        draw_circle = False

    # Update the full display Surface to the screen
    #pygame.display.flip()

    # Slightly more 'optimized' version of display.flip()
    # Also updates the screen
    pygame.display.update()
