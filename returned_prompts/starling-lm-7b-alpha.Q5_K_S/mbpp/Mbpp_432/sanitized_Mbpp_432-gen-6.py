def median_trapezium(a, b, c):
    """
    Find the median length of a trapezium

    Parameters:
    a (int): one of the base of the trapezium
    b (int): the other base of the trapezium
    c (int): the height of the trapezium

    Returns:
    int: the median length of the trapezium
    """
    # The median length of a trapezium is half of the height times the sum of the bases, divided by 2
    return (c * (a + b)) / 2