def substract_elements(tup1, tup2):
    result = tuple(a - b for a, b in zip(tup1, tup2))
    return result