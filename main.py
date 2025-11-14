import turtle
import time

Screen = turtle.Screen()
Screen.title("Game of The Turtles")
Screen.bgcolor("beige")

def WRITERtoCENTER(X,Y,STRING,S):
    T1 = turtle.Turtle()
    T1.hideturtle()
    T1.speed(0)
    T1.penup()
    T1.goto(X,Y)
    T1.write(STRING,align="center",font=("Arial",S,"normal"))

def TimerCounter(F):
    for i in range(F,-1,-1):
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.penup()
        t1.setpos(0, 300)
        t1.write(i, font=("Arial", 24, "normal"), align="center")
        time.sleep(1)
        i=i+1
        t1.clear()

def GAMEOVER():
    T1 = turtle.Turtle()
    T1.hideturtle()
    T1.setpos(0,0)
    T1.write("GAME OVER", font=("Arial", 24, "normal"), align="center")

WRITERtoCENTER(0,300,"MERHABA",24)
WRITERtoCENTER(0,250,"GAME OF THE TURTLES OYUNUNA",24)
WRITERtoCENTER(0,200,"HOŞ GELDİN",24)
WRITERtoCENTER(0,0,"OYUNA BAŞLAMAK İÇİN 'B' TUŞUNA BAS",14)




Screen.mainloop()