# Simple Pong game in Python 3
# by gautam.gandhi.100@gmail.com

# part 1: Getting Started

import turtle

#setting Window size
wn = turtle.Screen()
wn.title("Pong by @GetSetGoTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #It stops the window from updating

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle() # Returns the turtle object
paddle_a.speed(0) # This is the speed of animation and 0 is the max possible speed
paddle_a.shape("square") # This function has built in shape default shape size is 20px * 20px
paddle_a.color("white") # This sets the color of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # it multiply the width top to bottom by 5 ie 5 * 20px so 100 px tall and 20px left to right
paddle_a.penup() # This will not draw when movinf
paddle_a.goto(-350, 0) #start the paddle a at -350 x coordinate and 0, (0,0) is the center of the screen

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) 

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) 
ball.dx = 0.2 # Change in the X coordinate in ball or Delta X
ball.dy = 0.2 # Change in the y coordinate in ball or Delta y

# Pen (Player Score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # Hide turtle
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
# font(style_name, size, normal/bold/italics)
# write method writes the text in "" on screen and align means align the text from center center is 0,260 


# Function to move paddle
def paddle_a_up():
    y = paddle_a.ycor() # It will returns current Y coordinate of paddle A
    y += 20 # Add 20 px to y coordinate 
    paddle_a.sety(y) # Set new Y to Paddle A

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) 
# KeyBoard Binding
wn.listen() # It will listen to the keyboard input
wn.onkeypress(paddle_a_up, "w") # when w is pressed the call paddle_a_up method
wn.onkeypress(paddle_a_down, "s") # when s is pressed the call paddle_a_down method
wn.onkeypress(paddle_b_up, "Up") # when Up arrow is pressed the call paddle_b_up method
wn.onkeypress(paddle_b_down, "Down") # when down arrow is pressed the call paddle_b_down method

# Main Game Loop
while True:
    wn.update() #everytime loop run it updates the screen

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1