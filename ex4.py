choose = input("choose 1 ( + - / * ^):")
num1 = float(input("Enter number:"))
num2 = float(input("Enter number:"))

if choose == "+" :
    total = num1 + num2
    print(f"Result is {round(total, 2)}")
elif choose == "-" :
    total = num1 - num2
    print(f"Result is {round(total, 2)}")
elif choose == "/" :
    total = num1 / num2
    print(f"Result is {round(total, 2)}")
elif choose == "*" :
    total = num1 * num2
    print(f"Result is {round(total, 2)}")
elif choose == "^" :
    total = pow(num1, num2)
    print(f"Result is {round(total, 2)}")
else:
    print("bro why you do that?")