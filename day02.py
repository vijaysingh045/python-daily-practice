num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Arithmetic Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")

print("\n--- Comparison ---")

if num1 > num2:
    print("First number is greater.")
elif num1 < num2:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")