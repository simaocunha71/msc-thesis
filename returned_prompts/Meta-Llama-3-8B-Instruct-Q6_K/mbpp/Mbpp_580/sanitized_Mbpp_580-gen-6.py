def extract_even(mixed_tuple):
    even_tuple = ()
    for element in mixed_tuple:
        if isinstance(element, tuple):
            even_tuple += extract_even(element)
        elif element % 2 == 0:
            even_tuple += (element,)
    return even_tuple