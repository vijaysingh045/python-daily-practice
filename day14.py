transactions = []

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter income: "))
        transactions.append(["Income", amount])
        print("Income added!")

    elif choice == "2":
        amount = float(input("Enter expense: "))
        transactions.append(["Expense", amount])
        print("Expense added!")

    elif choice == "3":
        for item in transactions:
            print(item[0], ":", item[1])

    elif choice == "4":
        income = 0
        expense = 0

        for item in transactions:
            if item[0] == "Income":
                income += item[1]
            else:
                expense += item[1]

        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Remaining Balance:", income - expense)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")