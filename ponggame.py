import turtle
win=turtle.Screen()
win.setup(800,600)
win.bgcolor("black")
win.title("Pong game")
win.tracer(0)

#left_arun
left_arun=turtle.Turtle()
left_arun.shape("square")
left_arun.speed(400)
left_arun.color("red")
left_arun.shapesize(stretch_len=1.5,stretch_wid=6)
left_arun.penup()
left_arun.goto(-400,0)

#right_arun
right_arun=turtle.Turtle()
right_arun.shape("square")
right_arun.speed(400)
right_arun.color("red")
right_arun.shapesize(stretch_len=2.2,stretch_wid=6)
right_arun.penup()
right_arun.goto(400,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.dx=1
ball.dy=1
ball.penup()


#scores
score_a=0
score_b=0
pen=turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Player A : 0  Player B:0",align="center",font=("Arial",24,"normal"))
#moving_paddles

def left_paddle_up():
    left_arun.sety(left_arun.ycor()+20)


def left_paddle_down():
    left_arun.sety(left_arun.ycor()-20)

def right_paddle_up():
    right_arun.sety(right_arun.ycor()+20)

def right_paddle_down():
    right_arun.sety(right_arun.ycor()-20)
#paddles
win.listen()
win.onkeypress(left_paddle_up,'e')
win.onkeypress(left_paddle_down,'c')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')


while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A : {}   Player B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))
    if ball.xcor()>380:
        ball.setx(360)
        ball.dx*=-1

    if ball.xcor() < -380:
        ball.setx(-360)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A : {}    Player B: {}".format(score_a,score_b), align="center", font=("Arial", 24, "normal"))
    if ball.xcor() > 370 and right_arun.ycor()-50<ball.ycor() <right_arun.ycor()+50:
        ball.dx*=-1
    if ball.xcor ()<- 370 and left_arun.ycor() - 50 < ball.ycor() < left_arun.ycor() + 50:
        ball.dx *= -1
