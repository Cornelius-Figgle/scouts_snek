#max@fullimage.co.uk

from os import name, system
from subprocess import run
from sys import executable
from time import sleep as timesleep

#________________________________________________________________________________________________________________________________

clearConsole = lambda: system('cls' if name in ('nt', 'dos') else 'clear') #copied this from here, thanks: https://www.delftstack.com/howto/python/python-clear-console/

clearConsole() #wprds

def instalMod(module):
    run([executable, '-m','ensurepip','--upgrade'])
    run([executable, '-m','pip', 'install', 'pip-review'])
    run(['pip-review', '--auto'])
    run([executable,'-m','pip', 'install', module])

def sleep(milliseconds):
    try: seconds = int(milliseconds)/1000
    except: return 'Error'
    timesleep(seconds)


def checkEven(num): #returns 0 if even, 1 if odd (integers only)
    rem = int(num) % 2
    if rem == 0: return True
    else: return False

def smth(): pass
