from tkinter import *

current_expression = ""
input_field = None  
last_result = ""  

def click_button(value):
    global current_expression, input_field, last_result
    if value in ['C', '=', '+/-', '%', '⌦']:
        return  
    current_expression += str(value)
    input_field.delete(0, END)
    input_field.insert(0, current_expression)

def clear():
    global current_expression, input_field, last_result
    current_expression = ""
    last_result = "" 
    input_field.delete(0, END)
    input_field.insert(0, "0")

def backspace():
    
    global current_expression, input_field
    if current_expression:
        current_expression = current_expression[:-1]
        input_field.delete(0, END)
        input_field.insert(0, current_expression or "0")

def percent():

    global current_expression, input_field, last_result
    try:
        if current_expression:
            value = float(current_expression)
            result = value / 100
            last_result = str(result)
            input_field.delete(0, END)
            input_field.insert(0, f"{result:g}")
            current_expression = ""
    except:
        input_field.delete(0, END)
        input_field.insert(0, "Ошибка")

def plus_minus():

    global current_expression, input_field
    try:
        if current_expression:
            value = float(current_expression)
            result = -value
            current_expression = str(result)
            input_field.delete(0, END)
            input_field.insert(0, current_expression)
    except:
        pass

def calculate():
    global current_expression, input_field, last_result
    
    operation = current_expression.strip()
    result = None 
    

    if operation in ['+', '-']:
        input_field.delete(0, END)
        input_field.insert(0, f"{last_result or '0'}{operation} (введите число)")
        return
        

    if '+' in operation and operation.count('+') == 1:
        try:
            parts = operation.split('+')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                result = a + b
        except: pass
    
    elif '-' in operation and operation.count('-') == 1:
        try:
            parts = operation.split('-')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                result = a - b
        except: pass
    
    elif 'X' in operation:
        try:
            parts = operation.split('X')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                result = a * b
        except: pass
    
    elif '/' in operation:
        try:
            parts = operation.split('/')
            if len(parts) == 2:
                a = float(parts[0]) if parts[0] else float(last_result or 0)
                b = float(parts[1])
                if b != 0:
                    result = a / b
                else:
                    input_field.delete(0, END)
                    input_field.insert(0, "Ошибка")
                    return
        except: pass
    
    else: 
        input_field.delete(0, END)
        input_field.insert(0, "неверная операция")
        return
    
    if result is not None:
        last_result = str(result)
        input_field.delete(0, END)
        input_field.insert(0, f"{result:g}")  
        current_expression = ""  

root = Tk()
root.title("Калькулятор")
root.geometry("500x700")
root.configure(bg='lightgray')

root.eval('tk::PlaceWindow . center')

input_field = Entry(root, font=('Arial', 25), width=22, justify=RIGHT, 
                   relief=SOLID, bd=2, bg='white', fg='black')
input_field.grid(row=0, column=0, columnspan=4, padx=20, pady=20, 
                 sticky="ew", ipady=20, ipadx=10)


special_buttons = [
    ('⌦', backspace, 1, 0),
    ('C', clear, 1, 1), 
    ('%', percent, 1, 2),
    ('+/-', plus_minus, 5, 0),
    ('=', calculate, 5, 3)
]

normal_buttons = [
    ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('X', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 1), ('.', 5, 2)
]
for text, func, row, col in special_buttons:

    Button(root, text=text, padx=20, pady=20, font=('Arial', 22),
           command=func, bg='white', relief=RAISED, bd=2)\
    .grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

for text, row, col in normal_buttons:

    Button(root, text=text, padx=20, pady=20, font=('Arial', 22),
           command=lambda t=text: click_button(t), 
           bg='white', relief=RAISED, bd=2)\
    .grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
