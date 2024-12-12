import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball")
screen.setup(width=800, height=600)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0, 100)
ball.dx = 2  # Ball's horizontal speed
ball.dy = -2  # Ball's vertical speed

# Create the platform
platform = turtle.Turtle()
platform.shape("square")
platform.color("blue")
platform.shapesize(stretch_wid=1, stretch_len=5)  # Resize the platform
platform.penup()
platform.goto(0, -250)

# Platform movement speed
platform_speed = 20

# Function to move platform to the left
def move_left():
    x = platform.xcor()
    x -= platform_speed
    if x > -350:  # Ensure it stays within the window
        platform.setx(x)

# Function to move platform to the right
def move_right():
    x = platform.xcor()
    x += platform_speed
    if x < 350:  # Ensure it stays within the window
        platform.setx(x)

# Listen for keypress events
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Gravity effect
gravity = 0.1

# Main game loop
while True:
    screen.update()  # Update the screen to reflect changes

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with walls (left and right)
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1  # Reverse direction
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1  # Reverse direction

    # Ball collision with ceiling
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse direction

    # Ball collision with the platform
    if (ball.ycor() > platform.ycor() and ball.ycor() < platform.ycor() + 10 and
        ball.xcor() > platform.xcor() - 50 and ball.xcor() < platform.xcor() + 50):
        ball.dy *= -1  # Reverse the ball's vertical direction

    # Apply gravity to the ball (make it fall down)
    if ball.ycor() > -290:
        ball.dy -= gravity  # Gravity effect (falling)

    # Ball goes below the platform (game over or reset)
    if ball.ycor() < -300:
        ball.goto(0, 100)  # Reset ball position
        ball.dy = -2  # Reset the vertical speed


