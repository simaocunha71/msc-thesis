def count_first_elements(t):
    count = 0
    for el in t:
        if isinstance(el, tuple):
            break
        count += 1
    return count