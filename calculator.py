import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("解方程的计算器")

root.geometry("600x600")
custom_font = font.Font(size=16)   #字体大小

#定义加法函数
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"四则运算结果：{result}")
    except ValueError:
        result_label.config(text=f"请输入有效数字")

def subtract_numbers():
    num1, num2 = float(entry1.get()), float(entry2.get())
    result_label.config(text=f"四则运算结果={num1 - num2}")

def multiply_numbers():
    num1, num2 = float(entry1.get()), float(entry2.get())
    result_label.config(text=f"四则运算结果: {num1 * num2}")

def divide_numbers():
    num1, num2 = float(entry1.get()), float(entry2.get())
    if num2 != 0:
        result = round(num1 / num2, 3)
        result_label.config(text=f"四则运算结果: {result}")
    else:
        result_label.config(text="除数不能为零")

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            solution_label.config(text="a 不能为零")
            return

        delta = b**2 - 4*a*c
        if delta > 0:
            delta_sqrt = delta**0.5
            x1 = round((-b + delta_sqrt) / (2*a), 3)  #round 保留小数
            x2 = round((-b - delta_sqrt) / (2*a), 3)
            solution_label.config(text=f"解方程结果: x1 = {x1}, x2 = {x2}")
        elif delta == 0:
            x1 = round(-b / (2*a), 3)
            solution_label.config(text=f"解方程结果: x1 = x2 = {x1}")
        else:
            solution_label.config(text="解方程结果: 无实数解")
    except ValueError:
        solution_label.config(text="请输入有效的数字")

#重制函数
def reset_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    result_label.config(text="计算结果: ")
    solution_label.config(text="解方程结果: ")

#输入框
label1 = tk.Label(root, text="输入第一个数:", font=custom_font)
label1.place(x=50, y=20)

entry1 = tk.Entry(root)
entry1.place(x=150, y=20)

label2 = tk.Label(root, text="输入第二个数:", font=custom_font)
label2.place(x=50, y=60)

entry2 = tk.Entry(root)
entry2.place(x=150, y=60)

#按钮定位
add_button = tk.Button(root, text="加法", command=add_numbers, font=custom_font)
add_button.place(x=50, y=100, width=60, height=30)

subtract_button = tk.Button(root, text="减法", command=subtract_numbers, font=custom_font)
subtract_button.place(x=120, y=100, width=60, height=30)

multiply_button = tk.Button(root, text="乘法", command=multiply_numbers, font=custom_font)
multiply_button.place(x=190, y=100, width=60, height=30)

divide_button = tk.Button(root, text="除法", command=divide_numbers, font=custom_font)
divide_button.place(x=260, y=100, width=60, height=30)

#分割线
line1 = tk.Label(root, text="-"*50)
line1.place(x=50, y=140)

# 结果标签
result_label = tk.Label(root, text="计算结果: ", font=custom_font)
result_label.place(x=50, y=160)

line2 = tk.Label(root, text="-"*50)
line2.place(x=50, y=190)

#解方程部分
#输入框
label_a = tk.Label(root, text="a:")
label_a.place(x=50, y=220)

entry_a = tk.Entry(root)
entry_a.place(x=100, y=220)

label_b = tk.Label(root, text="b:")
label_b.place(x=50, y=260)

entry_b = tk.Entry(root)
entry_b.place(x=100, y=260)

label_c = tk.Label(root, text="c:")
label_c.place(x=50, y=300)

entry_c = tk.Entry(root)
entry_c.place(x=100, y=300)

#按钮
solve_button = tk.Button(root, text="解方程", command = solve_quadratic)
solve_button.place(x=150,y=330, width=80, height=30)

#重置
reset_button = tk.Button(root, text="重置", command=reset_fields)
reset_button.place(x=150, y=365, width=80, height=30)

line3 = tk.Label(root, text="-"*50)
line3.place(x=50, y=400)

#解方程结果
solution_label = tk.Label(root, text="解方程ax**2+bx+c = 0 的结果: ", font=custom_font)
solution_label.place(x=50, y=415)

root.mainloop()