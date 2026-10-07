products = {
    "apple": 50,
    "banana": 30,
    "milk": 60,
    "bread": 40,
    "rice": 80
}

cart = {}

while True:

    print("\n===== SHOPPING CART =====")
    print("1. View Products")
    print("2. Add Product")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nAvailable Products:")

        for product, price in products.items():
            print(product, "₹", price)

    elif choice == "2":

        product = input("Enter product name: ").lower()

        if product in products:

            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                cart[product] = cart.get(product, 0) + quantity
                print("Product added to cart!")
            else:
                print("Invalid quantity.")

        else:
            print("Product not available.")

    elif choice == "3":

        if len(cart) == 0:
            print("Cart is empty.")

        else:
            print("\nYour Cart:")

            total = 0

            for product, quantity in cart.items():

                price = products[product]
                amount = price * quantity
                total += amount

                print(product, "x", quantity, "=", amount)

            print("Total: ₹", total)

    elif choice == "4":

        product = input("Enter product to remove: ").lower()

        if product in cart:
            del cart[product]
            print("Product removed!")
        else:
            print("Product not found in cart.")

    elif choice == "5":

        if len(cart) == 0:
            print("Cart is empty.")

        else:
            total = 0

            for product, quantity in cart.items():
                total += products[product] * quantity

            print("\n===== BILL =====")
            print("Total Amount: ₹", total)
            print("Thank you for shopping!")

    elif choice == "6":

        print("Program closed.")
        break

    else:
        print("Invalid choice.")