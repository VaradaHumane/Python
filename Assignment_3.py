print("Please enter two numbers and select an operation.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nOperations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

num = input("\nEnter the operator (1-4): ")

number = int(num)

if number == 1:
    print("The sum between", num1, "and", num2, "is:", num1 + num2)
elif number == 2:
    print("The difference between", num1, "and", num2, "is:", num1 - num2)
elif number == 3:
    print("The product between", num1, "and", num2, "is:", num1 * num2)
elif number == 4:
    print("The quotient between", num1, "and", num2, "is:", num1 / num2)
else:
    print("invaild operator selected")
    exit()
