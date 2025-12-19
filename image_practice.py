# Section 1 - Your code
from utils import *
set_background("pixel city")

s1 = create_sprite("pixel guy", 100, 100)
s2 = create_sprite("pixel dog", -100, 100)
s2 = create_sprite("pixel dog", -100, -100)
s2 = create_sprite("pineapple", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("black")
message1.write("Hello user",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()