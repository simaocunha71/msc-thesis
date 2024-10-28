def count_first_elements(tup):
    count = 0
    for e in tup:
        if not isinstance(e, tuple):
            count += 1
    return count



