x = int(input("Enter your number (not float): "))

for i in range (1,x + 1):
    if i % 2 == 0:
        print(f"{i} is even number")
    elif i % 2 == 1:
        print(f"{i} is odd number")
    else:
        print("error")