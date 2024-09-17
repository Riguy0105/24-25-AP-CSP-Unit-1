#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
w = 6
y = 70
z = 380 / w
spider.pensize(5)
n = 0
while (n < w):
  spider.goto(0, 0)
  spider.setheading(z * n)
  spider.forward(y)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()