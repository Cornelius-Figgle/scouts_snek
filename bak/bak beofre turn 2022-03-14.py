from qol_mth import sleep, clearConsole, checkEven
from time import time as since
from random import choice
from msvcrt import getwch, kbhit
from inspect import stack

def moveChoice():
    global borderHit
    button = getwch() #takes a single character input and saves it as button
    if button == "N": quit()
    if spectrumMode == False: #if the user wants default controls (WASD)
        if button == "w": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveUp() if borderHit == False else sleep(1) 
        elif button == "s": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═":borderHit = True ; break
                else: borderHit = False
            moveDown() if borderHit == False else sleep(1)
        elif button == "a": moveLeft()
        elif button == "d": moveRight()
        elif button == "W": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveUp() if borderHit == False else sleep(1) ; moveUp() if borderHit == False else sleep(1) 
        elif button == "S": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═":borderHit = True ; break
                else: borderHit = False
            moveDown() if borderHit == False else sleep(1) ; moveDown() if borderHit == False else sleep(1) 
        elif button == "A": moveLeft() ; moveLeft() ; moveLeft() 
        elif button == "D": moveRight() ; moveRight() ; moveRight() 
    
    else: #if the user wants the controls to be WAOP rather than WASD
        if button == "w":
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveUp() if borderHit == False else sleep(1) 
        elif button == "a": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveDown() if borderHit == False else sleep(1)
        elif button == "o": moveLeft()
        elif button == "p": moveRight()
        elif button == "W": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveUp() if borderHit == False else sleep(1) ; moveUp() if borderHit == False else sleep(1) 
        elif button == "A": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═": borderHit = True ; break
                else: borderHit = False
            moveDown() if borderHit == False else sleep(1) ; moveDown() if borderHit == False else sleep(1) 
        elif button == "O": moveLeft() ; moveLeft() ; moveLeft() 
        elif button == "P": moveRight() ; moveRight() ; moveRight() 
def autoMoveChoice(button, direction):
    if button == "N": quit() #closes the app
    if spectrumMode == False: #if the user wants the defualt controls (WASD)
        if button == "w": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            direction = 1 if borderHit == False else sleep(1) 
        elif button == "s": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═": borderHit = True ; break
                else: borderHit = False
            direction = 2 if borderHit == False else sleep(1)
        elif button == "a": direction = 3
        elif button == "d": direction = 4
        elif button == "W": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            direction = 5 if borderHit == False else sleep(1) ; direction = 5 if borderHit == False else sleep(1) 
        elif button == "S":
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═": borderHit = True ; break
                else: borderHit = False
            direction = 6 if borderHit == False else sleep(1) ; direction = 6 if borderHit == False else sleep(1) 
        elif button == "A": direction = 7 
        elif button == "D": direction = 8     
    
    else: #if the user wants the controls to be WAOP rather than WASD
        if button == "w": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            direction = 1 if borderHit == False else sleep(1) 
        elif button == "a": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═": borderHit = True ; break
                else: borderHit = False
            direction = 2 if borderHit == False else sleep(1)
        elif button == "o": direction = 3
        elif button == "p": direction = 4
        elif button == "W": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] -  columns] == "═": borderHit = True ; break
                else: borderHit = False
            direction = 5 if borderHit == False else sleep(1) ; direction = 5 if borderHit == False else sleep(1) 
        elif button == "A": 
            for i in range(0,len(snekPos)): 
                if playArea[snekPos[i] +  columns] == "═": borderHit = True ; break
                else: borderHit = False
            direction = 6 if borderHit == False else sleep(1) ; direction = 6 if borderHit == False else sleep(1) 
        elif button == "O": direction = 7
        elif button == "P": direction = 8 
def autoMovePuter():
    if direction == 1: moveUp()
    elif direction == 2: moveDown()
    elif direction == 3: moveLeft()
    elif direction == 4: moveRight() 
    elif direction == 5: moveUp() ; moveUp()
    elif direction == 6: moveDown() ; moveDown()
    elif direction == 7: moveLeft() ; moveLeft() ; moveLeft() 
    elif direction == 8: moveRight() ; moveRight() ; moveRight()

