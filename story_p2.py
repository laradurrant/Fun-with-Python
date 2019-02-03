class Story():

    player_name = ""
    likes_apples = False
    game_status = True

    def __init__(self):
        return

    def getPlayerName(self):
        return self.player_name

    def getAppleStatus(self):
        return self.likes_apples

    def getGameStatus(self):
        return self.game_status

    def setAppleStatus(self, apples):
        self.likes_apples = apples

    def setPlayerName(self, name):
        self.player_name = name        

    def setGameStatus(self,  status):
        self.status = status   


def askPlayerName():

    confirmed = False

    while(not confirmed):
        name = input("What's your name? \n > ")

        answer = input("Is that okay? (y/n) \n > ")

        answer = answer.lower()
        
        if(answer == 'y' or answer == 'yes' or answer == '1'):
            our_story.setPlayerName(name)
            confirmed = True


def askAboutApples():
    apples = input("Do you like apples? (y/n) \n > ")
    apples = apples.lower()
    
    if(apples == 'y' or apples == 'yes' or apples == '1'):
        print("You like apples! Yay!")
        our_story.setAppleStatus(True)
    else:
        print("You don't like apples! Too bad!")
        our_story.setAppleStatus(False)


def askFavoriteColor():
    color = input("What's your favorite color? \n > ")
    color = color.lower()
    
    if(color == 'blue' or color == 'purple' or color == 'green'):
        print("You have good taste in colors!")
        our_story.setGameStatus(True)
    else:
        print("I don't want to talk to you anymore...")
        our_story.setGameStatus(False)
        return False

def winGame():
    print("")
    print("=====================")
    print("    Yay!! You win!   ")
    print("=====================")
    print("")

    
def gameOver():
    print("")
    print("=====================")
    print("Too bad!! You lose...")
    print("=====================")
    print("")


def intro():
    print("This is a story about " + our_story.player_name)


def game():
    
    continue_game = True
    
    while continue_game:
        askPlayerName()
        askAboutApples()
        continue_game = askFavoriteColor()
        
        if continue_game:
            gameOver()
        else:
            winGame()
        



our_story = Story()


while our_story.getGameStatus() is True:

    game()
    
    restart = input("Do you want to play again? (y/n) \n > ")
    
    if restart == 'n':
        break
    elif restart == 'y':
        continue
