def count_first_elements(my_tuple: tuple) -> int:
    count = 0
    for elem in my_tuple:
        if isinstance(elem, tuple):
            break
        count += 1
    return count