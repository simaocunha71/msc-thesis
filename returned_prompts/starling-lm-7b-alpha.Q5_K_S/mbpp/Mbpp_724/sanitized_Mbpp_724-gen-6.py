def power_base_sum(base, power):
    '''This function takes base and power as arguments and calculate the sum of all digits of the base to the specified power.'''
    # Initialize the result
    result = 0
    # Calculate the sum of all digits of the base to the specified power
    for i in range(power + 1):
        result += int(str(base)[i])
    # Return the result
    return result