from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()


def move_forward():
    jim.forward(10)


def move_backward():
    jim.backward(10)


def turn_left():
    new_heading = jim.heading() + 10
    jim.setheading(new_heading)


def turn_right():
    new_heading = jim.heading() - 10
    jim.setheading(new_heading)


def clear():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()


screen.listen()

screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()
