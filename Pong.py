import turtle

def PongGame():
    # For main Screen
    wn = turtle.Screen()
    wn.title("Pong by Shivani Agarwal")
    wn.bgcolor("black")
    wn.setup(width = 800, height=600)
    wn.tracer(0)

    # Score
    a_score = 0
    b_score = 0


    # Paddle 1
    a_paddle = turtle.Turtle()
    a_paddle.speed(0)
    a_paddle.shape("square")
    a_paddle.shapesize(stretch_wid=5, stretch_len=1)
    a_paddle.color("blue")
    a_paddle.penup()
    a_paddle.goto(-350,0)

    # Paddle 2
    b_paddle = turtle.Turtle()
    b_paddle.speed(0)
    b_paddle.shape("square")
    b_paddle.shapesize(stretch_wid=5, stretch_len=1)
    b_paddle.color("blue")
    b_paddle.penup()
    b_paddle.goto(350,0)
    # Ball

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx = 2  # every a ball it moves by 2 pixels
    ball.dy = -2


    # Pen : to write the scores
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


    # Functions
    # increases as we go up
    # decreases as we go down
    def a_paddle_up():
        y = a_paddle.ycor()
        y = y + 20
        a_paddle.sety(y)

    def a_paddle_down():
        y = a_paddle.ycor()
        y = y - 20
        a_paddle.sety(y)




    def b_paddle_up():
        y = b_paddle.ycor()
        y = y + 20
        b_paddle.sety(y)

    def b_paddle_down():
        y = b_paddle.ycor()
        y = y - 20
        b_paddle.sety(y)


    # keyboard binding
    wn.listen()
    wn.onkey(a_paddle_up, "w")

    wn.listen()
    wn.onkey(a_paddle_down, "s")


    wn.listen()
    wn.onkey(b_paddle_up, "Up")

    wn.listen()
    wn.onkey(b_paddle_down, "Down")


    # main game loop
    while True:
        wn.update()

        # Move the Ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking
        # top most corner
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        # bottom most corner
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # left and right corners
        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            a_score += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(a_score, b_score), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            b_score += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(a_score, b_score), align="center", font=("Courier", 24, "normal"))


        # Paddle and ball collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < b_paddle.ycor() + 50 and ball.ycor() > b_paddle.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < a_paddle.ycor() + 50 and ball.ycor() > a_paddle.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1


PongGame()
