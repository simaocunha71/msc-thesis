def count_first_elements(t):
    count = 0
    for elem in t:
        if isinstance(elem, tuple):
            break
        count += 1
    return count