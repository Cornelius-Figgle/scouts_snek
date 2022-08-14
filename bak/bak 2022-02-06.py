from os import name, system
from importlib import reload
from shutil import get_terminal_size as getSize
from time import sleep
from random import choice
from msvcrt import getwch

def clearConsole():
    command = 'clear'
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)

def moveChoice():
    button = getwch() #takes a single character input
    if spectrumMode == True:
        if button == "w":
            moveUp()
        elif button == "a":
            moveDown()
        elif button == "o":
            moveLeft()
        elif button == "p":
            moveRight()
        elif button == "W":
            moveUp()
            moveUp()
        elif button == "A":
            moveDown()
            moveDown()
        elif button == "O":
            moveLeft()
            moveLeft()
            moveLeft()
        elif button == "P":
            moveRight()
            moveRight()
            moveRight()
        elif button == "n": 
            quit()
        else:
            pass
    else:
        if button == "w":
            moveUp()
        elif button == "s":
            moveDown()
        elif button == "a":
            moveLeft()
        elif button == "d":
            moveRight()
        elif button == "W":
            moveUp()
            moveUp()
        elif button == "S":
            moveDown()
            moveDown()
        elif button == "A":
            moveLeft()
            moveLeft()
            moveLeft()
        elif button == "D":
            moveRight()
            moveRight()
            moveRight()    
        elif button == "n": 
            quit()
        else:
            pass
def moveUp(): #when called by moveChoice()
    temp = playArea.index("█") #find the location of the frist char in snake
    playArea.pop(temp) #remove it
    playArea.insert(temp, " ") #fill the gap with a blank
    temp = playArea.index("█") #repeat b/c snek 2 wide
    playArea.pop(temp)
    playArea.insert(temp, " ") 
    try: 
        while True: #infinate loop (until it can't any more)
            defTemp = playArea.index("█") #locate next char
            playArea.pop(defTemp) #remove it
            playArea.insert(defTemp, " ") #replace it
            defTemp = playArea.index("█") #repeat 
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
    except:
        pass #when it errors do nothing and move on
    temp = temp - 1 - columns #looks columns abive first char

    fruitLoc = temp #says fruit may be here
    if playArea[fruitLoc] == "♦": #if it is...
        playArea.pop(fruitLoc) #remove it
        playArea.insert(fruitLoc, " ") #replace it
        sleep(0.3) #sleep for some reason
        fruitLoc = choice(places) #selects random loc from list of 5
        playArea.pop(fruitLoc) #remove whatever is there
        playArea.insert(fruitLoc, "♦") #add a fruit
        scoreCheck(userScore) #increase the score (yes ik name is misleading, shut up)
    for i in range (0, userScore): #for amount of 'segments' 
        playArea.pop(temp) #remove at the loc of where the fruit used to be
        playArea.insert(temp, "█") #add a snek char
        temp = temp + 1 #go one across 4 2nd char
        playArea.pop(temp) #repeat
        playArea.insert(temp, "█")
        temp = temp - 1 + columns #uh go one columns down and back across one so at start of 2wide snek
    try:
        playArea.index("♦") #sees if can find fruit (b/c the rand is from the list so fruit might not change loc)
    except: #if fruit didn't change
        fruitLoc = choice(places) #choose another rand loc 
        while playArea[fruitLoc] == "█": #whilst this loc is where the snek is
            fruitLoc = choice(places) #choose another
        playArea.pop(fruitLoc) #remove the char here 
        playArea.insert(fruitLoc, "♦") #replaces it w the fruit
    pass #move up when called
