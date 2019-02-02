import pygame
pygame.init()

window_w = 800
window_h = 600

white = (255, 255, 255)
black = (0, 0, 0)

FPS = 120

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Game: ")
clock = pygame.time.Clock()
pause_game = True

ball_size = 20
velocity = [1, 1]

pos_x = window_w/2
pos_y = window_h/2

font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Hello, World", True, (0, 128, 0))


def pause():
    print("Pausing the game!")
    global pause_game
    pause_game = not pause_game


def print_ball_status():
    global pos_x, pos_y, velocity
    print("Ball's position X, Y: (%3d, %3d)" % (pos_x, pos_y))
    print("Ball's Velocity X, Y: (%.1f, %.1f)" % (velocity[0], velocity[1]))
    print("")    

# Our main game loop
def game_loop():
    global pos_x, pos_y
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Click event detected!")
                pause()

       
        # Run this if the game isn't paused
        if(not pause_game):

            pos_y += velocity[1]
            velocity[1] = velocity[1] + 0.04

            pos_x += velocity[0]

            #print_ball_status()

            
            if pos_x + ball_size > window_w or pos_x < ball_size:
                velocity[0] = -velocity[0]
                print("Hit the left or right sides!")

            if pos_y + ball_size > window_h or pos_y < ball_size:
                velocity[1] = -velocity[1]
                print("Hit the bottom!")

        # DRAW
        window.fill(white)
        pygame.draw.circle(window, black, (int(pos_x), int(pos_y)), ball_size)
        
        pygame.display.update()
        clock.tick(FPS)


game_loop()
