import turtle, time, random
from utils import *


# Section 1 - setup
# # TODO - set a background using set_background()

set_background("jungle")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
Monkeys=0
Monkey_cost=50 
Bananas=0

# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -300,250)
message_sprite.hideturtle()
message_sprite2 = create_sprite("alien", -300,230)
message_sprite2.hideturtle()
message_sprite3 = create_sprite("alien", 200,300)
message_sprite3.hideturtle()
def make_Bananas() :
    global Bananas
    Bananas += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("banana",x,y)

window.onkeypress( make_Bananas, "space")


# Section 2 - controls
# TODO - define an action. ex: def my_control()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control
def bribe_monkeys() :
    global Bananas, Monkeys
    if Bananas>=50:
        Monkeys += 1
        Bananas-=50
        x = random.randint(-200,200)
        y = -250
        create_sprite("monkey",x,y)
window.onkeypress(bribe_monkeys,"m")




# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here
    if i %20 == 0:
        Bananas+= Monkeys


    # OPTIONAL - use the message sprite to say a message
    message_sprite.clear()
    message_sprite.write ("Click space key for bananas. Use m key to bribe monkeys")
    message_sprite2.clear()
    message_sprite2.write (f"Bananas:{Bananas}")
    time.sleep(0.01)
    window.update()
    #The goal of the game is to get as many bananas as you can to become a millionaire 
    
if Bananas>= 5000 :
     message_sprite3.write("You have enough bananas to be a millionaire!!!! ")