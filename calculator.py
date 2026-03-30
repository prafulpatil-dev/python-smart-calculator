def add(num1, num2):
    print(f"Result: {num1} + {num2} = {num1 + num2}")

def sub(num1, num2):
    print(f"Result: {num1} - {num2} = {num1 - num2}")

def multi(num1, num2):
    print(f"Result: {num1} x {num2} = {num1 * num2}")

def div(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print(f"Result: {num1} / {num2} = {num1 / num2}")


print("This is a Smart Calculator!")

try:
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
except ValueError:
    print("Characters are not allowed!")
    exit()

print("Choose Operation:")
print("1: +")
print("2: -")
print("3: *")
print("4: /")

choose = input("Enter: ")

if choose == "1":
    add(num1, num2)
elif choose == "2":
    sub(num1, num2)
elif choose == "3":
    multi(num1, num2)
elif choose == "4":
    div(num1, num2)
else:
    print("Invalid choice!")