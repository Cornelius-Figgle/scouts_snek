
from threading import Thread
from queue import Queue
import time

def thread1(threadname, q):
    #read variable "a" modify by thread 2
    while True:
        a = q.get()
        if a is None: return # Poison pill
        print(a)

def thread2(threadname, q):
    a = 0
    for _ in range(10):
        a += 1
        q.put(a)
        time.sleep(1)
    q.put(None) # Poison pill

queue = Queue()
thread1 = Thread( target=thread1, args=("Thread-1", queue) )
thread2 = Thread( target=thread2, args=("Thread-2", queue) )

thread1.start()
thread2.start()
thread1.join()
thread2.join()


input("next?q")


from time import sleep
from threading import Thread

class loader(Thread):   
        def run(self):
                while True:
                        try: print(var)
                        except: print("no")
                        else: break
                        sleep(1)
                print("all done")


def run():
    sleep(4)
    global var
    var = "done"

loader().start()
run()

input()

"""
from threading import Thread
from time import sleep


class BackgroundTimer(Thread):   
   def run(self):
      while 1:
        sleep(5)
        print("yes")

timer = BackgroundTimer()
timer.start()


# ... SNIP ...
while True:
    print("no")
    sleep(1)
#... SNIP ...
# """