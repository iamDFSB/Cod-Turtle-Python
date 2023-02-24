# PRIMEIRO DESENHO USANDO O TURTLE
from turtle import *
begin_fill()
shape("turtle")
color("blue")
bgcolor("black")
speed(10)
x=0
while x<18:
    fd(200)
    lt(90)
    fd(200)
    lt(90)
    fd(200)
    lt(90)
    fd(200)
    lt(110)
    x+=1
done()

# OUTRO DESENHO PARA TESTAR
'''from turtle import *
import random as rd

def mudaCor():
   cores = ['blue', 'black', 'white', 'yellow', 'red']
   return rd.choice(cores)

speed(0)
begin_fill()
bgcolor("black")
while True:
   pencolor(mudaCor())
   circle(rd.randint(5 ,50))
   up()
   goto(rd.randint(-400,400),rd.randint(-400,400))
   down()
end_fill()
done()'''

