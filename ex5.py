#conyourweight

weight = input("Enter your kg or gram (k/g): ")
unit = float(input("Enter your weight: "))

if weight == "k":
    kg = unit * 100
    weight = "G."
elif weight == "g":
    kg = unit / 10
    weight = "KG."
else:
    print("bro")
print(f"Result is {kg} {weight}")
    