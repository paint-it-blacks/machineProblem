#!/usr/bin.env python3

import pandas as pd
import sys

def verifyInput(lis,inp):
    validInp = False
    for i in lis:
        if inp == i:
            validInp = True
            break
    return validInp

if __name__ == '__main__':
    f = None
    while f == None:
        PATH_CS = input("Enter filename: ")
        try:
            f = open(PATH_CS,"r",encoding="utf-8")
        except:
            print("Invalid file! Please try again!")
            f = None
    df = pd.read_csv(f,delimiter=",")
    f.close()
    arrHead = list(df.columns.values)
    category = None
    while not verifyInput(arrHead,category):
        category = input("Enter column name to be sorted: ")
        if not verifyInput(arrHead,category):
            print("Invalid header name! Please try again!")
    sortedDf = df.sort_values(category)
    sortedDf.to_csv(PATH_CS,index=False)
    sys.exit()
