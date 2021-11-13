import random 
# imported random module

import shutil
# imported shutil to be able to open up the wordList.txt

print('Welcome to CRYPTO-LOGIC!')
print('Try to guess the scrambled word, one letter at a time!')

# Function for choosing random word


# opening up the list of words file
my_file = open(r"C:\Users\kelli\OneDrive\Desktop\Back-end\wordList.txt")
content = my_file.read()
content_list = content.split(',')


# this function will randomly choose any word from the list
pick = random.choice(content_list)


print(f"scrambled word:")


