def extract_even(t):
    """
    >>> extract_even((4, 5, (7, 6, (2, 4)), 6, 8))
    (4, (6, (2, 4)), 6, 8)
    """
    if isinstance(t, tuple):
        new_t = []
        for elem in t:
            if isinstance(elem, tuple):
                new_t.append(extract_even(elem))
            elif isinstance(elem, int):
                if elem % 2 == 0:
                    new_t.append(elem)
        return tuple(new_t)
    else:
        return t