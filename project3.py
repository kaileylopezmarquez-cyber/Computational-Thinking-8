import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-500
y1 =200
x2 =-500
y2 =50
x3 =-500
y3 =-100
x4 =-500
y4 =-250


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("racetrack")
t1 = create_sprite("redcar",x1,y1)
t2 = create_sprite("yellow car",x2,y2)
t3 = create_sprite("bluecar",x3,y3)
t4 = create_sprite("basketball",x4,y4)

time.sleep(5)
# # # Section 3 - Racing
# # # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - Here there is a for loop, this code will repeat 10 times 
# The numbers show by how much each sprite will go toward in the x axis
# In this example the fastest sprite will be 4 beacuse it has the largest increases
for i in range(10):
    x1 +=20
    x2 +=40
    x3 +=70
    x4 +=150

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Red Car Wins!")
if x2 >= x1 and x1 >= x3 and x1 >= x4:
    print("Yellow Car Wins!")
if x3 >= x1 and x1 >= x2 and x1 >= x4:
    print("Blue Car wins!")
if x4 >= x1 and x1 >= x2 and x1 >= x3:
    print("Basketball Wins!")
else :
    print("nobody wins")    




turtle.exitonclick()