def extract_even(t):
    result = tuple()
    for elem in t:
        if isinstance(elem, tuple):
            result += (elem for elem in extract_even(elem) if elem % 2 == 0)
        elif elem % 2 == 0:
            result += elem,
    return result
t = (4, 5, (7, 6, (2, 4)), 6, 8)