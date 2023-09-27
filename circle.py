import math
import time

# define mode before using function.
mode = "secs"

def countDown(length):
    while length > 0:
        length -= 1
        time.sleep(1)
        print(length)

def countUp():
    num = 0
    if mode == "secs":
        while True:
            time.sleep(1)
            num += 1
            
    if mode == "mins":
        while True:
            time.sleep(60)
            num += 1

    if mode == "hrs":
        while True:
            time.sleep(3600)
            num += 1
    
    print(num + mode)

mode = "mins"
countUp()