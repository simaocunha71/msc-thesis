def median_numbers(a, b, c):
    return max(min(a, b), min(max(a, b), c))

assert median_numbers(25,55,65)==55.0

"""
