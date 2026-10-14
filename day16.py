def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_percentage(total):
    return total / 3


def calculate_grade(percentage):
    if percentage >= 90:
        return "A Grade"
    elif percentage >= 75:
        return "B Grade"
    elif percentage >= 60:
        return "C Grade"
    elif percentage >= 33:
        return "D Grade"
    else:
        return "Fail"


name = input("Enter student name: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

if all(0 <= marks <= 100 for marks in [m1, m2, m3]):
    total = calculate_total(m1, m2, m3)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)

    print("\n===== STUDENT RESULT =====")
    print("Name:", name)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
else:
    print("Marks must be between 0 and 100.")