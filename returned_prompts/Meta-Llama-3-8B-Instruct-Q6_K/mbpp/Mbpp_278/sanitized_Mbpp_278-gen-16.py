def count_first_elements(t):
    count = 0
    for x in t:
        if not isinstance(x, tuple):
            count += 1
        else:
            return count
    return count