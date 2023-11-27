num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter mathematical operator: ")
if op in ('+', '-', '*', '/' , '//', '%', '**'):
    print("Result is", eval(f"{num1}{op}{num2}"))
else:
    print("Operator not recognized.")