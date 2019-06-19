# some practice with python for a student

# This function says "hello"
def say_hello():
  print "hello"

# This function prints a new line
def add_new_line():
  print "\n"

# This function will print every letter of the string on a new line
def get_letters(string):
  for letter in string:
    print letter
    
  
# This function will create a variable new_word and copy each letter from "string"
# into the new_word. At the end, it will print new_word.
def get_letters_one_line(string):
  new_word = "nothing to see here... "
  print new_word
  for letter in string:
    new_word += letter
  print new_word
  
# This function will print the length of the variable "string"
# In this example we use "hello" so the answer is 5. 
def get_word_length(string):
  print "Total number of words in " + string + " is: "
  print len(string)

# This function will print the number of each letter in our variable "string"
# 0-1-2-3-4 will appear on new lines
def get_numbers_per_letter(string):
  for number in range(0, len(string)):
    print number
  
# This function will print the number of each letter in our variable "string"
# 01234 will appear on the same line
def get_numbers_per_letter_one_line(string):
  new_word = ""
  for number in range(0, len(string)):
    new_word += str(number)
  print new_word
  
# This function does the same as get_numbers-per_letter_one_line() ...
# but it does so in a slightly different way
def get_numbers_per_letter_one_line_alt(string):
  new_word = ""
  word_length = len(string)
  for number in range(0, word_length):
    new_word += str(number)
  print new_word
  

# This function will print the text "fizz" if the first letter is uppercase
# ... or "bang" if the letter is bang
# It will then cycle through the letters of the word
def get_uppercase(string):
  for letter in string:
    if letter.isupper():
      print("fizz")
    else:
      print("bang")
    
say_hello()

add_new_line()    

get_letters("hello")

add_new_line()

get_letters_one_line("hello")

add_new_line()

get_word_length("hello")

add_new_line()

get_numbers_per_letter("hello")

add_new_line()

get_numbers_per_letter_one_line("hello")

add_new_line()

get_numbers_per_letter_one_line_alt("hello")

add_new_line()

get_uppercase("HelLo")
