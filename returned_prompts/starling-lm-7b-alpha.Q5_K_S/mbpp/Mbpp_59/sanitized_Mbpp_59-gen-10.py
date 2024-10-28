def is_octagonal(n):
    return is_nth_polygonal(n, 8)
def is_nth_polygonal(n, s):
    """
    Return the nth polygonal number of side length s.
    """
    return n * (s ** 2 + s) // 2