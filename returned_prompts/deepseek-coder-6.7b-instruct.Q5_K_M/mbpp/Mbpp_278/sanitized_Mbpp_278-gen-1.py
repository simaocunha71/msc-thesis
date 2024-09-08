def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            break
        count += 1
    return count