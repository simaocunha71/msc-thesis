def digit_distance_nums(n1, n2):
    """
    Find the sum of the per-digit difference between two integers.
    """
    return sum(abs(int(digit) - int(digit)) for digit in str(n1) for digit in str(n2))