def armstrong_number(n):
    # convert the number to string to get the number of digits
    num_str = str(n)
    num_digits = len(num_str)
    
    # calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    
    # check if the sum is equal to the original number
    return armstrong_sum == n