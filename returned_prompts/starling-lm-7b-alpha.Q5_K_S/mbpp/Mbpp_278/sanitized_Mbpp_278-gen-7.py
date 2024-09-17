def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            count += len(i)
        else:
            count += 1
    return count