import random

min = 1
max = 5

keep_playing = True

while(keep_playing):
    answer = random.randint(min,max)

    print("I'm thinking of a random number between " + str(min) + " and " + str(max))

    invalid = True
    
    while invalid:
        try:
            guess = int(input("Enter your guess: "))
            invalid = False
        except ValueError:
            print("Invalid input.")
            invalid = True

    if answer == int(guess):
        print("You guessed correctly!")
    else:
        print("Whoops! You lose!")
        print("The correct answer was", answer)

    answer = input("Try again? y/n ")
    answer = answer.lower()

    if(answer == 'y'):
        keep_playing = True
    else:
        keep_playing = False
