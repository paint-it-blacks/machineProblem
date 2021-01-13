import random
import index

quesNum = None
charName = None

PATH_EZ = "txts/ezQs.txt"
PATH_MD = "txts/mdQs.txt"
PATH_DF = "txts/dfQs.txt"
choice1 = ['A','B','C','a','b','c']
choiceMain = ['A','B','C','D','a','b','c','d']
yesOrNo = ['y','n','Y','N']
aOrB = ['a','b','A','B']
LLUsed = [False,False,False,False]
LLs = ["Wise Friend","Unsure Friend","Arrogant Friend","50/50"]
difficultyStr = ["Easy","Moderate","Hard"]
amtWinnings = [0,1000,2000,4000,8000,15000,30000,40000,50000,80000,100000,200000,300000,600000,800000,1000000]


def randomPickQs(origList,newList):
    while(len(newList) < 5):
        randIndex = random.randint(0,len(origList)-1)
        newList.append(origList[randIndex])
        origList.remove(origList[randIndex])
    return (origList,newList)

def preProcessQs():
    ezDraw = [int(i) for i in range(0,10)]
    mdDraw = [int(i) for i in range(0,10)]
    dfDraw = [int(i) for i in range(0,10)]
    fEz = open(PATH_EZ,"r",encoding="utf-8")
    fMd = open(PATH_MD,"r",encoding="utf-8")
    fDf = open(PATH_DF,"r",encoding="utf-8")
    ezList = [i for i in fEz.read().split("\n")]
    mdList = [i for i in fMd.read().split("\n")]
    dfList = [i for i in fDf.read().split("\n")]
    ezPicked = list()
    mdPicked = list()
    dfPicked = list()
    (ezList,ezPicked) = randomPickQs(ezList,ezPicked)
    (mdList,mdPicked) = randomPickQs(mdList,mdPicked)
    (dfList,dfPicked) = randomPickQs(dfList,dfPicked)
    return ezPicked + mdPicked + dfPicked

