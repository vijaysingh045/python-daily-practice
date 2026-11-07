items = []

while True:
    print("\n1. Add Item")
    print("2. View Items")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.append(item)
        print("Item added successfully!")

    elif choice == "2":
        print("Shopping List:", items)

    elif choice == "3":
        item = input("Enter item to remove: ")

        if item in items:
            items.remove(item)
            print("Item removed!")
        else:
            print("Item not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")