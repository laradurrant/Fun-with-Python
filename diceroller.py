from random import randint

# Functions! 
def diceRoll():
	dice = randint(1,6)
	return dice
	
	
def printWelcome():
	print("Welcome to the Dice Roller game!")

	
def getName():
	person = input('What is your name? ')
	print('Hello', person)
	
	
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
	
	
# Variables!
guess = diceRoll()	
printWelcome()
getName()
count = 0

# Main guessing game loop
while(getNumber(guess) == False):
	print("Trying again.")
	count += 1
	print ("You have attempted this " + str(count) + " time(s).") 
	
# Exit message
print("Congrats! You finished in " + str(count) + " attempt(s).");