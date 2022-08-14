from qol_mth import sleep, clearConsole, checkEven
from random import choice
from msvcrt import getwch, getwche
from inspect import stack

def moveChoice():
    global borderHit ; global lastDirec
    button = getwch() #takes a single character input and saves it as button
    
    if button.isupper() == False:
        if button == keyMap["upKey"]: 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveUp() if lastDirec != 2 and borderHit == False and checkIfEatSelf(-columns) == False else sleep(1) 
        elif button == keyMap["downKey"]: 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveDown() if lastDirec != 1 and borderHit == False and checkIfEatSelf(columns) == False else sleep(1)
        elif button == keyMap["leftKey"]: moveLeft() if lastDirec != 4 and checkIfEatSelf(-2) == False else sleep(1)
        elif button == keyMap["rightKey"]: moveRight() if lastDirec != 3 and checkIfEatSelf(2) == False else sleep(1)
        else: pass

    elif button.isupper() == True:
        button = button.lower()
        if button == keyMap["upKey"]: 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveUp() if lastDirec != 2 and borderHit == False and checkIfEatSelf(-columns) == False else sleep(1) ; moveUp() if lastDirec != 2 and borderHit == False and checkIfEatSelf(-columns) == False else sleep(1)  
        elif button == keyMap["downKey"]: 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═":borderHit = True ; break
                else: borderHit = False
            moveDown() if lastDirec != 1 and borderHit == False and checkIfEatSelf(columns) == False else sleep(1) ; moveDown() if lastDirec != 1 and borderHit == False and checkIfEatSelf(columns) == False else sleep(1)
        elif button == keyMap["leftKey"]: moveLeft() if lastDirec != 4 and checkIfEatSelf(-2) == False else sleep(1); moveLeft() if lastDirec != 4 and checkIfEatSelf(-2) == False else sleep(1)
        elif button == keyMap["rightKey"]: moveRight() if lastDirec != 3 and checkIfEatSelf(2) == False else sleep(1); moveRight() if lastDirec != 3 and checkIfEatSelf(2) == False else sleep(1)
        else: pass

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

    try: playArea.index("♦") #sees if it can find the fruit (b/c the rand is from the list so the fruit might not change loc and therefore get replaced by the snek so char don't exist anymore and will raise an error)
    except: #if fruit didn't change place (error raised)
        fruitLoc = choice(places) #choose another rand loc 
        while playArea[fruitLoc] == "█": fruitLoc = choice(places) #whilst the new loc is taken by snek, reroll loc 
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #remove the char here & replaces it w the fruit
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

    try: playArea.index("♦") #sees if it can find the fruit (b/c the rand is from the list so the fruit might not change loc and therefore get replaced by the snek so char don't exist anymore and will raise an error)
    except: #if fruit didn't change place (error raised)
        fruitLoc = choice(places) #choose another rand loc 
        while playArea[fruitLoc] == "█": fruitLoc = choice(places) #whilst the new loc is taken by snek, reroll loc 
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #remove the char here & replaces it w the fruit
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

    try: playArea.index("♦") #sees if it can find the fruit (b/c the rand is from the list so the fruit might not change loc and therefore get replaced by the snek so char don't exist anymore and will raise an error)
    except: #if fruit didn't change place (error raised)
        fruitLoc = choice(places) #choose another rand loc 
        while playArea[fruitLoc] == "█": fruitLoc = choice(places) #whilst the new loc is taken by snek, reroll loc 
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #remove the char here & replaces it w the fruit
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

    try: playArea.index("♦") #sees if it can find the fruit (b/c the rand is from the list so the fruit might not change loc and therefore get replaced by the snek so char don't exist anymore and will raise an error)
    except: #if fruit didn't change place (error raised)
        fruitLoc = choice(places) #choose another rand loc 
        while playArea[fruitLoc] == "█": fruitLoc = choice(places) #whilst the new loc is taken by snek, reroll loc 
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #remove the char here & replaces it w the fruit

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
    clearConsole() #wipes the console to start
    global userName ; userName = input("\n\tHello!\n\tPlease enter your name: ") ; clearConsole() #asks the user for a name then clears
    print("\n\tThanks!") ; sleep(400) ; clearConsole() #says thanks b/c niceties
    global userContact ; userContact = input("\n\tPlease enter an email address\n\t\t or phone number: ") ; clearConsole() 
    print("\n\tThanks!") ; sleep(400) ; clearConsole()
    global userScore; userScore = 1 #it works - I'm not changing it (yet)
    file = open("msg.txt", "w") ; file.write("") ; file.close()
    asignButtons()
    print("\n\tThanks!") ; sleep(400) ; clearConsole()#says thanks b/c niceties
    print("_"*62,"\n\n\tPress any key to start...") # line for measuring scrn size 
    sortScores() 
    getwch()
