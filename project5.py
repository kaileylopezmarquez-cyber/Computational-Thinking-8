import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites

s1=create_sprite("farm",0,0)
create_sprite("chicken",0,0)
# TODO - set your background
# TODO - set the starting value for your variables
sprite_list = []

# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control
# TODO - add code for automatic actions
def move_up():
    if s1.ycor() < 600:
        x = s1.xcor()
        y = s1.ycor() + 3
        s1.goto(x,y)
    
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 3
    s1.goto(x,y)

def move_left():
    x = s1.xcor() - 3
    y = s1.ycor() 
    s1.goto(x,y)

def move_right(): 
    x = s1.xcor() + 3
    y = s1.ycor() 
    s1.goto(x,y)
window.onkeypress(move_up, "s")
window.onkeypress(move_down, "w")
window.onkeypress(move_left, "d")
window.onkeypress(move_right, "a")
# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    
    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")