def moveDown():
    temp = playArea.index("█")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    temp = playArea.index("█")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    try:
        while True:
            defTemp = playArea.index("█")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
            defTemp = playArea.index("█")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
    except:
        pass
    temp = temp - 1 + columns

    fruitLoc = temp
    if playArea[fruitLoc] == "♦":
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, " ")
        sleep(0.3)
        fruitLoc = choice(places)
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, "♦")
        scoreCheck(userScore)
    for i in range (0, userScore):
        playArea.pop(temp)
        playArea.insert(temp, "█")
        temp = temp + 1
        playArea.pop(temp)
        playArea.insert(temp, "█")
        temp = temp - 1 + columns
    try:
        playArea.index("♦")
    except:
        fruitLoc = choice(places)
        while playArea[fruitLoc] == "█":
            fruitLoc = choice(places)
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, "♦") #repeat but for moving down
def moveLeft():
    temp = playArea.index("█")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    temp = playArea.index("█")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    try:
        while True:
            defTemp = playArea.index("█")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
            defTemp = playArea.index("█")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
    except:
        pass
    temp = temp - 3
    
    fruitLoc = temp
    if playArea[fruitLoc] == "♦":
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, " ")
        sleep(0.3)
        fruitLoc = choice(places)
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, "♦")
        scoreCheck(userScore)
    for i in range (0, userScore):
        playArea.pop(temp)
        playArea.insert(temp, "█")
        temp = temp + 1
        playArea.pop(temp)
        playArea.insert(temp, "█")
        temp = temp - 3
    try:
        playArea.index("♦")
    except:
        fruitLoc = choice(places)
        while playArea[fruitLoc] == "█":
            fruitLoc = choice(places)
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, "♦") #again
def moveRight():
    temp = playArea.index("█")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    temp = playArea.index("█")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    try:
        while True:
            defTemp = playArea.index("█")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
            defTemp = playArea.index("█")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
    except:
        pass
    temp = temp + 2
    
    fruitLoc = temp
    if playArea[fruitLoc] == "♦":
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, " ")
        sleep(0.3)
        fruitLoc = choice(places)
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, "♦")
        scoreCheck(userScore)
    temp = temp - 1
    for i in range (0, userScore):
        playArea.pop(temp)
        playArea.insert(temp, "█")
        temp = temp + 1
        playArea.pop(temp)
        playArea.insert(temp, "█")
        temp = temp + 1
    try:
        playArea.index("♦")
    except:
        fruitLoc = choice(places)
        while playArea[fruitLoc] == "█":
            fruitLoc = choice(places)
        playArea.pop(fruitLoc)
        playArea.insert(fruitLoc, "♦") #u guessed it

def start():
    sleep(0.4)
    global userName
    userName = input("\n\tHello!\n\tPlease enter your name: ") 
    clearConsole()
    print("\n\tThanks!")
    sleep(0.4)
    clearConsole()
    global userScore
    userScore = 1
    print("_"*62,"\n") # line is for measuring scrn size cos im lazy
    print("\n\tPress any key to start...")
    secret = getwch() #checks if the 'any key' is an s
    if secret == "s": #binds control to QAOP rather than WASD
        global spectrumMode
        spectrumMode = True 
    clearConsole()
def scoreCheck(currentScore):
    global userScore
    userScore = currentScore + 1
    pass
def printSmol():
    print("".join(playArea[:1]))
    print("".join(playArea[1:63]))
    print("".join(playArea[63:125]))
    print("".join(playArea[125:187]))
    print("".join(playArea[187:249]))
    print("".join(playArea[249:311]))
    print("".join(playArea[311:373]))
    print("".join(playArea[373:435]))
    print("".join(playArea[435:497]))
    print("".join(playArea[497:559]))
    print("".join(playArea[559:621]))
    print("".join(playArea[621:683]))
    print("".join(playArea[683:745]))
    print("".join(playArea[745:807]))
    try:
        print("\t",userName," ",userScore)
    except:
        print("\t",userScore)


spectrumMode = False #default is WASD
start()
"""
groupedTerminalSize = getSize() #works out the size
columns = groupedTerminalSize[0] #extracts amount of columns
lines = groupedTerminalSize[1] #extracts amount of lines
""" #old code
columns = 62 #fixed area size for zoomed terminal
lines = 16
area = columns * lines #works out the amount of chars on the screen
area = area - columns * 2
playArea = [] #creates a blank list for the chars to go in
playArea.append("═"*columns) #creates border
for i in range(0, (area - 2 * columns)):
    playArea.append(" ")
    pass #fills spaces
playArea.append("═"*columns) #same

playArea.pop(area // 3) #remove the character halfway though the list
playArea.insert(area // 3, "█") #adds our 'snake' to the list
playArea.pop(area // 3 + 1) #2wide snek
playArea.insert(area // 3 + 1, "█") 
playArea.pop(area // 5) #removes the character needed
playArea.insert(area // 5, "♦") #adds 'fruit' to list
printSmol() #print it to the terminal
#places = [(columns * 2) + 22, (columns * 5) - 55, area // 5, (columns // 3) + 123, (columns * (lines // 4)) - 77, (columns // 5) + 64, (columns * 2) + 31, (columns * 3) + 42, (columns * 9) + 47]
places = [(3 * lines) + 4, (4 * lines) + 49, (9 * lines) + 59, (6 * lines) + 31, (13 * lines) + 15] #places for the fruit to be

while 3 > 2:  #always running game
    try: #to stop crashing (bubblegum and stickytape solutio right here)
        moveChoice()
        #print("".join(playArea),"\t",userScore) #join the list into one string & prints it to the terminal
        clearConsole()
        printSmol()
    except:
        pass