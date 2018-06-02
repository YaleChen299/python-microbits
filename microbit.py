from microbit import *

while True:
    X = accelerometer.get_x()
    Y = accelerometer.get_y()
    if X>30:
        if Y<-30:
            display.show(Image.ARROW_NE)
        elif Y>30:
            display.show(Image.ARROW_SE)
        else:
            display.show(Image.ARROW_E)
    elif X<-30:
        if Y<-30:
            display.show(Image.ARROW_NW)
        elif Y>30:
            display.show(Image.ARROW_SW)
        else:
            display.show(Image.ARROW_W)
    else:
        if Y<-30:
            display.show(Image.ARROW_N)
        elif Y>30:
            display.show(Image.ARROW_S)
        else:
            display.show("-")
   