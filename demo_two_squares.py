import turtle
screen = turtle.Screen()

circle_turtle =turtle.Turtle()
circle_turtle.speed(1)
circle_turtle.color("red")

radius = 150
circle_turtle.circle(radius)

circle_turtle.penup()
circle_turtle.goto(0, -radius)
circle_turtle.pendown()

circle_turtle.circle(radius*0.2)

circle_turtle.hideturtle()
screen.mainloop()