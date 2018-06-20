# Our list of prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# min = 0
min = 0
# max = n - 1
max = len(primes) - 1
# Our target search value
# To-do: allow user to input this number
target = 79


# Linear search example
# Will stop upon reaching the right number
print("---------------------------------------\n")
print("Now trying the linear search method\n")
print("---------------------------------------\n")
tries = 0

# Searches from beginning to end of the list
for i in primes:
	tries += 1
	print(str(i) + " -- Attempts: " + str(tries) + "\n")
	if(i == target):
		print("Found it!")
		break
print("\n");

# Resets the number of tries
tries = 0
print("---------------------------------------\n")
print("Now trying the binary search method!\n")
print("---------------------------------------\n")

while(True):
	if max < min:
		print("Not in the list!")
		break
	guess = int((max + min) / 2)
	if primes[guess] == target:
		tries += 1
		print(str(primes[guess]) + " -- Attempts: " + str(tries) + "\n")
		print("Found it!")
		break
	elif primes[guess] < target:
		tries += 1
		print(str(primes[guess]) + " -- Attempts: " + str(tries) + "\n")
		min = guess + 1
	elif primes[guess] > target:
		tries += 1
		print(str(primes[guess]) + " -- Attempts: " + str(tries) + "\n")
		max = guess - 1
		
			