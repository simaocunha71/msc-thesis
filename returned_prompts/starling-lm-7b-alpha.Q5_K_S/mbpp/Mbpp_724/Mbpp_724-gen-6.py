
def power_base_sum(base, power):
    # Initialize result
    res = 0
    # Calculate sum of all digits
    for i in range(0, power + 1):
        res += (base ** i)
    return res


