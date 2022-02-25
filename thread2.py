print("-------------------threadimage----------------------")
from re import I
import threading
import time
from unicodedata import name

def thread_delay(thread_name,delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count +- 1 
        print(thread_name,"----------->",time.time())

t1 = threading.Thread(target=thread_delay,args=('t1',1))
t2 = threading.Thread(target=thread_delay,args=('t2',3))
t1.start()
t2.start()
print("----------------------------------------------------")

print(1)
time.sleep(10)
print("Done Sleeping")
print(2)

print(3)

print("---------------------threadimage--------------------")

def loop1_10():
    for i in range(1,11):
        time.sleep(1)
        print(i)

threading.Thread(target=loop1_10).start()

class MyThread(threading.Thread):
    def run(self):
        print("{} Started!".format(self.getName()))
        time.sleep(1)
        print("{} Started!".format(self.getName()))

def main():
    for x in range(4):
        mythread = MyThread(name = "Thread - {}".format(x))
        mythread.start()
        time.sleep(.9)

if __name__ == '__main__':
    main()

print("----------------------------------------------------")