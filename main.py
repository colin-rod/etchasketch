from turtle import Turtle, Screen

timmy= Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_back():
    timmy.backward(10)

def turn_right():
    timmy.right(10)

def turn_left():
    timmy.left(10)

def clear_screen():
    timmy.clear()


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_back,"s")
screen.onkey(turn_right,"d")
screen.onkey(turn_left,"a")
screen.onkey(clear_screen,"c")

screen.exitonclick()