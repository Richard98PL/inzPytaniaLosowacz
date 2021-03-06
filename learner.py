import random
import time
from os import system, name 
import msvcrt

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def sleeper(number):
    for i in range(number):
        print(str(number-i) + '...')
        time.sleep(0.1)
    clear()

file = open('pytania.txt','r',encoding='utf-8')
lines = file.read().splitlines()
random.shuffle(lines)

singlePhrases = []
for line in lines:
    #line = line.lower()
    if line.strip():
            singlePhrases.append(line)
            print(line)
print('\nIntialization finished succesfully.')
print(str(len(singlePhrases)) + ' questions loaded.')

input_char = 'a'

while ord(input_char) is not 113:
    for i in range(3):
        print('-> ' + random.choice(singlePhrases))
    print('Press anything or press q to leave...')
    input_char = msvcrt.getch()       
    sleeper(3)
    



    


