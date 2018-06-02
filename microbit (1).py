from microbit import *
import random
x = random.randint(0, 4)
y = random.randint(0, 4)
display.set_pixel(x, y, 9)

while True:
    X = accelerometer.get_x()
    Y = accelerometer.get_y()
    if X>30:
        if Y<-30:
            x = (x+1)%5
            y = (y-1)%5
            display.set_pixel(x, y, 9)
        elif Y>30:
            x = (x+1)%5
            y = (y+1)%5
            display.set_pixel(x, y, 9)
        else:
            x = (x+1)%5
            display.set_pixel(x, y, 9)
    elif X<-30:
        if Y<-30:
            x = (x_1)%5
            y = (y-1)%5
            display.set_pixel(x, y, 9)
        elif Y>30:
            x = (x-1)%5
            y = (y+1)%5
            display.set_pixel(x, y, 9)
        else:
            x = (x-1)%5
            display.set_pixel(x, y, 9)
    else:
        if Y<-30:
            y = (y-1)%5
            display.set_pixel(x, y, 9)
        elif Y>30:
            y = (y+1)%5
            display.set_pixel(x, y, 9)
        else:
            display.set_pixel(x, y, 9)
   