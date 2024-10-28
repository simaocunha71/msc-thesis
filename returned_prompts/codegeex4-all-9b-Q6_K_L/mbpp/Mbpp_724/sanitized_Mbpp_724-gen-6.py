def power_base_sum(base, power):
    # Calculate the base raised to the power
    result = base ** power
    # Convert the result to a string
    result_str = str(result)
    # Sum up all the digits
    digit_sum = sum(int(digit) for digit in result_str)
    return digit_sum