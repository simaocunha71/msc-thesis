def sum_digits(n):
    return sum(int(digit) for digit in str(n))

# Test the function
assert sum_digits(345)==12


