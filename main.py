import turtle as t
import random

t.colormode(255)
mikky = t.Turtle()
mikky.penup()
mikky.speed(10)
color_list = [(226, 231, 236), (57, 106, 148), (224, 200, 110), (133, 85, 59), (222, 141, 65), (195, 145, 171),
              (234, 225, 203), (144, 179, 203), (224, 233, 230), (138, 82, 106)]

mikky.setheading(225)
mikky.forward(300)
mikky.setheading(0)


for i in range(1, 101):
    mikky.dot(20, random.choice(color_list))
    mikky.fd(50)

    if i % 10 == 0:
        mikky.setheading(90)
        mikky.forward(50)
        mikky.setheading(180)
        mikky.forward(500)
        mikky.setheading(360)

mikky.hideturtle()


screen = t.Screen()
screen.exitonclick()
