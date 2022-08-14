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
def moveUp():
    temp = playArea.index("■")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    try:
        while True:
            defTemp = playArea.index("■")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
    except:
        pass
    temp = temp - columns

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
        playArea.insert(temp, "■")
        temp = temp + columns
def moveDown():
    temp = playArea.index("■")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    try:
        while True:
            defTemp = playArea.index("■")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
    except:
        pass
    temp = temp + columns

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
        playArea.insert(temp, "■")
        temp = temp + columns
def moveLeft():
    temp = playArea.index("■")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    try:
        while True:
            defTemp = playArea.index("■")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
    except:
        pass
    temp = temp - 1
    
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
        playArea.insert(temp, "■")
        temp = temp + 1
def moveRight():
    temp = playArea.index("■")
    playArea.pop(temp)
    playArea.insert(temp, " ")
    try:
        while True:
            defTemp = playArea.index("■")
            playArea.pop(defTemp)
            playArea.insert(defTemp, " ")
    except:
        pass
    temp = temp + 1
    
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
        playArea.insert(temp, "■")
        temp = temp + 1

def start():
    sleep(0.4)
    userName = input("\n\tHello!\n\tPlease enter your name: ")
    clearConsole()
    print("\n\tThanks!")
    sleep(0.4)
    clearConsole()
    global userScore
    userScore = 1
    print("_"*62,"\n") # █
    print("\n\tPress any key to start...")
    secret = getwch()
    if secret == "s":
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
        print("\t",userName,": ",userScore)
    except:
        print("\t",userScore)


spectrumMode = False
start()
"""
groupedTerminalSize = getSize() #works out the size
columns = groupedTerminalSize[0] #extracts amount of columns
lines = groupedTerminalSize[1] #extracts amount of lines
"""
columns = 62
lines = 16
area = columns * lines #works out the amount of chars on the screen
area = area - columns * 2
playArea = [] #creates a blank list
playArea.append("═"*columns)
for i in range(0, (area - 2 * columns)):
    playArea.append(" ")
    pass
playArea.append("═"*columns)

playArea.pop(area // 3) #remove the character halfway though the list
playArea.insert(area // 3, "■") #adds our 'snake' to the list
playArea.pop(area // 5) #removes the character needed
playArea.insert(area // 5, "♦") #adds 'fruit' to list
printSmol()
#places = [(columns * 2) + 22, (columns * 5) - 55, area // 5, (columns // 3) + 123, (columns * (lines // 4)) - 77, (columns // 5) + 64, (columns * 2) + 31, (columns * 3) + 42, (columns * 9) + 47]
places = [(3 * lines) + 4, (4 * lines) + 49, (9 * lines) + 59, (6 * lines) + 31, (13 * lines) + 15]

while 3 > 2:
    moveChoice()
    #print("".join(playArea),"\t",userScore) #join the list into one string & prints it to the terminal
    clearConsole()
    printSmol()