from inspect import stack
from msvcrt import getwch, getwche
from random import choice
from threading import Thread
from time import time

from qol_mth import checkEven, clearConsole, sleep

#________________________________________________________________________________________________________________________________

def moveChoice():
    global borderHit
    global lastDirec
    button = getwch() #takes a single character input and saves it as button

    if button.islower():
        if button == keyMap[0]: 
            if playArea[snekPos[0] - columns] == "═": borderHit = True
            else: borderHit = False
            if lastDirec != 2 and borderHit == False and checkIfEatSelf(-columns) == False: moveUp()
        elif button == keyMap[2]:  
            if playArea[snekPos[0] + columns] == "═": borderHit = True
            else: borderHit = False
            if lastDirec != 1 and borderHit == False and checkIfEatSelf(columns) == False: moveDown() 
        elif button == keyMap[1]:
            if playArea[snekPos[0] - 2] == "═": borderHit = True
            else: borderHit = False 
            if lastDirec != 4 and borderHit == False and checkIfEatSelf(-1) == False: moveLeft() 
        elif button == keyMap[3]: 
            if playArea[snekPos[0] + 3] == "═": borderHit = True
            else: borderHit = False 
            if lastDirec != 3 and borderHit == False and checkIfEatSelf(2) == False: moveRight()

    elif button.isupper():
        button = button.lower()
        if button == keyMap[0]: 
            if playArea[snekPos[0] -  columns] == "═": borderHit = True
            else: borderHit = False
            if lastDirec != 2 and borderHit == False and checkIfEatSelf(-columns) == False: moveUp()

            if playArea[snekPos[0] -  columns] == "═":borderHit = True
            else: borderHit = False
            if lastDirec != 2 and borderHit == False and checkIfEatSelf(-columns) == False: moveUp() 
        elif button == keyMap[2]: 
            if playArea[snekPos[0] +  columns] == "═":borderHit = True
            else: borderHit = False
            if lastDirec != 1 and borderHit == False and checkIfEatSelf(columns) == False: moveDown() 

            if playArea[snekPos[0] +  columns] == "═":borderHit = True
            else: borderHit = False
            if lastDirec != 1 and borderHit == False and checkIfEatSelf(columns) == False: moveDown() 
        elif button == keyMap[1]: 
            if playArea[snekPos[0] - 2] == "═": borderHit = True
            else: borderHit = False 
            if lastDirec != 4 and borderHit == False and checkIfEatSelf(-1) == False: moveLeft() 

            if playArea[snekPos[0] - 2] == "═": borderHit = True
            else: borderHit = False 
            if lastDirec != 4 and borderHit == False and checkIfEatSelf(-1) == False: moveLeft() 
        elif button == keyMap[3]: 
            if playArea[snekPos[0] + 3] == "═": borderHit = True
            else: borderHit = False 
            if lastDirec != 3 and borderHit == False and checkIfEatSelf(2) == False: moveRight()

            if playArea[snekPos[0] + 3] == "═": borderHit = True
            else: borderHit = False 
            if lastDirec != 3 and borderHit == False and checkIfEatSelf(2) == False: moveRight()

