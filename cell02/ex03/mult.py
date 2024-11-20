num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

result = num1 * num2

if result > 0:
    print("The result of multiplication is positive.")
elif result < 0:
    print("The result of multiplication is negative.")
else:
    print("The result of multiplication is zero.")

print(f"The result of multiplying {num1} and {num2} is: {result}")
