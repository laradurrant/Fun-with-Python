import pygame

pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = ( 255, 255, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False

player_pos = (8,1)

our_map = [[2,2,2,2,2,2,2,2,2,2,2,2,2],
           [2,1,0,0,0,0,0,0,1,0,0,0,2],
           [2,0,0,1,0,1,0,1,0,0,1,0,2],
           [2,0,1,0,1,0,0,1,0,1,1,0,2],
           [2,0,1,0,1,0,1,0,0,1,0,0,2],
           [2,0,1,0,1,0,1,0,1,1,0,1,2],
           [2,0,0,0,1,0,1,0,1,0,0,0,2],
           [2,1,1,0,1,0,1,0,1,0,1,0,2],
           [2,5,0,0,1,0,0,0,0,1,7,0,2],
           [2,2,2,2,2,2,2,2,2,2,2,2,2]]
    

def draw_map():
# Draws a square at position specified in our_map
# The x and y coordinates are multiplied by 50 so that the
# grid can be spaced out correctly. 
  for i in range(len(our_map)) :  
      for j in range(len(our_map[i])) :  
          if(our_map[i][j] == 1):
            pygame.draw.rect(screen, RED, [50*j, 50*i, 50, 50], 0)
          elif(our_map[i][j] == 2):
            pygame.draw.rect(screen, BLUE, [50*j, 50*i, 50, 50], 0)
          elif(our_map[i][j] == 5):
            pygame.draw.rect(screen,GREEN,[50*j, 50*i, 50, 50], 0)
          elif(our_map[i][j] == 7):
            pygame.draw.rect(screen,YELLOW,[50*j, 50*i, 50, 50], 0)
            
            

# This function will update our player's current location & map
def move(direction_key):
  #direction_key
  # 0 = left
  # 1 = up
  # 2 = right
  # 3 = down
  
  global player_pos
  global our_map
  global done
  
  i = player_pos[0]
  j = player_pos[1]
  
  new_i = i
  new_j = j
  
  if(direction_key == 0):
    new_j = j-1
  elif(direction_key == 1):
    new_i = i-1
  elif(direction_key == 2):
    new_j = j+1
  elif(direction_key == 3):
    new_i = i+1
    
  if(our_map[new_i][new_j] == 2):
    return
  elif(our_map[new_i][new_j] == 1):
    return
  else:
    player_pos = (new_i,new_j)
    if(our_map[new_i][new_j] == 7):
      print("You win!")
      done = True
    our_map[new_i][new_j] = 5
    our_map[i][j] = 0  


def print_intro():
  print("Welcome to the maze game!")
  print("Use the Left Right Up Down keys to move")
  print("Reach the yellow square to win!")

print_intro()

while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            move(0)
          if event.key == pygame.K_RIGHT:
            move(2)
          if event.key == pygame.K_DOWN:
            move(3)
          if event.key == pygame.K_UP:
            move(1)


 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    
    #pygame.draw.rect(screen, RED, [55, 50, 20, 25], 0)
    draw_map()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
