text = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0

for char in text.lower():

    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)