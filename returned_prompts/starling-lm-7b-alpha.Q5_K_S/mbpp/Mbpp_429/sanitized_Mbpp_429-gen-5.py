def and_tuples(tup1, tup2):
    """
    Extract the elementwise and tuples from the given two tuples.
    """
    # Initialize the result
    result = []

    # Extract the elementwise and tuples
    for i in range(len(tup1)):
        result.append(tup1[i] & tup2[i])

    return result