import turtle as t
import random as rand

# Initialize Variables
wn = t.Screen()
maze_painter = t.Turtle()

path_width = 30
wall_color = "black"
wall_length = 35
barrier_length = (path_width * 2)




# Setup Turtle
maze_painter.pencolor(wall_color)
maze_painter.speed(0)
maze_painter.pensize(5)
maze_painter.hideturtle()
maze_painter.left(90)


#Draw Maze
'''
Process:
Draw a line
Turn Left
Increment Length
Repeat
'''
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.back(path_width)
    maze_painter.left(90)

for wall in range(21):
    first_length = wall_length / rand.randint(1, 3)
    maze_painter.forward(first_length)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if(wall > 5):
        draw_barrier()
    maze_painter.forward(wall_length - path_width - first_length)
    maze_painter.left(90)
    wall_length += 15



wn.mainloop()