def moveUp(): 
    global snekPos
    global playArea
    global lastDirec ; lastDirec = 1

    for i in range(0, len(snekPos)):
        playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ") #replace the item at the loc of the snake with a space
        playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ") #the snake is 2 chars wide

    checkFruit(snekPos[0] - columns) #conditional for direction

    snekPos.pop(-1)
    snekPos.insert(0, snekPos[0] - columns) #conditional for direction
    
    for i in range(0, len(snekPos)): 
        if i == 0: 
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "◘") 
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "◘") 
        else:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█") #adds our snek back into the terminal
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█") #adds second snek char bak in    
def moveDown():
    global snekPos
    global playArea
    global lastDirec ; lastDirec = 2
    
    for i in range(0, len(snekPos)):
        playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ") #replace the item at the loc of the snake with a space
        playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ") #the snake is 2 chars wide

    checkFruit(snekPos[0] + columns) #conditional for direction

    snekPos.pop(-1)
    snekPos.insert(0, snekPos[0] + columns) #conditional for direction

    for i in range(0, len(snekPos)): 
        if i == 0: 
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "◘") 
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "◘") 
        else:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█") #adds our snek back into the terminal
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█") #adds second snek char bak in 
def moveLeft():
    global snekPos
    global playArea
    global lastDirec ; lastDirec = 3
    
    for i in range(0, len(snekPos)):
        playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ") #replace the item at the loc of the snake with a space
        playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ") #the snake is 2 chars wide

    checkFruit(snekPos[0] - 2) #conditional for direction

    snekPos.pop(-1)
    snekPos.insert(0, snekPos[0] - 2) #conditional for direction

    for i in range(0, len(snekPos)): 
        if i == 0: 
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "◘") 
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "◘") 
        else:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█") #adds our snek back into the terminal
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█") #adds second snek char bak in  
def moveRight():
    global snekPos
    global playArea
    global lastDirec ; lastDirec = 4
    
    for i in range(0, len(snekPos)):
        playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ") #replace the item at the loc of the snake with a space
        playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ") #the snake is 2 chars wide

    checkFruit(snekPos[0] + 2) #conditional for direction

    snekPos.pop(-1)
    snekPos.insert(0, snekPos[0] + 2) #conditional for direction

    for i in range(0, len(snekPos)): 
        if i == 0: 
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "◘") 
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "◘") 
        else:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█") #adds our snek back into the terminal
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█") #adds second snek char bak in   

"""def preLoad():
    getwch()
    n1 = 1 ; n2 = 1 ; cent = 1
    for i in range(10):
        square = "█"*(i+1) ; line = "─"*36 ; spaces = " "*(30 - ((i+1)*3))
        if cent < 10: spaces = spaces + " " ; print("", end=f"\r\n\t╓{line}╖\n\t║ {cent}% {square}{square}{square} {spaces}║\n\t╙{line}╜")
        cent = n1 + n2 ; n1 = n2 ; n2 = cent
        sleep(400) ; clearConsole()
    print("", end=f"\r\n\t╓{line}╖\n\t║ {98}% {square}{square}{square} {spaces}║\n\t╙{line}╜")
    sleep(400) ; getwch() ; clearConsole()"""
def start():
    clearConsole()
    global userName ; userName = input("\n\tHello!\n\tPlease enter your name: ") #asks the user for a name 
    clearConsole() #then clears
    print("\n\tThanks!")#says thanks b/c niceties
    sleep(400)
    clearConsole() 

    global userContact ; userContact = "" #userContact = input("\n\tPlease enter a phone number: ")
    #clearConsole() 
    #print("\n\tThanks!")
    #sleep(400)
    #clearConsole()

    global userScore ; userScore = 1
    sleep(400)
    clearConsole()
    print("\n\n\tPress any key to start...")
    #sortScores() 

    possSecret = getwch()
    if possSecret == "C": printCredits()
    elif possSecret == "Q": asignCustomButtons() 
    else: 
        global keyMap
        if "&" in userName or "+" in userName: keyMap = ["w", "k", "s", "l"]
        else: keyMap = ["w", "a", "s", "d"]
