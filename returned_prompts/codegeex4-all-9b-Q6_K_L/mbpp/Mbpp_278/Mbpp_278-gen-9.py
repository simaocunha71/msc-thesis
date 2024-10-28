def count_first_elements(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        count += 1
    return count

