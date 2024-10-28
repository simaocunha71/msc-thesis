def extract_even(tup):
    result = ()
    for element in tup:
        if isinstance(element, tuple):
            element = extract_even(element)
        elif element % 2 == 0:
            result += (element,)
    return result