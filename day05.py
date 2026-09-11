day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if year <= 0:
    print("Invalid year")

elif month < 1 or month > 12:
    print("Invalid month")

else:
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False

    if month == 2:
        days = 29 if leap else 28

    elif month in [4, 6, 9, 11]:
        days = 30

    else:
        days = 31

    if day >= 1 and day <= days:
        print("Valid Date")

        if leap:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Invalid Date")