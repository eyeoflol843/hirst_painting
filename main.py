###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random


def rgb(color):
    rgb = color.rgb
    red = rgb[0]
    blue = rgb[1]
    green = rgb[2]
    return [red, blue, green]


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
first_color = colors[0]
for color in range(len(colors)):
    chosen_color = colors[color]
    rgb_colors.append(rgb(chosen_color))
print(rgb_colors)

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for j in range(9):
    timmy.setheading(0)
    for i in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.forward(50)

    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)

screen = turtle.Screen()
screen.exitonclick()