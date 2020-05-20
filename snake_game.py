import os
import keyboard
import time
import random
import sys
clear = lambda: os.system('clear')


x = 8
y = 7
line = 0
length = 1
fruit_x = 8
fruit_y = 9
fruit_line = 0
fruits = 0
w=0
a=0
s=0
d=0
random_fruit_x = 18
random_fruit_y = 38
width = 40
height = 20
while True:

    if height == 4:
        mare = 1
    if height==20:
        mare=0
    if x==height+1 or y==width+1 or x==0 or y==0 :
        clear()
        print("Game ended!")
        print("Points: "+str(fruits))
        break
    if fruit_x == x and y == fruit_y:
        fruits += 1
        length +=0
        fruit_x = random.randint(2,random_fruit_x)
        fruit_y = random.randint(2, random_fruit_y)
        if mare==1:
            random_fruit_x += 1
            random_fruit_y += 1
            height += 1
            width += 1
        else:

            random_fruit_x -=1
            random_fruit_y-=1
            height-=1
            width-=1
    print(unichr(9619)*(width+1)+unichr(9619))
    for i in range(height):
        line+=1

        if line ==x and line == fruit_x:
            if y < fruit_y:
                print(unichr(9619)+     unichr(9617)*(y-length)+ unichr(9608)*length+unichr(9617)*(fruit_y-y-length)+unichr(9638)+ unichr(9617)*(width-fruit_y)+unichr(9619))
            else:
                print(unichr(9619)+     unichr(9617) * (fruit_y - 1) +unichr(9638)+ unichr(9617) * (y - fruit_y - length) + unichr(9608)*length + unichr(9617)* (width - y)+unichr(9619))

        elif line == x:
            print(unichr(9619)+   unichr(9617)*(y-length)+ unichr(9608)*length+ unichr(9617)*(width-y)+unichr(9619))
        elif line == fruit_x:
            print(unichr(9619)+ unichr(9617) * (fruit_y - 1) + unichr(9638) + unichr(9617)* (width - fruit_y)+unichr(9619))
        else:
            print(unichr(9619)+unichr(9617)*width+unichr(9619))
    print(unichr(9619) * (width+1) + unichr(9619))
    line = 0
    if (keyboard.is_pressed('d')):
        y += 1
        w=0
        a=0
        s=0
        d=1

    elif (keyboard.is_pressed('a')):
        y -= 1
        w = 0
        a = 1
        s = 0
        d = 0

    elif (keyboard.is_pressed('w')):
        x -= 1
        w = 1
        a = 0
        s = 0
        d = 0

    elif (keyboard.is_pressed('s')):
        x += 1
        w = 0
        a = 0
        s = 1
        d = 0

    else:
        if a==1:
            y-=1
        if s==1:
            x+=1
        if d==1:
            y+=1
        if w==1:
            x-=1


    if fruits<=10:
        time.sleep(0.07)

    elif fruits<=20:
        time.sleep(0.06)
    elif fruits<=30:
        time.sleep(0.05)
    elif fruits<=45:
        time.sleep(0.04)
    else:
        pass

    clear()
    time.sleep(0)
    print()
    print("Y: "+str(x))
    print("x: "+str(y))
    print("Points: "+str(fruits))

    line=0










