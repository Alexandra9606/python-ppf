import time
import os

H = 10
W = 20
C = "#"
SLEEP = 1

x = H//2
y = 0
snake_len = 3
direction = "RIGHT"

clear = lambda: os.system('clear')

while True:
    clear()
    for i in range(H):
        for j in range(W):
            print(C if (i==0 or i==H-1 or j == 0 or j==W-1) else " ", end="")
        print("")
    time.sleep(SLEEP)