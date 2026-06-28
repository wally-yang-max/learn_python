import turtle

pen = turtle.Turtle()
pen.color("red")

# first
pen.circle(50)
pen.circle(50, steps=3)
pen.circle(50, steps=4)

#second
pen.color("blue")
sides = 6
length = 200
angle = 360 / sides
for i in range(sides):
    pen.forward(length)
    pen.right(angle)

turtle.done()