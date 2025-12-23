print("калькулятор")
 # ввод чисел
# выбор действия
operation = input("выберите операцию(+ для сложения; - для вычитания; x для умножения; : для деления;  для возведения в степень:")

if operation == '+':
    a = float(input("Первое число"))  # float - дробные числа 
    b = float(input("Второе число"))
    result = a + b
    print(f"сумма  сложения: {result:g}")

elif operation == '-' : # elif - доп условия
    a = float(input("Первое число"))  # float - дробные числа 
    b = float(input("Второе число"))
    result = a - b
    print(f"результат вычитания: {result:g}")

elif operation == '*' :
    a = float(input("Первое число"))  # float - дробные числа 
    b = float(input("Второе число"))
    result = a * b
    print(f" результат умножения: {result:g}")

elif operation == ':' :
    a = float(input("Первое число"))  # float - дробные числа 
    b = float(input("Второе число"))
    result = a / b
    if b != 0:
     print(f" результат деления: {result:g}")
    else:
     print("Ошибка")

elif operation == '' :
    a = float(input("число возмодимое в степень"))  # float - дробные числа 
    b = float(input("степень"))
    result = a ** b
    print(f"результат возведения в степень: {result:g}")

else: 
    print("неверная операция")