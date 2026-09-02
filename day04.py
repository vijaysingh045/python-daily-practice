a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a > b and a > c and a > d:
    print("Largest a: ", a)
elif b > a and b > c and b > d:
    print("Largest b: ", b)
elif c > a and c > b and c > d:
    print("Largest c: ", c)
else:
    print("Largest d: ", d)