def asignButtons():
    global keyMap
    clearConsole()
    def askForMap(): 
        global chooseMap ; chooseMap = input("\n\n\tPlease select a control scheme:\n\t\t1) WASD, 2) ESDF, 3) IJKL, 4) QAOP\n\t\t\t5) Custon Binds\n\n\t\t").lower()
        if chooseMap is None: askForMap()
    askForMap()

    if "1" in chooseMap or "wasd" in chooseMap: 
        keyMap = {"upKey": "w", "leftKey": "a", "downKey": "s", "rightKey": "d"}
        file = open("msg.txt", "w") ; file.write("asigned") ; file.close()
    elif "2" in chooseMap or "esdf" in chooseMap: 
        keyMap = {"upKey": "e", "letfKey": "s", "downKey": "d", "rightKey": "f"}
        file = open("msg.txt", "w") ; file.write("asigned") ; file.close()
    elif "3" in chooseMap or "ijkl" in chooseMap: 
        keyMap = {"upKey": "i", "leftKey": "j", "downKey": "k", "rightKey": "l"}
        file = open("msg.txt", "w") ; file.write("asigned") ; file.close()
    elif "4" in chooseMap or "qaop" in chooseMap: 
        keyMap = {"upKey": "q", "leftKey": "o", "downKey": "a", "rightKey": "p"}
        file = open("msg.txt", "w") ; file.write("asigned") ; file.close()
    else: 
        clearConsole()
        keyMap = {"upKey", "downKey", "leftKey", "rightKey"}
        
        def mapToUp():
            global keyMap
            print("", end=f"\n\n\tPress the key you wish to be up: ") ; tempUp = getwche()
            if tempUp.isalpha(): keyMap.update({"upKey": tempUp})
            else: 
                print("\n\tPlease pick a letter,\n\tnot a number or symbol")
                sleep(2000)
                clearConsole()
                mapToUp()
        def mapToLeft():
            global keyMap
            print("", end=f"\n\n\tPress the key you wish to be left: ") ; tempLeft = getwche()
            if tempLeft.isalpha(): keyMap.update({"leftKey": tempLeft})
            else: 
                print("\n\tPlease pick a letter,\n\tnot a number or symbol")
                sleep(2000)
                clearConsole()
                mapToLeft()
        def mapToDown():
            global keyMap
            print("", end=f"\n\n\tPress the key you wish to be down: ") ; tempDown = getwche()
            if tempDown.isalpha(): keyMap.update({"downKey": tempDown})
            else: 
                print("\n\tPlease pick a letter,\n\tnot a number or symbol")
                sleep(2000)
                clearConsole()
                mapToDown()
        def mapToRight():
            global keyMap
            print("", end=f"\n\n\tPress the key you wish to be right: ") ; tempRight = getwche()
            if tempRight.isalpha(): keyMap.update({"rightKey": tempRight})
            else: 
                print("\n\tPlease pick a letter,\n\tnot a number or symbol")
                sleep(2000)
                clearConsole()
                mapToDown()
        
        mapToUp()
        mapToLeft()
        mapToDown()
        mapToRight()
        file = open("msg.txt", "w") ; file.write("asigned") ; file.close()
    print("", end=f"\n\n\tYou have set your controls to: ")
    print('', end=f'{keyMap["upKey"].upper()}')
    print('', end=f'{keyMap["leftKey"].upper()}')
    print('', end=f'{keyMap["downKey"].upper()}')
    print('', end=f'{keyMap["rightKey"].upper()}')
    print("\n\tPress any key to continue... ") ; getwch() ; clearConsole()

def scoreCheck(currentScore): global userScore ; userScore = currentScore + 1 #sorry for global
def checkFruit(fruitLoc):
    global snekPos
    fruitLocTheSecond = fruitLoc - 1 if checkEven(fruitLoc) == 0 else fruitLoc + 1 #checks even or odd (b/c 2 wide snek)
    if playArea[fruitLoc] == "♦" or playArea[fruitLocTheSecond] == "♦": #if the next loc is where the fruit is
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, " ") #remove it & replace it
        fruitLoc = choice(places) #selects random loc from list
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #remove whatever is there & add a fruit
        scoreCheck(userScore) #increase the score (yes ik name is misleading, shut up)
        
        call = stack()[1].function # thanks Ayman Hourieh & Ma0 on stackoverflow for this: https://stackoverflow.com/a/900404
        if call == 'moveUp': direcFromCall_forGetLongER = -columns
        elif call == 'moveDown': direcFromCall_forGetLongER = columns
        elif call == 'moveLeft': direcFromCall_forGetLongER = -2
        elif call == 'moveRight': direcFromCall_forGetLongER = 2

        #clearConsole() ; print(snekPos[len(snekPos)-1]) ; print((snekPos[len(snekPos)-1]+direcFromCall_forGetLongER)) ; getwch()
        snekPos.append(snekPos[len(snekPos)-1]+direcFromCall_forGetLongER +1) #this hurt ma brain
