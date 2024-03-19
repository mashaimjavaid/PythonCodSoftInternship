import tkinter as tk
import math

root = tk.Tk()
root.geometry("300x350")
root.title("Calculator")
root.resizable(width=False, height=False)
l = tk.Label(root, text = " ")
result = tk.Text(root, height=1, width=15, font=("Arial",24))
expression = ""

def press_button(calculator_button):  
    global expression 
    expression = expression + str(calculator_button) 
    result.delete(1.0, "end")
    result.insert(1.0, expression)

def evaluate_expression():
    try: 
        global expression  
        total = str(eval(expression))
        result.delete(1.0, "end") 
        result.insert(1.0, total)
        expression = total
    except: 
        result.delete(1.0, "end")
        result.insert(1.0, "Error")
        expression = total

def clear_all():
    global expression
    expression = ""
    result.delete(1.0, "end")

def squareRoot():
    try:
        global expression
        square_root = str(math.sqrt(float(expression)))
        result.delete(1.0, "end")
        result.insert(1.0, square_root)
        expression = square_root
    except Exception as e:
        result.delete(1.0, "end")
        result.insert(1.0, "Error")
        expression = ""

def factorial():
    try:
        global expression
        square_root = str(math.factorial(int(float(expression))))
        result.delete(1.0, "end")
        result.insert(1.0, square_root)
        expression = square_root
    except Exception as e:
        result.delete(1.0, "end")
        result.insert(1.0, "Error")
        expression = ""

def backspace():
    global expression
    backspace = result.get(1.0, "end")[:-2]
    result.delete(1.0, "end")
    result.insert(1.0, backspace)

num_1_btn = tk.Button(root, text="c", height = 2, width=3, command=clear_all)
num_1_btn.place(x=20,y=75)
num_2_btn = tk.Button(root, text="√", height = 2, width=3, command=squareRoot)
num_2_btn.place(x=95,y=75)
num_3_btn = tk.Button(root, text="/", height = 2, width=3, command=lambda: press_button("/"))
num_3_btn.place(x=170,y=75)
num_4_btn = tk.Button(root, text="<-", height = 2, width=3, command=backspace)
num_4_btn.place(x=245,y=75)

num_5_btn = tk.Button(root, text="7", height = 2, width=3, command=lambda: press_button(7))
num_5_btn.place(x=20,y=125)
num_6_btn = tk.Button(root, text="8", height = 2, width=3, command=lambda: press_button(8))
num_6_btn.place(x=95,y=125)
num_7_btn = tk.Button(root, text="9", height = 2, width=3, command=lambda: press_button(9))
num_7_btn.place(x=170,y=125)
num_8_btn = tk.Button(root, text="*", height = 2, width=3, command=lambda: press_button("*"))
num_8_btn.place(x=245,y=125)

num_9_btn = tk.Button(root, text="4", height = 2, width=3, command=lambda: press_button(4))
num_9_btn.place(x=20,y=175)
num_10_btn = tk.Button(root, text="5", height = 2, width=3, command=lambda: press_button(5))
num_10_btn.place(x=95,y=175)
num_11_btn = tk.Button(root, text="6", height = 2, width=3, command=lambda: press_button(6))
num_11_btn.place(x=170,y=175)
num_12_btn = tk.Button(root, text="-", height = 2, width=3, command=lambda: press_button("-"))
num_12_btn.place(x=245,y=175)

num_13_btn = tk.Button(root, text="1", height = 2, width=3, command=lambda: press_button(1))
num_13_btn.place(x=20,y=225)
num_14_btn = tk.Button(root, text="2", height = 2, width=3, command=lambda: press_button(2))
num_14_btn.place(x=95,y=225)
num_15_btn = tk.Button(root, text="3", height = 2, width=3, command=lambda: press_button(3))
num_15_btn.place(x=170,y=225)
num_16_btn = tk.Button(root, text="+", height = 2, width=3, command=lambda: press_button("+"))
num_16_btn.place(x=245,y=225)

num_17_btn = tk.Button(root, text="!", height = 2, width=3, command=factorial)
num_17_btn.place(x=20,y=275)
num_18_btn = tk.Button(root, text="0", height = 2, width=3, command=lambda: press_button(0))
num_18_btn.place(x=95,y=275)
num_19_btn = tk.Button(root, text=".", height = 2, width=3, command=lambda: press_button("."))
num_19_btn.place(x=170,y=275)
num_20_btn = tk.Button(root, text="=", height = 2, width=3, command=evaluate_expression)
num_20_btn.place(x=245,y=275)

l.pack()
result.pack()
root.mainloop()

  