def showQues(quesNum,arr,guestName):
    global charName
    splitContents = arr[quesNum].split('$') #Categ,Ques,A,B,C,D,CORRECT
    notDecided = True
    showChoices = [True for i in range(4)]
    lifelineUsed = False
    while notDecided:
        if quesNum == 14:
            print("Now %s, your current money in the bank is Php %0.2f.\nFor the final question, which is worth Php 1000000.00, here is your question...\nThe category is %s.\n\n%s Question %d. %s\n" %(guestName,amtWinnings[quesNum],splitContents[0],difficultyStr[quesNum//5],int(quesNum)+1,splitContents[1]) )
        else:
            print("Your current money in the bank is Php %0.2f.\nNow %s, for Php %0.2f, here is your question.\nThe category is %s.\n\n%s Question %d. %s\n" %(amtWinnings[quesNum],guestName,amtWinnings[quesNum+1],splitContents[0],difficultyStr[quesNum//5],(int(quesNum)%5)+1,splitContents[1]) )
        for i in range(2,6):
            if showChoices[i-2]:
                print(splitContents[i])
        print("\nDo you want to:\nA. Pick an answer\nB. Use a lifeline\nC. Walk away with 1⁄2 of the earnings\n")
        ans = None
        #Getting input
        while not index.verifyInput(choice1,ans):
            ans = input("Choose (A,B,C): ")
            if not index.verifyInput(choice1,ans):
                print("Invalid input! Please try again!")
        #Choices
        if ans.upper() == 'A':
            print("You chose to pick an answer!")
            finalAns = None
            confirmationAns = False
            while not confirmationAns:
                while not index.verifyInput(choiceMain,finalAns):
                    finalAns = input("\nChoose an answer (A,B,C,D): ")
                    if (not index.verifyInput(choiceMain, finalAns)) or (not index.verifyInput([True], showChoices[ord(finalAns.upper())-65])):
                        print("Invalid Input! Please Try again!")
                        finalAns = None
                finalAns = finalAns.upper()
                if quesNum >= 5:
                    while not index.verifyInput(yesOrNo,confirmationAns):
                        confirmationAns = input("Is this your final answer? (Y for yes, N for No): ")
                        if not index.verifyInput(yesOrNo,confirmationAns):
                            print("Invalid Input! Please try again!\n")
                else:
                    confirmationAns = 'Y'
                if confirmationAns.upper() == 'Y':
                    notDecided = False
                    if finalAns == splitContents[6]:
                        print("The correct answer is %s! You are correct!"%(splitContents[ord(splitContents[6])-63]) )
                        return (True,1)
                    else:
                        print("I'm sorry to say, but your answer is wrong. The correct answer is %s." % (splitContents[ord(splitContents[6])-63]))
                        return (False,0.25)
                else:
                    print("Okay, I will repeat the question.\n----------------------------------------------------")
        #Use a lifeline
        elif ans.upper() == 'B':
            if not quesNum == 14:
                hasNoneLeft = True
                for i in range(4):
                    hasNoneLeft &= LLUsed[i]
                if hasNoneLeft:
                    print("There are no more lifelines left to be used! I will repeat the question.\n----------------------------------------------------\n")
                    continue
                print("Which lifeline would you want to use?\n\n"+(not LLUsed[0])*"A. Wise\n" + (not LLUsed[1])*"B. Unsure\n" + (not LLUsed[2])*"C. Arrogant\n" + (not LLUsed[3])*"D. 50/50\n")
                LL = None
                indLL = None
                while not index.verifyInput([True],LL):
                    try:
                        indLL = ord(input("Choose (A,B,C,D):").upper())-65
                        LL = LLUsed[indLL]
                    except:
                        print("Invalid input! Please try again!")
                        continue
                    if not index.verifyInput([False],LL):
                        print("Lifeline is not available! Please choose again!")
                        LL = None
                        indLL = None
                    else:
                        print("\nYou chose: ",LLs[indLL])
                        LLUsed[indLL] = True
                        break
                print("")
                if indLL == 0: #Wise 90% correct
                    n = random.randint(1,10)
                    if not n == 1: #probability of not 1 = 9/10 = 90%
                        #Help
                        print("Hi %s! Ang sagot pong naiisip ko ay %s. Sigurado po ako rito! :>" % (charName,splitContents[ord(splitContents[6])-63]))
                    else:
                        #NotHelp
                        ind = 2
                        while splitContents[ind] == splitContents[6] or not showChoices[ind-2]:
                            ind = random.randint(2,6)
                        print("Hi %s! Ang sagot pong naiisip ko ay %s. Sigurado po ako rito! :>" % (charName,splitContents[ind]))
                elif indLL == 1:
                    n = random.randint(1,2)
                    if n == 1: #probability of 1 = 1/2 = 50%
                        #Help
                        print("Hindi ako sigurado sa sasabihin ko, %s. Pero sa tingin ko ang sagot ay %s." %(charName,splitContents[ord(splitContents[6])-63]+"."))
                    else:
                        #NotHelp
                        ind = 2
                        while splitContents[ind] == splitContents[6] or not showChoices[ind-2]:
                            ind = random.randint(2,6)
                        print("Hindi ako sigurado sa sasabihin ko, %s. Pero sa tingin ko ang sagot ay %s." % (charName,splitContents[ind]))
                elif indLL == 2:
                    n = random.randint(1,10)
                    if n <= 3: #probability of (1,2,3) out of 10 = 3/10 = 30%
                        #Help
                        print("Oy %s! Ang hina mo naman at kailangan mo pa tulong ko 'no! Anyway, sa tingin ko ang sagot ay %s." %(charName,splitContents[ord(splitContents[6])-63]+"."))
                    else:
                        #NotHelp
                        ind = 2
                        while splitContents[ind] == splitContents[6] or not showChoices[ind-2]:
                            ind = random.randint(2,6)
                        print("Oy %s! Ang hina mo naman at kailangan mo pa tulong ko 'no! Anyway, sa tingin ko ang sagot ay %s." % (charName,splitContents[ind]))
                else:
                    #Choose two incorrect answers
                    rem1 = None
                    rem2 = None
                    arr = ['A','B','C','D']
                    arr.remove(splitContents[6])
                    rand = random.randint(0,2)
                    arr.pop()
                    for i in arr:
                        showChoices[ord(i)-65] = False
                print("You have used your lifeline! I will repeat the question.\n----------------------------------------------------")
            else:
                print("Lifelines cannot be used for the last question!\nI will repeat the question.\n----------------------------------------------------")
        #Babye
        else:
            notDecided = False
            return (False,0.5)

def startGame(name):
    global charName
    charName = name
    arr = preProcessQs()
    global quesNum
    alive = True
    quesNum = 0
    while alive and quesNum < 15:
        if quesNum == 0:
            print("----------------------------------------------------\n\t\t Easy Round!\n----------------------------------------------------")
        elif quesNum == 5:
            print("You have completed the Easy Round! Let us now play in the...\n----------------------------------------------------\n\t\tModerate Round!\n----------------------------------------------------")
        elif quesNum == 10:
            print("You have completed the Moderate Round! Let us now play in the...\n----------------------------------------------------\n\t\tHard Round!\n----------------------------------------------------")
        if quesNum > 0:
            if not quesNum%5 == 0:
                print("----------------------------------------------------")
            print("Your current money in the bank is Php %0.2f.\n\nDo you want to:\n\nA. Continue to play? or\nB. Walk away with your earnings?" % (amtWinnings[quesNum]))
            responsePlay = None
            while not index.verifyInput(aOrB,responsePlay):
                responsePlay = input("Choose (A or B): ")
                if not index.verifyInput(aOrB,responsePlay):
                    print("Invalid input! Please try again!\n")
            if responsePlay.upper() == "B":
                return (quesNum,1)
            else:
                print("----------------------------------------------------\nLET'S PLAY!")
        isCorrect,remaining = showQues(quesNum,arr,name)
        if not isCorrect:
            return (quesNum,remaining)
        else:
            quesNum += 1
    return (quesNum,1)
        

if __name__ == '__main__':
    (level,multiplier) = startGame("Al")
