def power_base_sum(base, power):
    # Initialize result
    result = 0

    # Calculate the sum
    for _ in range(power + 1):
        result += base

    # Return the result
    return result