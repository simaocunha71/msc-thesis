def extract_even(t):
    new_tuple = ()
    for element in t:
        if isinstance(element, tuple):
            new_tuple += extract_even(element)
        elif element % 2 == 0:
            new_tuple += (element,)
    return new_tuple