def count_integer(lst):
    count = 0
    for element in lst:
        if isinstance(element, int):
            count += 1
    return count