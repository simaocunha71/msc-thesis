def count_first_elements(my_tuple):
    count = 0
    for el in my_tuple:
        if not isinstance(el, tuple):
            count += 1
    return count
