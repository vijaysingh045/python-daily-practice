numbers = [23, 98, 45, 90, 1, 35, 46, 87]

n = len(numbers)

for i in range(n):
    for j in range(n - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted List:", numbers)
print("Greatest Number:", numbers[-1])

