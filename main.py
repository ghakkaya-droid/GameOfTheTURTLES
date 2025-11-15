import turtle
import time
import random

Screen = turtle.Screen()
Screen.title("Game of The Turtles")
Screen.bgcolor("beige")
FreeTurtle = turtle.Turtle()
FreeTurtle.shape("turtle")
FreeTurtle.color("Green")
FreeTurtle.penup()
FreeTurtle.hideturtle()
FreeTurtle.shapesize(1.5)
Counter_Value=10
Counter_Turtle=turtle.Turtle()
Counter_Turtle.hideturtle()
Counter_Turtle.penup()
Counter_Turtle.goto(0,300)
WellcomeWriter=turtle.Turtle()
WellcomeWriter.hideturtle()
WellcomeWriter.penup()
SCOREWRITER=turtle.Turtle()
SCOREWRITER.hideturtle()
SCOREWRITER.penup()
SCOREWRITER.goto(0,250)
X_Click=0
Y_Click=0
S=0

def WRITERtoCENTER(X,Y,STRING,S):
    WellcomeWriter.speed(0)
    WellcomeWriter.goto(X,Y)
    WellcomeWriter.write(STRING,align="center",font=("Arial",S,"normal"))

def TimerCounter():
    global Counter_Value
    Counter_Turtle.clear()
    Counter_Turtle.write(Counter_Value,align="center",font=("Arial",24,"normal"))
    if Counter_Value>0:
        Counter_Value-=1
        Screen.ontimer(TimerCounter,1000)
    else:
        GAMEOVER()


def GAMEOVER():
    WellcomeWriter.write("GAME OVER", font=("Arial", 24, "normal"), align="center")

def hide_Free_Turtle():
    FreeTurtle.hideturtle()
    if Counter_Value>0:
        Screen.ontimer(Free_Turtle,700)

def Free_Turtle():
    if Counter_Value<0:
        return
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    FreeTurtle.goto(x,y)
    FreeTurtle.showturtle()
    Screen.ontimer(hide_Free_Turtle,700)

def SCORE_CONTROL():
    SCOREWRITER.clear()
    SCOREWRITER.write(f"SCORE: {S} ", align="center", font=("Arial", 24, "normal"))
def SHOW_WELCOME():
    WellcomeWriter.clear()
    WRITERtoCENTER(0,300,"MERHABA",24)
    WRITERtoCENTER(0,250,"GAME OF THE TURTLES OYUNUNA",24)
    WRITERtoCENTER(0,200,"HOŞ GELDİN",24)
    WRITERtoCENTER(0,0,"OYUNA BAŞLAMAK İÇİN 'B' TUŞUNA BAS",14)

def START_GAME():
    global Counter_Value
    global S
    WellcomeWriter.clear()
    Counter_Value=10
    S=0
    Screen.bgcolor("beige")
    SCORE_CONTROL()
    TimerCounter()
    Free_Turtle()

def click(x,y):
    global X_Click
    global Y_Click
    global S
    X_Click=x
    Y_Click=y
    print(X_Click,Y_Click)

    if Counter_Value>0 and FreeTurtle.isvisible():
        if FreeTurtle.distance(x,y) < 50:
            S += 1
            SCORE_CONTROL()

SHOW_WELCOME()
Screen.listen()
Screen.onkey(START_GAME,"b")

Screen.onscreenclick(click)



Screen.mainloop()