def printCredits():
    clearConsole()
    print("", end=f"\r\n\tThanks to al") ; sleep(798)
    print("", end=f"\r\tThanks to all the people who he") ; sleep(798)
    print("", end=f"\r\tThanks to all the people who helped with Snek") ; sleep(798)
    print("", end=f"\r\n\n\tCRED") ; sleep(467)
    print("", end=f"\r\tCREDITS:\t") ; sleep(798)
    print("", end=f"\r\n\t\tMain C0d3in") ; sleep(798)
    print("", end=f"\r\t\tMain C0d3ing: Max Harrison") ; sleep(798)
    print("", end=f"\r\n\t\tMaking 'Our' Ga") ; sleep(798)
    print("", end=f"\r\t\tMaking 'Our' Game: Maciej Lewko") ; sleep(798)
    print("", end=f"\r\n\t\tWWYISTS Moveme") ; sleep(798)
    print("", end=f"\r\t\tWWYISTS Movement C0d3: Callum Bl") ; sleep(798)
    print("", end=f"\r\t\tWWYISTS Movement C0d3: Callum Blumfield") ; sleep(798)
    print("", end=f"\r\n\t\tTitle Scree") ; sleep(798)
    print("", end=f"\r\t\tTitle Screen Art: Jake Cu") ; sleep(798)
    print("", end=f"\r\t\tTitle Screen Art: Jake Cuthbertson") ; sleep(798)
    print("", end=f"\r\n\t\tMoral Suppor") ; sleep(798)
    print("", end=f"\r\t\tMoral Support: Quandale Dingle") ; sleep(798)
    print("", end=f"\r\n\t\tRandom Cod") ; sleep(798)
    print("", end=f"\r\t\tRandom Code: The Inter") ; sleep(798)
    print("", end=f"\r\t\tRandom Code: The Internet At Large") ; sleep(798)
    print("", end=f"\r\n\n\t\tAlso the devs of Pyt") ; sleep(798)
    print("", end=f"\r\t\tAlso the devs of Python, AHK, VS Code") ; sleep(798)
    print("", end=f"\r\n\n\tThank You F!") ; sleep(798)
    print("", end=f"\r\tThank You For Playing!") ; sleep(798)
    getwch()
    clearConsole()
    global keyMap ; keyMap = ["w", "a", "s", "d"]
def asignCustomButtons():
    global keyMap
    clearConsole()
    keyMap = []
        
    def mapToUp():
        print("", end=f"\n\n\tPress the key you wish to be up: ")
        tempChar = getwche()
        if tempChar.isalpha() == True: keyMap.append(tempChar)
        else: 
            clearConsole()
            print("\n\t\tMust be a letter")
            mapToUp()

    def mapToLeft():
        print("", end=f"\n\n\tPress the key you wish to be left: ")
        tempChar = getwche()
        if tempChar.isalpha() == True: keyMap.append(tempChar)
        else: 
            clearConsole()
            print("\n\t\tMust be a letter")
            mapToLeft()
    
    def mapToDown():
        print("", end=f"\n\n\tPress the key you wish to be down: ")
        tempChar = getwche()
        if tempChar.isalpha() == True: keyMap.append(tempChar)
        else: clearConsole()
        print("\n\t\tMust be a letter")
        mapToDown()
    def mapToRight():
        print("", end=f"\n\n\tPress the key you wish to be right: ")
        tempChar = getwche()
        if tempChar.isalpha() == True: keyMap.append(tempChar)
        else: clearConsole()
        print("\n\t\tMust be a letter")
        mapToRight()

    mapToUp()
    mapToLeft()
    mapToDown()
    mapToRight()


    print("", end=f"\n\n\tYou have set your controls to: ")
    for key in keyMap:
        try: print('', end=f'{keyMap[key].upper()}')
        except: print('', end=f'{keyMap[key]}')
    print("", end=f"\n\n\tPress shift to go faster")
    print("\n\tPress any key to continue... ")
    getwch()
    clearConsole()

