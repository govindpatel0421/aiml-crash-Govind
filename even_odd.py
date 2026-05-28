try:
    number = int(input("Enter a number: "))

    if number == 0:
        print("The number is zero.")
    elif number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

except ValueError:
    # int("abc") gives ValueError because "abc" cannot be converted into an integer.
    print("Invalid input! Please enter a valid number.")