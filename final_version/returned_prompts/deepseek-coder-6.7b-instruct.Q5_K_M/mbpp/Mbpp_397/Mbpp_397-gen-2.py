def median_numbers(a, b, c):
    """
    This function finds the median of three numbers.
    """
    return a + b + c - min(a, b, c) - max(a, b, c)

assert median_numbers(25,55,65)==55.0

#Task-2