def moveUp(): 
    global snekPos
    global playArea

    for i in range(0, len(snekPos) + 1, 2): #repeats for the amount of locs in snekPos but in intervals of 2, b/c every other item in the list is the pos
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ") #replace the item at the loc of the snake with a space
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ") #the snake is 2 chars wide
        except: break
    
    checkFruit(snekPos[0] - columns) #conditional for direction
    

    for i in range(1, len(snekPos) + 1, 2): #alternate of above code
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i - 1]) #remove the 'where next' items and replaces it with the higher segment
        except: break
    for i in range(0, len(snekPos) + 1, 2): #alternate of previous, same as original
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i] - columns) #conditional for direction, removes the item w. the current loc of snke and replaces it w. the loc of one space above in the terminal
        except: break

    for i in range(0, len(snekPos) + 1, 2): #same as first fn
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█") #adds our snek back into the terminal
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█") #adds second snek char bak in
        except: break

    try: playArea.index("♦") #sees if it can find the fruit (b/c the rand is from the list so the fruit might not change loc and therefore get replaced by the snek so char don't exist anymore and will raise an error)
    except: #if fruit didn't change place (error raised)
        fruitLoc = choice(places) #choose another rand loc 
        while playArea[fruitLoc] == "█": fruitLoc = choice(places) #whilst the new loc is taken by snek, reroll loc 
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #remove the char here & replaces it w the fruit
def moveDown():
    global snekPos
    global playArea
    
    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ")
        except: break

    checkFruit(snekPos[0] + columns) #conditional

    for i in range(1, len(snekPos) + 1, 2):
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i - 1])
        except: break
    for i in range(0, len(snekPos) + 1, 2):
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i] + columns)#conditional
        except: break

    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█")
        except: break

    try: playArea.index("♦")
    except:
        fruitLoc = choice(places)
        while playArea[fruitLoc] == "█": fruitLoc = choice(places)
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #repeat but for moving down
def moveLeft():
    global snekPos
    global playArea
    
    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ")
        except: break

    checkFruit(snekPos[0] - 1)#conditional

    for i in range(1, len(snekPos) + 1, 2):
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i - 1])
        except: break
    for i in range(0, len(snekPos) + 1, 2):
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i] - 1)#conditional
        except: break

    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█")
        except: break

    try: playArea.index("♦")
    except:
        fruitLoc = choice(places)
        while playArea[fruitLoc] == "█": fruitLoc = choice(places)
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #again
    
    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ")
        except: break

    checkFruit(snekPos[0] - 1)#conditional

    for i in range(1, len(snekPos) + 1, 2):
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i - 1])
        except: break
    for i in range(0, len(snekPos) + 1, 2):
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i] - 1)#conditional
        except: break

    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█")
        except: break

    try: playArea.index("♦")
    except:
        fruitLoc = choice(places)
        while playArea[fruitLoc] == "█": fruitLoc = choice(places)
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #again
def moveRight():
    global snekPos
    global playArea
    
    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ")
        except: break

    checkFruit(snekPos[0] + 2) #conditional

    for i in range(1, len(snekPos) + 1, 2):
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i - 1])
        except: break
    for i in range(0, len(snekPos) + 1, 2):
        try: snekPos.pop(i) ; snekPos.insert(i, snekPos[i] + 1) #conditional
        except: break

    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█")
        except: break

    try: playArea.index("♦")
    except:
        fruitLoc = choice(places)
        while playArea[fruitLoc] == "█": fruitLoc = choice(places)
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #again

    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], " ")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, " ")
        except: break

    checkFruit(snekPos[0] + 2) #conditional

    for i in range(1, len(snekPos) + 1, 2):
        try: 
            snekPos.pop(i) ; snekPos.insert(i, snekPos[i - 1])
        except: break
    for i in range(0, len(snekPos) + 1, 2):
        try: snekPos.pop(i) ; snekPos.insert(i, snekPos[i] + 1) #conditional
        except: break

    for i in range(0, len(snekPos) + 1, 2):
        try:
            playArea.pop(snekPos[i]) ; playArea.insert(snekPos[i], "█")
            playArea.pop(snekPos[i]+1) ; playArea.insert(snekPos[i]+1, "█")
        except: break

    try: playArea.index("♦")
    except:
        fruitLoc = choice(places)
        while playArea[fruitLoc] == "█": fruitLoc = choice(places)
        playArea.pop(fruitLoc) ; playArea.insert(fruitLoc, "♦") #again

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
    """sleep(400)""" ; clearConsole() #wipes the console to start
    global userName; userName = input("\n\tHello!\n\tPlease enter your name: ") ; clearConsole() #asks the user for a name then clears
    print("\n\tThanks!") ; sleep(400) ; clearConsole() #says thanks b/c niceties
    global userScore; userScore = 1 #it works - I'm not changing it (yet)
    print("_"*62,"\n\n\tPress any key to start...") # line for measuring scrn size 
    if getwch() == "s": global spectrumMode; spectrumMode = True  #binds controls to QAOP rather than WASD if the 'any key' is an s
    global direction; direction = 1 ; clearConsole() #the rest runs normally, this is just setup 
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
        elif call == 'moveLeft': direcFromCall_forGetLongER = -4
        elif call == 'moveRight': direcFromCall_forGetLongER = 2
        else: direcFromCall_forGetLongER = -columns

        #clearConsole() ; print(snekPos[len(snekPos)-1]) ; print((snekPos[len(snekPos)-1]+direcFromCall_forGetLongER)) ; getwch()
        snekPos.append(snekPos[len(snekPos)-1]+direcFromCall_forGetLongER +1) #this hurt ma brain
        snekPos.append(snekPos[len(snekPos)-2]+direcFromCall_forGetLongER +2) # twice b/c needs next place
