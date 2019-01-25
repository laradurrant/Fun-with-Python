import random


# ~OUR VARIABLES~ #

#the title of our game
title = "Haunted House Game"

#gives us a random age between 18 and 80
age = random.randint(18,80)

#default player_name
player_name = "Coder Coding"

#likes apples, should be True or False
likes_apples = True

hill_type = ["grassy", "barren", "spooky", "cold", "dreary", "small", "rainy", "lonely", "hidden"]

#line-break response
line_break_response = " \n > "

#yes-or-no options
yes_or_no = " \n 1 - Yes, 2 - No \n > "

# ~OUR FUNCTIONS~ #

#returns a series of equal signs for a page break
def txtbreak():
    return "=================="

#returns a blank string for our game
def txtblank():
    return "                  "


#print the title of our game
def print_title():
    print(txtblank())
    print(txtbreak())
    print(title)
    print(txtbreak())
    print(txtblank())

#ask name
def askName():
    confirmed = False

    while(confirmed == False):
        player_name =  input("What should I call you?" + line_break_response)
        answer = input("Is " + player_name + " okay?" + yes_or_no)
        
        if(answer == '1' or answer == 'Yes' or answer == 'Y'):
            print("Cool! We'll go with that for now!")
            confirmed = True
            return player_name    

# Ask a simple yes or no question; return True is the answer is 1, Yes, or Y
def askQuestion(question):
    
    player_answer = input(question)
    if(player_answer == '1' or player_answer == 'Yes' or player_answer == 'Y'):
        print("Cool! We'll go with that!")
        return True
    else:
        return False

#asks another question   
def askNextQuestion():
     print("Next question...")

#asks a question about apples and returns True or False depending if the player likes apples or not
def askAboutApples():
    likes_apples = askQuestion("Do you like apples?" + yes_or_no)
    return likes_apples

# Confirms a response (text only)
def confirmResponse():
    print("Got it!")

# Prints a line whether the player likes apples or not
def getAppleStatus():
    if(likes_apples):
        print("You like apples! Yay!")
    else:
        print("You don't like apples! Too bad!")
        

def getHillType():
    x = random.randint(0,len(hill_type))
    return hill_type[x]

def appleSentence():
    if(likes_apples):
      return "likes apples"
    else:
      return "doesn't like apples"

# Repeats the name of the player
def repeatName():
    print("It's nice to meet you, {}!".format(player_name))


# the very beginning of our story
def startIntro():
    print("You are a person.")
    print("This year you are turning " + str(age) + " years old.")
    print("It's your birthday soon!")
    print("You've always wanted to explore a haunted house.")

    print("Oops! I never asked you your name.")

def tellStory():
    print("This is a story about " + player_name + " who " + appleSentence() + ".")
    print("Once upon a time, our hero decided they wanted to explore a haunted mansion.")
    print("The mansion was set atop a " + getHillType() + " hill.")

# ~OUR STORY~ #

#writes the title
print_title()

#intoduction!
startIntro()

#calls a function to ask the player's name
player_name = askName()

#asks another question
askNextQuestion()

#asks if the player likes apples
likes_apples = askAboutApples()

#confirms the player's response in text
confirmResponse()

#repeats back the player's name
repeatName()

#returns whether the player likes apples or not
getAppleStatus()

#continues the story
tellStory()
