from random import randint

# Functions! 

# Outputs a random int (dice roll) between 1 and 6
def diceRoll():
	dice = randint(1,6)
	return dice
	
# Welcomes the player to the game
def printWelcome():
	print("Welcome to the Dice Roller game!")

# Gets the player's name
# To-Do: Consider some sort of error checking
def getName():
	person = input('What is your name? ')
	print('Hello', person)
	
# Accepts the player's guesses
# If the number matches the computer's guess, then the player wins
# If they guess incorrectly, they will be prompted to add another

# To-Do: Cut the player off after a certain number of incorrect guesses

def getNumber( roll ):
	guess = input('Guess a number between 1 and 6: ')
	guess = int(guess)
	if(roll == guess):
		print("You guessed correctly!")
		return True
	else:
		print("You guessed wrongly...")
		print("Try again!")
		return False		
	
	
# Rolls the dice
guess = diceRoll()	
# Welcomes the player 
printWelcome()
# Gets the player's name
getName()
# Sets the guess count to zero
count = 0

# Main guessing game loop
# If the player hasn't guessed correctly, the game will prompt
# the player to ask again.

while(getNumber(guess) == False):
	print("Trying again.")
	# Increases the guess count by one each time
	count += 1
	print ("You have attempted this " + str(count) + " time(s).")
	
# Exit message
print("Congrats! You finished in " + str(count) + " attempt(s).");