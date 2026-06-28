# 导入和初始化
import turtle

# 创建画布和海龟
screen = turtle.Screen()
t = turtle.Turtle()

# 设置画布属性
screen.title("我的绘图")
screen.bgcolor("white")

# 设置海龟路径：
# turtle.speed()默认为 3 ，表示中等速度
t.speed(3)
t.color("blue")
t.pensize(2)
t.hideturtle()  #隐藏海龟光标

#基本绘图指令
#移动：
t.forward(100)
t.backward(50)
t.goto(0, 0) #go to direct target

# turn the sight
t.left(90)
t.right(90)

#control the pen:
t.penup()
t.pendown()

# color and fillcolor
t.color("red")
t.fillcolor("orange")
#fill the shape
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

# gain the location
current_x = t.xcor()
y = t.ycor()
t.forward(200)
# clear the screen
#t.clear()
# write the words
t.write("had cleared the screen",font=("Arial",12,"normal"))

# set the initial place
t.penup()
t.goto(-300, 0)
t.pendown()

t.left(45)

for _ in range(6):
    current_x = t.xcor()
    print(current_x)
    # use if-elif control the color
    # set the color according to the current_x
    if current_x < -200:
        color = 'red'
    elif -200 <= current_x < -100:
        color = 'blue'
    elif -100 <= current_x < 100:
        color = 'orange'
    elif 100 <= current_x < 200:
        color = 'purple'
    else:
        color = 'yellow'

    t.color(color)
    t.forward(100)
    # write the color name in the located place
    t.write(color, font=("Arial",14,"normal"))
screen.exitonclick()