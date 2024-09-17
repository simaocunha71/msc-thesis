def count_first_elements(t):
    count = 0
    for i, element in enumerate(t):
        if isinstance(element, tuple):
            break
        count += 1
    return count