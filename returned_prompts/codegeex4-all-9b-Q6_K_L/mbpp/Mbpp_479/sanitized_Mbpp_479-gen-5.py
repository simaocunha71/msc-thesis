def first_Digit(num):
    """
    This function takes an integer as input and returns the first digit of the number.
    """
    num = abs(num)  # Handle negative numbers
    while num >= 10:
        num = num // 10  # Remove the last digit
    return num