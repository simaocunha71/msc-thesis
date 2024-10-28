def count_first_elements(my_tuple: tuple) -> int:
    count = 0
    for element in my_tuple:
        if isinstance(element, tuple):
            break
        count += 1
    return count