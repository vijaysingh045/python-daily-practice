students = {}

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        students[roll] = {
            "name": name,
            "marks": marks
        }

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for roll, data in students.items():
                print(roll, data["name"], data["marks"])

    elif choice == "3":
        roll = input("Enter roll number to search: ")

        if roll in students:
            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll number to delete: ")

        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")