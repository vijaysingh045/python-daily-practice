text = input("Enter a string: ")

digits = 0

for char in text:
    if char.isdigit():
        digits += 1

print("Total digits:", digits)