balance = 10000
pin = 1234

entered_pin = int(input("Enter PIN: "))

if entered_pin == pin:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Amount Deposited:", amount)
            print("New Balance:", balance)
        else:
            print("Invalid Amount")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid Amount")

        elif amount > balance:
            print("Insufficient Balance")

        else:
            balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", balance)

    else:
        print("Invalid Choice")

else:
    print("Incorrect PIN")