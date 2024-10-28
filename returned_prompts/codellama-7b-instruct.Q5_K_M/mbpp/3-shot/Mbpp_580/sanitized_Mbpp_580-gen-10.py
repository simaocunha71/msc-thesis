def extract_even(my_tuple: tuple) -> tuple:
    result_tuple = ()
    for item in my_tuple:
        if isinstance(item, tuple):
            result_tuple += (extract_even(item),)
        elif item % 2 == 0:
            result_tuple += (item,)
    return result_tuple