try:
    name = input("Enter student name: ")

    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))

    if not (0 <= m1 <= 100 and
            0 <= m2 <= 100 and
            0 <= m3 <= 100):
        print("Marks must be between 0 and 100!")

    else:
        total = m1 + m2 + m3
        percentage = total / 3

        print("\nStudent Name:", name)
        print("Total Marks:", total)
        print("Percentage:", round(percentage, 2))

        if m1 >= 33 and m2 >= 33 and m3 >= 33:
            print("Result: Pass")
        else:
            print("Result: Fail")

except ValueError:
    print("Invalid input! Please enter numbers for marks")