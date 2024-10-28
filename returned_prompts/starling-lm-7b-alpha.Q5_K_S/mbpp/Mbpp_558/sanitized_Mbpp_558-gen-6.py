def digit_distance_nums(n1, n2):
    """Returns the sum of the absolute difference between each digit of two numbers.
    >>> digit_distance_nums(1, 2)
    1
    """
    d1 = str(n1)
    d2 = str(n2)
    if len(d1) != len(d2):
        raise ValueError("The two numbers must have the same number of digits")

    diff = 0
    for i, j in zip(d1, d2):
        diff += abs(int(i) - int(j))
    return diff