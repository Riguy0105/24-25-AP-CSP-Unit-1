#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

color = "gray"

# starting location of the tower
x = -125
y = -125

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  if floor % 3 == 0:
       if color == "gray":
           color = "blue"
       else:
           color = "gray"

  # Changing the program to modify the color every three floors
  if floor % 6 == 0:
      painter.color("grey")
  if floor % 6 == 3:
      painter.color("blue")



  y = y + 5 # location of next floor

  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()