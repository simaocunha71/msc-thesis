def armstrong_number(n):
    # Convert the number to a string to easily access each digit
    str_n = str(n)
    # Calculate the length of the number
    length = len(str_n)
    # Initialize a variable to store the sum of the digits raised to the power of their length
    total = 0
    # Loop through each digit in the number
    for digit in str_n:
        # Add the digit raised to the power of its length to the total
        total += int(digit) ** length
    # If the total is equal to the original number, then it is an armstrong number
    return total == n