from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(clear, "c")

screen.exitonclick()