def printSmol(): #b/c it zooms so retricts scrn size
    clearConsole()
    print("".join(playArea[0:62])) ; print("".join(playArea[62:124])) ; print("".join(playArea[124:186])) ; print("".join(playArea[186:248])) ; print("".join(playArea[248:310])) ; print("".join(playArea[310:373])) ; print("".join(playArea[372:434])) ; print("".join(playArea[434:496])) ; print("".join(playArea[496:558])) ; print("".join(playArea[558:620])) ; print("".join(playArea[620:682])) ; print("".join(playArea[682:744])) ; print("".join(playArea[744:806])) ; print("".join(playArea[806:]))
    #print(playArea[0:62]) ; print(playArea[62:124]) ; print(playArea[124:186]) ; print(playArea[186:248]) ; print(playArea[248:310]) ; print(playArea[310:372]) ; print(playArea[372:434]) ; print(playArea[434:496]) ; print(playArea[496:558]) ; print(playArea[558:620]) ; print(playArea[620:682]) ; print(playArea[682:744]) ; print(playArea[744:806]) ; print(playArea[806:])
    #print(playArea)
    try: print("\t",userName," ",userScore) #tries to print name
    except: print("\t",userScore) #if it can't for whatever reason don't bother
def endPoint(name, score): 
    file.close() ; log = open("Scores.txt", "a") ; log.write(f"\n{name} {score}") ; log.close()
    for i in range(5, -1, -1): clearConsole() ; print(f"\n\tThe End! You got a score of {userScore}\n\n\t\t%%Reset in {i}_") ; sleep(1000)

spectrumMode = False #default is WASD
borderHit = False #is snek next to border
#preLoad() #just a little animation that isn't finished
start()

columns = 62 ; lines = 16 ; area = columns * lines ; area = area - columns * 2 #fixed area size for zoomed terminal & works out the amount of chars on the screen
playArea = [] #creates a blank list for the chars to go in & then creates borders
for i in range(0, columns): playArea.append("═")
for i in range(0, (area - 2 * columns)): playArea.append(" ")
for i in range(0, columns): playArea.append("═")

playArea.pop(area // 3) ; playArea.insert(area // 3, "█") #remove the character halfway though the list & adds our 'snake' to the list
playArea.pop(area // 3 + 1) ; playArea.insert(area // 3 + 1, "█")  #2wide snek
playArea.pop(area // 5) ; playArea.insert(area // 5, "♦") #removes the character needed & adds 'fruit' to list
printSmol() #print it to the terminal

places = [700, (4 * lines) + 49, (9 * lines) + 59, (6 * lines) + 31, (13 * lines) + 15, 570, 660] #places for the fruit to be
snekPos = [area // 3, area // 3 - columns] #locs of snek segments

file = open("msg.txt", "w") ; file.write("") ; file.close()

"""while True:  #always running game
    def timed_input(prompt, timeout=3):
        print(prompt, end='', flush=True)
        start = since() ; response = '  '
        while since() - start < timeout: 
            if kbhit(): 
                global char
                char = getwch()
                break 
                #response += char
        else: response = None
        return response
    time_limit = 0.6 ; validation = timed_input('', time_limit)
    if validation is None: autoMovePuter(); printSmol()
    else: autoMoveChoice(char, direction) ; autoMovePuter() ; printSmol()"""

while True: 
    moveChoice() ; printSmol() ; file = open("msg.txt") 
    if file.read() == "end": file.close() ; endPoint(userName, userScore) ; break
    else: file.close()

while True: pass