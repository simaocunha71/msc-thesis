def extract_even(tup):
    """
    This function will take a nested tuple and return a new tuple with only the even numbers.
    """
    result = []
    for i in tup:
        if type(i) == tuple:
            result.append(extract_even(i))
        elif i % 2 == 0:
            result.append(i)
    return tuple(result)