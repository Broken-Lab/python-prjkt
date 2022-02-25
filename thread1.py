# print("-------------------threadimage----------------------")
# import threading
# import time
# def sleepy_man(secs):
#     print('Starting To Sleep Inside')
#     time.sleep(secs)
#     print('Woke Up Inside')

# x = threading.Thread(target=sleepy_man,args=(1,))
# x.start()
# print("\nActive Count",threading.activeCount())
# time.sleep(1.2)
# print("Done")

print("-------------------threadimage----------------------")
import threading
import time

def sleepy_man(secs):
    print('Starting To Sleep Inside')
    time.sleep(secs)
    print('Woke Up Inside')

x = threading.Thread(target=sleepy_man,args=(4,))
x.start()
print("\nActive Count",threading.activeCount())
time.sleep(1.2)
print("Done")