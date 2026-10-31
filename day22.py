a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("First number is greatest")
elif b > a and b > c:
    print("Second number is greatest")
elif c > a and c > b:
    print("Third number is greatest")
else:
    print("Some numbers are equal")