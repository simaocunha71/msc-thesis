def is_num_decagonal(n):
    """
    Write a function to find the nth decagonal number.
    """
    # Initialize result
    result = 0

    # Calculate nth decagonal number
    for i in range(1, n + 1):
        result += i * 10

    # Return result
    return result
result = 0