from turtle import Turtle, Screen
import random


jimmy = Turtle()

# jimmy.forward(100)
# jimmy.left(90)
# jimmy.forward(100)
# jimmy.left(90)
# jimmy.forward(100)
# jimmy.left(90)
# jimmy.forward(100)
# jimmy.left(90)

colours = ['DarkOrchid']


def draw_shap(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        jimmy.forward(100)
        jimmy.right(angle)


for shap_side_n in range(3, 11):
    jimmy.color(random.choice(colours))
    draw_shap(shap_side_n)


sc = Screen()
sc.exitonclick()
