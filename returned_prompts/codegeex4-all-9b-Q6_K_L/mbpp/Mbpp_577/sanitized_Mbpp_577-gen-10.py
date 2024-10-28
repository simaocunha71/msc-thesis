def last_Digit_Factorial(n):
    # If n is 0 or 1, the factorial is 1, so the last digit is 1
    if n == 0 or n == 1:
        return 1
    # If n is 2, the factorial is 2, so the last digit is 2
    elif n == 2:
        return 2
    # If n is 3, the factorial is 6, so the last digit is 6
    elif n == 3:
        return 6
    # If n is 4, the factorial is 24, so the last digit is 4
    elif n == 4:
        return 4
    # If n is 5, the factorial is 120, so the last digit is 0
    elif n == 5:
        return 0
    # If n is 6, the factorial is 720, so the last digit is 0
    elif n == 6:
        return 0
    # If n is 7, the factorial is 5040, so the last digit is 0
    elif n == 7:
        return 0
    # If n is 8, the factorial is 40320, so the last digit is 2
    elif n == 8:
        return 2
    # If n is 9, the factorial is 362880, so the last digit is 8
    elif n == 9:
        return 8
    # If n is 10, the factorial is 3628800, so the last digit is 0
    elif n == 10:
        return 0