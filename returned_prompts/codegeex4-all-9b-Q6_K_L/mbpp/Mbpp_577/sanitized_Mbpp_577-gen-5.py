def last_Digit_Factorial(n):
    """
    Function to find the last digit in factorial of a given number.
    """
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial % 10