def scoreCheck(currentScore): global userScore ; userScore = currentScore + 1 #sorry for global
def checkFruit(fruitLoc):
    global snekPos
    if checkEven(fruitLoc) == 0: fruitLocTheSecond = fruitLoc - 1 #checks even or odd (b/c 2 wide snek)
    else: fruitLocTheSecond = fruitLoc + 1 
    
    if playArea[fruitLoc] == "♦" or playArea[fruitLocTheSecond] == "♦": #if the next loc is where the fruit is
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, " ") #remove it & replace it
        #fruitLoc = randint(columns, len(playArea) - columns) #selects random loc from list
        fruitLoc = choice(fruitArea)
        while playArea[fruitLoc] == "█" or playArea[fruitLoc] == "◘" or playArea[fruitLoc] == "═": #while bad num
            #fruitLoc = randint(columns, len(playArea) - columns)
            fruitLoc = choice(fruitArea)
        playArea.pop(playArea[fruitLoc]) ; playArea.insert(playArea[fruitLoc], "♦") #remove whatever is there & add a fruit
        scoreCheck(userScore) #increase the score (yes ik name is misleading, shut up)
        
        call = stack()[1].function # Ayman Hourieh & Ma0 on stackoverflow: https://stackoverflow.com/a/900404
        if call == 'moveUp': direcFromCall_forGetLongER = -columns
        elif call == 'moveDown': direcFromCall_forGetLongER = columns
        elif call == 'moveLeft': direcFromCall_forGetLongER = -2
        elif call == 'moveRight': direcFromCall_forGetLongER = 2

        #clearConsole() ; print(snekPos[len(snekPos)-1]) ; print((snekPos[len(snekPos)-1]+direcFromCall_forGetLongER)) ; getwch()
        snekPos.append(snekPos[len(snekPos)-1]+direcFromCall_forGetLongER +1) #this hurt ma brain
def checkIfEatSelf(direcFromCall_forNotEatingSelf): 
    if playArea[snekPos[0] + direcFromCall_forNotEatingSelf] == "█" or playArea[snekPos[0] + direcFromCall_forNotEatingSelf] == "◘": 
        #return True #
        endPoint(userName, userScore, userContact, "eatSelf")
    else: return False

def printSmol(startPoint): #b/c it zooms so retricts scrn size
    clearConsole()
    # OLD   print("".join(playArea[0:62])) ; print("".join(playArea[62:124])) ; print("".join(playArea[124:186])) ; print("".join(playArea[186:248])) ; print("".join(playArea[248:310])) ; print("".join(playArea[310:373])) ; print("".join(playArea[372:434])) ; print("".join(playArea[434:496])) ; print("".join(playArea[496:558])) ; print("".join(playArea[558:620])) ; print("".join(playArea[620:682])) ; print("".join(playArea[682:744])) ; print("".join(playArea[744:806])) ; print("".join(playArea[806:]))
    print("".join(playArea[0:62]),'\n',"".join(playArea[62:124]),'\n',"".join(playArea[124:186]),'\n',"".join(playArea[186:248]),'\n',"".join(playArea[248:310]),'\n',"".join(playArea[310:373]),'\n',"".join(playArea[372:434]),'\n',"".join(playArea[434:496]),'\n',"".join(playArea[496:558]),'\n',"".join(playArea[558:620]),'\n',"".join(playArea[620:682]),'\n',"".join(playArea[682:744]),'\n',"".join(playArea[744:806]),'\n',"".join(playArea[806:]))
    #print(playArea[0:62]) ; print(playArea[62:124]) ; print(playArea[124:186]) ; print(playArea[186:248]) ; print(playArea[248:310]) ; print(playArea[310:372]) ; print(playArea[372:434]) ; print(playArea[434:496]) ; print(playArea[496:558]) ; print(playArea[558:620]) ; print(playArea[620:682]) ; print(playArea[682:744]) ; print(playArea[744:806]) ; print(playArea[806:])
    #print(playArea)

    #messy

    timer = str(60 - (time() - startPoint))[:2]
    if timer.endswith("."): 
        timer = timer[:1] #lol bad formatting
    print("\t",userName," Score:", userScore," Timer:", timer,"\n\t\tKeys:"," ".join(keyMap).upper())
