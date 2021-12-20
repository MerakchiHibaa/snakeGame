import turtle
import winsound

wn = turtle.Screen()
wn.title("Pog by Hiba")
wn.bgcolor("black")
wn.setup(width=800 , height=600)
wn.tracer(0) 

# Score
score_a = 0
score_b = 0

#stop the game from updating so it dosnt get slow

# Paddle A
paddle_a = turtle.Turtle() #turtle object 
paddle_a.speed(0) #the speed of animation, this sets it t the max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)#the default size is 20 so we stretch five times the width
paddle_a.penup() #no drawing while moving
paddle_a.goto(-350,0) #starts at 350 fl3ord and centereed
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1 , stretch_wid=5)
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350,0)
# Ball
ball= turtle.Turtle()
ball.color("white")
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(0,0)
#everytime the ball moves it moves with 2 pixels
ball.dx = 0.25 #delta change x
ball.dy = -0.25 #delta change y

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center" , font=("Courier" , 24 , "normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor() #retourne la coordonnee y
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #retourne la coordonnee y
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #retourne la coordonnee y
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor() #retourne la coordonnee y
    y -= 20
    paddle_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "s") #losquon appuie sur w (up) on appelle la fonction up
wn.onkeypress(paddle_a_down, "w") #losquon appuie sur s (up) on appelle la fonction up
wn.onkeypress(paddle_b_up, "Up") #losquon appuie sur w (up) on appelle la fonction up
wn.onkeypress(paddle_b_down, "Down") #losquon appuie sur s (up) on appelle la fonction up




#main game loop
while True:
    wn.update()
    #move the ball everytime the loop loops the ball changes its position with 2 pixels

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking
    if ball.ycor()> 290 : #because the height is 600 so 300 from center to top, minux the size of the ball/2 (20/2=10)
        ball.sety(290)
        ball.dy*= -1 #reversing the directiong if we cross the border
        winsound.PlaySound("bounce.mp3" , winsound.SND_ASYNC)

    if ball.ycor()< -290 : #because the height is 600 so 300 from center to top, minux the size of the ball/2 (20/2=10)
        ball.sety(-290)
        ball.dy*= -1 #reversing the directiong if we cross the border
        winsound.PlaySound("bounce.mp3" , winsound.SND_ASYNC)  
    if ball.xcor() > 390:
        ball.goto(0 , 0)
        ball.dx*= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center" , font=("Courier" , 24 , "normal"))
        winsound.PlaySound("bounce.mp3" , winsound.SND_ASYNC)
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center" , font=("Courier" , 24 , "normal"))
        winsound.PlaySound("bounce.mp3" , winsound.SND_ASYNC)

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 )and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40): 
        ball.setx(340) #back it to the left a little bit
        ball.dx*= -1 #if the ball is going on the right,<350 becus the width of the panel is 10 so the ball muct be collide with the paddle (so it wont bounce even behin the paddle), >340 cuz the width of the paddle is 50 (390 -50)and its position is between the position of paddleb +50 and -40 (40 is the length of the paddle b) then collision so we reverse the direction
    
    if (ball.xcor() < -340 and ball.xcor() > -350 )and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40): 
        ball.setx(-340) #back it to the left a little bit
        ball.dx*= -1 #if the ball is going on the right,<350 becus the width of the panel is 10 so the ball muct be collide with the paddle (so it wont bounce even behin the paddle), >340 cuz the width of the paddle is 50 (390 -50)and its position is between the position of paddleb +50 and -40 (40 is the length of the paddle b) then collision so we reverse the direction


