# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst_severed_spots.jpg", 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

color_list = [(249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dota = 101

for dot_count in range(1, number_of_dota):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


##Drugi nacin koji daje rezultat koji se trazi
# tim.penup()
# tim.goto(-250, -250)
# tim.pensize(5)
# screen = Screen()
# screen.colormode(255)
#
# y = 0
# x = 0
# while x < 10:
#     for _ in range(10):
#         tim.pencolor(random.choice(color_list))
#         tim.dot(20)
#         tim.penup()
#         tim.fd(50)
#         tim.pendown()
#
#     tim.penup()
#     tim.goto(-250, -210 + y)
#     x += 1
#     y += 40


screen.exitonclick()