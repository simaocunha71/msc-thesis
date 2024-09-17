def armstrong_number(n):
    # Convert the number to a string to easily extract digits
    str_n = str(n)
    
    # Calculate the number of digits in the number
    num_digits = len(str_n)
    
    # Calculate the sum of cubes of the digits
    sum_cubes = sum(int(digit) ** num_digits for digit in str_n)
    
    # Check if the sum of cubes is equal to the original number
    return sum_cubes == n