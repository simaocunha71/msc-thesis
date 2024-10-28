def get_total_number_of_sequences(m, n):
    """
    Finds the number of possible sequences of length n,
    such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
    """
    if n == 1:
        return m
    else:
        return (m - 1) + get_total_number_of_sequences(m, n - 1)