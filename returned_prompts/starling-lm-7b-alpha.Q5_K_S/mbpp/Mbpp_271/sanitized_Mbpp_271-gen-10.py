def even_Power_Sum(n):
    # Initialize result
    result = 0
    # Calculate sum of first n even natural numbers raised to the fifth power
    for i in range(1, n + 1):
        result += i ** 5
    return result