def first_Digit(n):
    try:
        while n >= 10:
            n //= 10
        return n
    except TypeError:
        print("Invalid input. Please enter a positive integer.")