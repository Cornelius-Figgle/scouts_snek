from os import name, system
from shutil import get_terminal_size as getSize
from time import sleep, time
from random import choice
from msvcrt import kbhit, getwch

def clearConsole():
    command = 'clear'
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)

def moveChoice(button):
    #button = getwch() #takes a single character input
    global direction
    if spectrumMode == True:
        if button == "w":
            direction = 1
        elif button == "a":
            direction = 2
        elif button == "o":
            direction = 3
        elif button == "p":
            direction = 4
        elif button == "W":
            direction = 5
        elif button == "A":
            direction = 6
        elif button == "O":
            direction = 7
        elif button == "P":
            direction = 8
        elif button == "n": 
            quit()
        else:
            pass
    else:
        if button == "w":
            direction = 1
        elif button == "s":
            direction = 2
        elif button == "a":
            direction = 3
        elif button == "d":
            direction = 4
        elif button == "W":
            direction = 5
        elif button == "S":
            direction = 6
        elif button == "A":
            direction = 7
        elif button == "D":
            direction = 8
        elif button == "n": 
            quit()
        else:
            pass #automove choices
def autoMovePuter():
        if direction == 1:
            moveUp()
            pass
        elif direction == 2:
            moveDown()
            pass
        elif direction == 3:
            moveLeft()
            pass
        elif direction == 4:
            moveRight()
            pass
        elif direction == 5:
            moveUp()
            moveUp()
        elif direction == 6:
            moveDown()
            moveDown()
        elif direction == 7:
            moveLeft()
            moveLeft()
            moveLeft()
        elif direction == 8:
            moveRight()
            moveRight()
            moveRight()#if gates for movement dir
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

def preLoad():
    getwch()
    n1 = 1
    n2 = 1
    cent = 1
    for i in range(10):
        square = "█"*(i+1) 
        line = "─"*36 
        spaces = " "*(30 - ((i+1)*3))
        if cent < 10:
            spaces = spaces + " "
        print("", end=f"\r\n\t╓{line}╖\n\t║ {cent}% {square}{square}{square} {spaces}║\n\t╙{line}╜")
        cent = n1 + n2
        n1 = n2
        n2 = cent
        sleep(0.4)
        clearConsole()
    print("", end=f"\r\n\t╓{line}╖\n\t║ {98}% {square}{square}{square} {spaces}║\n\t╙{line}╜")
    sleep(0.4)
    getwch()
    clearConsole()
def start():
    #sleep(0.4)
    global userName
    userName = input("\n\tHello!\n\tPlease enter your name: ") 
    clearConsole()
    print("\n\tThanks!")
    #sleep(0.4)
    clearConsole()
    global userScore
    userScore = 1
    print("_"*62,"\n") # line is for measuring scrn size cos im lazy
    print("\n\tPress any key to start...")
    secret = getwch() #checks if the 'any key' is an s
    if secret == "s": #binds control to QAOP rather than WASD
        global spectrumMode
        spectrumMode = True 
    global direction
    direction = 1
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
#preLoad()
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

while True:  #always running game
    try: #to stop crashing (bubblegum and stickytape solutio right here)
        def timed_input(prompt, timeout=3):
            print(prompt, end='', flush=True)
            start = time()
            response = '  '
            while time() - start < timeout:
                if kbhit():
                    global char
                    char = getwch()
                    #if char == '\r':
                    break
                    response += char
            else:
                response = None
            return response
        time_limit = 0.06 # in seconds
        validation = timed_input('', time_limit)
        if validation is None:
            autoMovePuter()
            #sleep(0.6)
        else:
            moveChoice(char)
        #print("".join(playArea),"\t",userScore) #join the list into one string & prints it to the terminal
        clearConsole()
        printSmol()
    except:
        pass