def sum_Of_product(n):
    assert n >= 0, "n must be non-negative"
    # Initialize the result
    result = 0
    # Initialize the first two terms
    result += 1
    result += 1
    # Calculate the remaining terms
    for i in range(2, n + 1):
        result += (i + 1)
        result *= i
    return result