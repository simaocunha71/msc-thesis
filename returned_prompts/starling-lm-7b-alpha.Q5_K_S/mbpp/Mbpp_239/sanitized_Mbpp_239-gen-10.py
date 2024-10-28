def get_total_number_of_sequences(m, n):
    """
    Returns the total number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
    >>> get_total_number_of_sequences(10, 4)
    4
    """
    # Initialize the result
    result = 0
    # Initialize the first element of the sequence
    element = 2

    # Compute the total number of possible sequences of length n
    for _ in range(n):
        # If the element is less than or equal to m, increment the result and update the element
        if element <= m:
            result += 1
            element += 1
        # Otherwise, update the element to twice the previous element
        else:
            element *= 2

    return result