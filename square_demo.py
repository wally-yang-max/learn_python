import turtle

square_turtle = turtle.Turtle()
square_turtle.speed(1)
side_length = 100

square_turtle.forward(side_length)
square_turtle.left(90)
square_turtle.forward(side_length)
square_turtle.left(90)
square_turtle.forward(side_length)
square_turtle.left(90)
square_turtle.forward(side_length)


square_turtle.hideturtle()
turtle.done()