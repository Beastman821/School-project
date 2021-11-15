from random import choice
from random import shuffle
# imported random module

# import shutil
# imported shutil to be able to open up the wordList.txt

print('Welcome to CRYPTO-LOGIC!')
print('Try to guess the scrambled word, one letter at a time!')

# Function for choosing random word


# opening up the list of words file
# my_file = open(r"C:\Users\kelli\OneDrive\Desktop\Back-end\wordList.txt")
# content = my_file.read()
# content_list = content.split(',')




words = ["logic", "apple", "red"]
global pick
pick = choice(words)
    
break_apart_word = list(pick)
shuffle(break_apart_word)
    
global shuffled_word
shuffled_word = ''
for letter in break_apart_word:
    shuffled_word += letter
    
    
print("scrambled word:", break_apart_word)
guess = input("Enter your guess.... ")
score = 0
letters_gussed = []

while pick != letters_gussed:
    if pick[0] == guess:
        letters_gussed.append(guess)
        a = score
    elif pick[0] != guess: 
        a = score + 1 
    else:
        print('0')


print('letter already guessed', letters_gussed)
print('incorrect guesses', a)
    



