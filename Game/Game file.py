import turtle
import time

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
ball.dx = 2
ball.dy = -2

# Create the platform
platform = turtle.Turtle()
platform.shape("square")
platform.color("blue")
platform.shapesize(stretch_wid=1, stretch_len=5)
platform.penup()
platform.goto(0, -250)

# Platform movement speed
platform_speed = 20

# Create the score display
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Timer setup


# Function to move platform to the left
def move_left():
    x = platform.xcor()
    x -= platform_speed
    if x > -350:
        platform.setx(x)

# Function to move platform to the right
def move_right():
    x = platform.xcor()
    x += platform_speed
    if x < 350:
        platform.setx(x)

# Listen for keypress events
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Gravity effect
gravity = 0.5

# Main game loop
while True:
    screen.update()

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
        score += 10
        score_display.clear()  # Clear the previous score
        score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

    # Apply gravity to the ball (make it fall down)
    if ball.ycor() > -290:
        ball.dy -= gravity

    # Check if the ball falls below the platform (game over condition)
    if ball.ycor() < -290:
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 24, "normal"))
        break  # Exit the game loop

# Exit the game when clicked
screen.exitonclick()