def checkIfEatSelf(direcFromCall_forNotEatingSelf): 
    if playArea[snekPos[0] + direcFromCall_forNotEatingSelf] == "█": endPoint(userName, userScore, userContact, "eatSelf") ; return True #endPoint(userName, userScore, userContact, "eatSelf") ;
    else: return False

def printSmol(): #b/c it zooms so retricts scrn size
    clearConsole()
    print("".join(playArea[0:62])) ; print("".join(playArea[62:124])) ; print("".join(playArea[124:186])) ; print("".join(playArea[186:248])) ; print("".join(playArea[248:310])) ; print("".join(playArea[310:373])) ; print("".join(playArea[372:434])) ; print("".join(playArea[434:496])) ; print("".join(playArea[496:558])) ; print("".join(playArea[558:620])) ; print("".join(playArea[620:682])) ; print("".join(playArea[682:744])) ; print("".join(playArea[744:806])) ; print("".join(playArea[806:]))
    #print(playArea[0:62]) ; print(playArea[62:124]) ; print(playArea[124:186]) ; print(playArea[186:248]) ; print(playArea[248:310]) ; print(playArea[310:372]) ; print(playArea[372:434]) ; print(playArea[434:496]) ; print(playArea[496:558]) ; print(playArea[558:620]) ; print(playArea[620:682]) ; print(playArea[682:744]) ; print(playArea[744:806]) ; print(playArea[806:])
    #print(playArea)
    try: print("\t",userName," ",userScore) #tries to print name
    except: print("\t",userScore) #if it can't for whatever reason don't bother
def endPoint(name, score, contact, reason): 
    if "&" in userName or "+" in userName: userScore = userScore * 2
    file.close() ; log = open("Scores.txt", "a") ; log.write(f"\n{score:02} {name} {contact} \n") ; log.close() ; sortScores()
    if reason == "eatSelf": 
        clearConsole() ; print(f"\n\tRemember, don't eat yourself!\n\tYou got a score of {userScore}")
    elif reason == "end": 
        clearConsole() ; print(f"\n\tThe End! You got a score of {userScore}")
    else: 
        clearConsole() ; print(f"\n\tendForce// {userName} {userScore}")
def sortScores(): #https://stackoverflow.com/q/12330522
    lines = open("Scores.txt",'r').readlines()
    lines.sort(reverse=True)
    infile = open("Scores.txt", "w")
    for i in lines: infile.writelines(i)
    infile.close()

global lastDirec ; lastDirec = 1
borderHit = False #is snek next to border
#preLoad() #just a little animation that isn't finished
start()

columns = 62 ; lines = 16 ; area = columns * lines ; area = area - columns * 2 #fixed area size for zoomed terminal & works out the amount of chars on the screen
playArea = [] #creates a blank list for the chars to go in & then creates borders
for i in range(0, columns): playArea.append("═")
for i in range(0, (area - 2 * columns)): playArea.append(" ")
for i in range(0, columns): playArea.append("═")

#playArea.pop(area // 3) ; playArea.insert(area // 3, "█") #remove the character halfway though the list & adds our 'snake' to the list
#playArea.pop(area // 3 + 1) ; playArea.insert(area // 3 + 1, "█")  #2wide snek
playArea.pop(area // 5) ; playArea.insert(area // 5, "♦") #removes the character needed & adds 'fruit' to list
printSmol() #print it to the terminal

places = [700, (4 * lines) + 49, (9 * lines) + 59, (6 * lines) + 31, (13 * lines) + 15, 570, 660] #places for the fruit to be
snekPos = [227, 289] #locs of snek segments

file = open("msg.txt", "w") ; file.write("") ; file.close()

moveUp() ; printSmol()
while True: 
    moveChoice() ; printSmol() ; file = open("msg.txt") 
    if file.read() == "end": file.close() ; endPoint(userName, userScore, userContact, "end") ; break
    else: file.close()

while True: pass