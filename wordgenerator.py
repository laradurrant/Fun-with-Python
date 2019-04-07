# Random word generator

import random


vowels = ["a","i","e","o","u","iht","ai","ia","ei","io","au","oi","ea","ui"]
# consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
consonants = ["v","b","p","f","m","n","j","k","g","q","d","t","w","s","tj","z","nj","l","r","ht","h"]

endings = ["q","k","v","ir","n","l","","",""]


#print(vowels)
#print(consonants)


def getRandomVowel():
    x = random.randint(0,len(vowels)-1)
    return vowels[x]

def getRandomConsonant():
    x = random.randint(0,len(consonants)-1)
    return consonants[x]

def getRandomEnding():
    x = random.randint(0,len(endings)-1)
    return endings[x]


def getWord():
    length = random.randint(3,8)
    #print(length)
    word = ""
    
    if(length % 2 == 0):
        #print("even")
        for x in range(0, length, 2):
            word += getRandomConsonant() + getRandomVowel()
    else:
        #print("odd")
        word += getRandomVowel()
        for x in range(1, length-1, 2):
            word += getRandomConsonant() + getRandomVowel()
    word += getRandomEnding()
    return word
    

def getWords(x):
    for n in range(x):
        print(getWord())
        
    

#print(getRandomVowel())

#print(getWord())
getWords(20)
