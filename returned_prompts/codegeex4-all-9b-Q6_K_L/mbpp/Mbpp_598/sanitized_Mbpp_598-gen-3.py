def armstrong_number(n):
    # Convert the number to a string to easily iterate over its digits
    str_n = str(n)
    # Calculate the sum of the cubes of the digits
    sum_cubes = sum(int(digit) ** 3 for digit in str_n)
    # Check if the sum is equal to the original number
    return sum_cubes == n