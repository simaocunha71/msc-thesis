def extract_even(nested_tuple):
    even_tuple = ()
    for item in nested_tuple:
        if isinstance(item, tuple):
            even_tuple += extract_even(item)
        elif item % 2 == 0:
            even_tuple += (item,)
    return even_tuple