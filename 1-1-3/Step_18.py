import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
color = "gray"

# iterate
for floor in range(num_floors):
    if floor % 21 == 0:
        x = x + 75
        y = y - 105
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    if floor % 3 == 0:
        if color == "gray":
            color = "blue"
        # set color and placement of turtle
        else:
            color = "gray"

    painter.color(color)
    y = y + 5  # location of next floor

    # draw the floor
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()