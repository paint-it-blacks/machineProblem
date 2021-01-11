#CMSC11 >:'(

import csv
import pandas
import sys

def Play():
    #inserting name
    answer = input ('Insert Name: \n')
    print ('Hello, {answer}')
    #csv
    f = None
    df = pd.read_csv('questionBank.csv')
    print(df)
    
def Highscores():
    #inserting name
    answer = input ('Insert Name: \n')
    print ('Hello, {answer}')
    #csv
    f = None
    df = pd.read_csv('questionBank.csv')
    print(df)

while(True):
    print ('1 - Play \n')
    print ('2 - Highscores \n')
    print ('3 - Quit \n')
    answer = input ('Choose a number: ')
    if answer == 1:
        Play()
    elif answer == 2:
        Highscores
    else: sys.exit()
