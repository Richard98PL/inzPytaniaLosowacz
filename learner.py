import random
import time
import os
import msvcrt

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def sleeper(number):
    for i in range(number):
        #print(str(number-i) + '...')
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
        print('-> ' + bcolors.WARNING + random.choice(singlePhrases) + bcolors.ENDC)
    print('Press anything or press q to leave...')
    input_char = msvcrt.getch()       
    



    


