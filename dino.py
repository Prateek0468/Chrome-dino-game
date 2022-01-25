import pyautogui
from PIL import Image,ImageGrab
import time
import math
import keyboard

def isCactus(data,x_start,x_end,checker):

    # for cactus 
    for i in range(x_start,x_end):
        for j in range(600,715):
            if data[i,j] == checker: 
                keyboard.press(" ")
                return

    return

if __name__ == "__main__":
    
    print("Hey.. Dino game about to start in 2 seconds")
    time.sleep(2)
    
    x_start,x_end,last,total_time = 390, 435, 0, 0

    while True:
        t1 = time.time()

        # Emergency Button
        if keyboard.is_pressed('q'):
            break

        image = ImageGrab.grab().convert('L')
        data = image.load()

        #background checker
        if data[15,1000] > 128: checker = 83
        else: checker =  172

        # increase the search width every second to simulate the dino acceleration
        if math.floor(total_time) != last:
            x_end += 4
            if x_end >= 1600:                                                       
                x_end = 1600
            last = math.floor(total_time)

        isCactus(data,x_start,x_end,checker)

        t2 = time.time()-t1
        total_time += t2