def endPoint(name, score, contact, reason="end"): 
    if "&" in name or "+" in name: score = score * 1.5
    if name != "dubug":
        log = open("Scores.txt", "a")
        log.write(f"\n{score:02} {name} {contact} \n")
        log.close()
        sortScores()
        if reason == "eatSelf": 
            clearConsole()
            print(f"\n\n\tRemember, don't eat yourself!\n\tYou got a score of {score}")
        elif reason == "end": 
            clearConsole()
            print(f"\n\n\tThe End! You got a score of {score}")
        else: 
            clearConsole()
            print(f"\n\n\t endForced// {name} {score}")
    while True: pass
def sortScores(): #https://stackoverflow.com/q/12330522
    lines = open("Scores.txt",'r').readlines()
    lines.sort(reverse=True)
    infile = open("Scores.txt", "w")
    for i in lines: infile.writelines(i)
    infile.close()

#________________________________________________________________________________________________________________________________

if __name__ == '__main__':
    
    global lastDirec ; lastDirec = 1
    borderHit = False #is snek next to border

    columns = 62
    lines = 16
    area = columns * lines

    playArea = [] #creates a blank list for the chars to go in & then creates borders
    for i in range(0, columns): playArea.append("═")
    for i in range(0, (area - 4 * columns)): playArea.append(" ")
    for i in range(0, columns): playArea.append("═")

    fruitArea = [700, (4 * lines) + 49, (9 * lines) + 59, (6 * lines) + 31, (13 * lines) + 15, 570, 660] #places for the fruit to be

    playArea.pop(area // 5) ; playArea.insert(area // 5, "♦") #removes the character needed & adds 'fruit' to list
    snekPos = [227, 289] #locs of snek segments

    #________________________________________________________________________________________________________________________________

    clearConsole() #wipes the console to start
    #SNAEK rather than SNAKE #print("══════════════════════════════════════════════════════════════\n                                                              \n         _______  _        _______  _______  _                \n        (  ____ \( (    /|(  ___  )(  ____ \| \    /\         \n        | (    \/|  \  ( || (   ) || (    \/|  \  / /         \n        | (_____ |   \ | || (___) || (__    |  (_/ /          \n        (_____  )| (\ \) ||  ___  ||  __)   |   _ (           \n              ) || | \   || (   ) || (      |  ( \ \          \n        /\____) || )  \  || )   ( || (____/\|  /  \ \         \n        \_______)|/    )_)|/     \|(_______/|_/    \/         \n                                                              \n                                                              \n══════════════════════════════════════════════════════════════\n        < Press Any Key To Start >                            \n                                                              \n")
    print("══════════════════════════════════════════════════════════════\n                                                              \n         _______  _        _______  _        _______                  \n        (  ____ \( (    /|(  ___  )| \    /\(  ____ \        \n        | (    \/|  \  ( || (   ) ||  \  / /| (    \/        \n        | (_____ |   \ | || (___) ||  (_/ / | (__              \n        (_____  )| (\ \) ||  ___  ||   _ (  |  __)              \n              ) || | \   || (   ) ||  ( \ \ | (                \n        /\____) || )  \  || )   ( ||  /  \ \| (____/\         \n        \_______)|/    )_)|/     \||_/    \/(_______/         \n                                                              \n                                                              \n══════════════════════════════════════════════════════════════\n        < Press Any Key To Start >                            \n                                                              \n")
    sleep(500)
    getwch()

    start()

    startPoint = time()
    moveUp()
    printSmol(startPoint)

    #________________________________________________________________________________________________________________________________

    class BackgroundTimer(Thread): #0fxe on StackOverflow: https://stackoverflow.com/a/2223191
        def run(self):
            while time() - startPoint < 60:
                sleep(1000)
                printSmol(startPoint)
            endPoint(userName, userScore, userContact, "end")
    timer = BackgroundTimer()
    timer.start()

    while time() - startPoint < 60: 
        moveChoice()
        printSmol(startPoint)
    endPoint(userName, userScore, userContact, "end")
